class logger:
    """
    i made this logger class because i couldn't find a good and customizable logger
    the class is pretty simple and straight forward but i will commment it anyway
    because...it's alaways a good idea maybe it will help someone :)
    """

    # basically these are the AINSI escape codes
    # and if you wrapp your text
    # between a "color code" and a "end code", the terminal colors you codep
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    CRITICAL = '\u001b[41m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # here you can define the decoration for each log level
    # meaning you can customize the "[+]" and "[-]" things to whatever you want

    OKBLUE_DECO = "[+]"
    OKCYAN_DECO = "[+]"
    OKGREEN_DECO = "[+]"
    WARNING_DECO = "[!]"
    FAIL_DECO = "[-]"
    CRITICAL_DECO = "[☠️]"

    """the methods of the class are :
    - info : prints a message in green for infomation purposes (you can also use okblue, okcyan for the same thing)
    - header : prints a message in purple
    - warning : prints a message in yellow
    - error (or fail they're the same thing) : prints a message in red
    - critical : prints a message in dark red
    """


    @staticmethod
    def info(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.OKGREEN}{logger.BOLD}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.OKGREEN}{logger.BOLD}[+] {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.OKGREEN}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        else:
             print(f"{logger.OKGREEN}{logger.OKGREEN_DECO} {msg}{logger.ENDC}")


    @staticmethod
    def header(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.HEADER}{logger.BOLD}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.HEADER}{logger.BOLD}[+] {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.HEADER}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        else:
            print(f"{logger.HEADER}{logger.OKBLUE_DECO} {msg}{logger.ENDC}")


    @staticmethod
    def warning(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.WARNING}{logger.BOLD}{logger.UNDERLINE}[!] {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.WARNING}{logger.BOLD}[!] {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.WARNING}{logger.UNDERLINE}[!] {msg}{logger.ENDC}")
        else:
            print(f"{logger.WARNING}{logger.WARNING_DECO} {msg}{logger.ENDC}")

    
    @staticmethod
    def error(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.FAIL}{logger.BOLD}{logger.UNDERLINE}[-] {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.FAIL}{logger.BOLD}[-] {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.FAIL}{logger.UNDERLINE}[-] {msg}{logger.ENDC}")
        else:
            print(f"{logger.FAIL}{logger.FAIL_DECO} {msg}{logger.ENDC}")

    @staticmethod
    def fail(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.FAIL}{logger.BOLD}{logger.UNDERLINE}[-] {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.FAIL}{logger.BOLD}[-] {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.FAIL}{logger.UNDERLINE}[-] {msg}{logger.ENDC}")
        else:
            print(f"{logger.FAIL}{logger.FAIL_DECO} {msg}{logger.ENDC}")


    @staticmethod
    def critical(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.CRITICAL}{logger.BOLD}{logger.UNDERLINE}{logger.CRITICAL_DECO} {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.CRITICAL}{logger.BOLD}{logger.CRITICAL_DECO} {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.CRITICAL}{logger.UNDERLINE}{logger.CRITICAL_DECO} {msg}{logger.ENDC}")
        else:
            print(f"{logger.CRITICAL}{logger.CRITICAL_DECO} {msg}{logger.ENDC}")
    
    @staticmethod
    def okcyan(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.OKCYAN}{logger.BOLD}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.OKCYAN}{logger.BOLD}[+] {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.OKCYAN}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        else:
            print(f"{logger.OKCYAN}{logger.OKCYAN_DECO} {msg}{logger.ENDC}")

    
    @staticmethod
    def okblue(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.OKBLUE}{logger.BOLD}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.OKBLUE}{logger.BOLD}[+] {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.OKBLUE}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        else:
            print(f"{logger.OKBLUE}{logger.OKBLUE_DECO} {msg}{logger.ENDC}")

  
    @staticmethod
    def okgreen(msg, bold=False, underline=False):
        if (bold and underline):
            print(f"{logger.OKGREEN}{logger.BOLD}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        elif (bold and not underline):
            print(f"{logger.OKGREEN}{logger.BOLD}[+] {msg}{logger.ENDC}")

        elif (underline and not bold):
            print(f"{logger.OKGREEN}{logger.UNDERLINE}[+] {msg}{logger.ENDC}")
        else:
            print(f"{logger.OKGREEN}{logger.OKGREEN_DECO} {msg}{logger.ENDC}")

    @staticmethod
    def bold(msg):
        print(f"{logger.BOLD}{msg}{logger.ENDC}")

    @staticmethod
    def underline(msg):
        print(f"{logger.UNDERLINE}{msg}{logger.ENDC}")

    @staticmethod
    def bold_underline(msg):
        print(f"{logger.BOLD}{logger.UNDERLINE}{msg}{logger.ENDC}")

    
if __name__ == "__main__":
    
    logger.info("info message")
    logger.info("info message bold", bold=True)
    logger.info("info message underline", underline=True)
    logger.info("info message bold and underline", bold=True, underline=True)
    logger.header("header message")
    logger.header("header message bold", bold=True)
    logger.header("header message underline", underline=True)
    logger.header("header message bold and underline", bold=True, underline=True)
    logger.warning("warning message")
    logger.warning("warning message bold", bold=True)
    logger.warning("warning message underline", underline=True)
    logger.warning("warning message bold and underline", bold=True, underline=True)
    logger.error("error message")
    logger.error("error message bold", bold=True)
    logger.error("error message underline", underline=True)
    logger.error("error message bold and underline", bold=True, underline=True)
    logger.critical("critical message")
    logger.critical("critical message bold", bold=True)
    logger.critical("critical message underline", underline=True)
    logger.critical("critical message bold and underline", bold=True, underline=True)
    logger.okcyan("okcyan message")
    logger.okcyan("okcyan message bold", bold=True)
    logger.okcyan("okcyan message underline", underline=True)
    logger.okcyan("okcyan message bold and underline", bold=True, underline=True)
    logger.okblue("okblue message")
    logger.okblue("okblue message bold", bold=True)
    logger.okblue("okblue message underline", underline=True)
    logger.okblue("okblue message bold and underline", bold=True, underline=True)
    









