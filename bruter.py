#!/bin/python
import requests
import threading
from args_parser import parser
from logger import logger as log
from time import sleep
import utils

verbosity = True
args = parser.parse_args() # argument parser set up in ./args_parser.py

# setting verbbosity and checking if the user wants to use a wordlist or not
if (args.login is None and args.login_file is None):
    parser.error('you must specify a login or a login file')
if (args.password is None and args.password_file is None):
    parser.error('you must specify a password or a password file')
if (args.quiet):
    verbosity = False

# loading username and password in python Lists whether they are single or wordlists
username_list = []
password_list = []
if (args.login is not None):
    username_list = [args.login]
if (args.login_file is not None):
    with open(args.login_file, 'r') as f:
        username_list = f.read().splitlines()
if (args.password is not None):
    password_list = [args.password]
if (args.password_file is not None):
    with open(args.password_file, 'r') as f:
        password_list = f.read().splitlines()


# the function that will be used to test the login it is pretty straight forward, it just sends a request to the website
# and checks if the website redirects to a page (i.e dashbord.php, home...)) in other words if the request url changed
# if so, it means that the login was successful
def brute_force(username, password):
    global verbosity
    global args

    session = requests.Session()
    payload = {args.login_param_name: username,
               args.password_param_name: password}
    post_req = session.post(args.url, data=payload)
    if (args.url != post_req.url): # i will add more conditions to check wether the login was successful or not 
                                   # as i come accross them and that are not explicit countrary to the usual "incorrect password" etc...
                                   # if you have any other conditions to check that would indicate if the login was successful or not you can add them
        
        log.info(
            f"found a valid username and password {username}:{password}", bold=True, underline=True)
        # killing all threads before exiting
        for thread in threading.enumerate():
            if thread is not threading.current_thread():
                thread.join()
        exit(0)

    else:
        if (verbosity):
            log.fail(f"{username}:{password} is not a valid login")
        session.close()
        sleep(args.wait)


def main():
    global verbosity
    global args
    global brute_force
    if (verbosity):

        log.header(f"starting brute force with {args.threads} threads")
    connection_success = False
    times = 0
    while not connection_success:
        connection_success = utils.try_connection(args.url, timeout=args.wait, follow_redirects=args.follow_redirects)
        if not connection_success and times < 5:
            log.error("connection failed, retrying...")
            times += 1
            sleep(args.wait)

        if times == 5:
            log.error("connection failed, exiting...")
            exit(1)

    if connection_success:
        log.okblue("connection successful")
    for username in username_list:
        for password in password_list:
            t = threading.Thread(target=brute_force, args=(username, password))
            t.start()
            # this infinite loop will run if the count of the active threads is higher than the threads allowed by the user to stop creation of new threads
            # once this number of active threads goes down, we exit from the loop and we can start new threads
            while threading.active_count() > args.threads:
                pass


if __name__ == "__main__":
    utils.print_banner()
    main()
