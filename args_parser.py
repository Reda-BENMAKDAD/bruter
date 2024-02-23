from argparse import ArgumentParser, RawTextHelpFormatter

# setting the argument parser
parser = ArgumentParser(description="""
Description: this is a python script to bruteforce a website's login page.
this python script implements an option that hydra does not have.
basically in hydra, you check if login is succesful or not by checking the presence of an error string,
but sometimes the error string is not present in the page when login is not successful, 
the website simply redirects to a page on succesful login, or says nothing.
this script checks if the login is successful by if checking the website redirects to a page (i.e dashbord.php, home...))""",
                        formatter_class=RawTextHelpFormatter)

# all the arguments that you'll find in the help menu
parser.add_argument('-u', '--url', type=str, metavar='',
                    help='the url of the website to brute force (the url should be full not relative eg. http://example.com/login.php)', required=True)
login_group = parser.add_mutually_exclusive_group()
login_group.add_argument('-l', '--login', type=str,
                         metavar='', help='a single username to test')
login_group.add_argument('-L', '--login-file', type=str,
                         metavar='', help='wordlist of usernames to test')
password_group = parser.add_mutually_exclusive_group()
password_group.add_argument(
    '-p', '--password', type=str, metavar='', help='a single password to test')
password_group.add_argument('-P', '--password-file', type=str,
                            metavar='', help='wordlist of passwords to test')

parser.add_argument('-lp', '--login-param-name', type=str,
                    metavar='', help='the login parameter\'s name of the website')
parser.add_argument('-pp', '--password-param-name', type=str,
                    metavar='', help='the password parameter\'s name of the website')

verbosity_group = parser.add_mutually_exclusive_group()
verbosity_group.add_argument(
    '-v', '--verbose', action='store_false', help='increase output verbosity')
verbosity_group.add_argument(
    '-q', '--quiet', action='store_true', help='decrease output verbosity')

parser.add_argument('-t', '--threads', default=10, type=int, metavar='',
                    help='the number of threads to use (default=10)', required=False)
parser.add_argument('-w', '--wait', default=1, type=int, metavar='',
                    help='the time to wait between each request in seconds (default=0)', required=False)
parser.add_argument("-fr", "--follow-redirects", default=True, type=bool, metavar='',
                    help="whether or not to follow redirect, and thus treat 3XX status codes as failure or not", required=False)
