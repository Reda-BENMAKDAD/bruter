import requests

def try_connection(url, port=None, path=None):
    if (port is None):
        port = 80
    if (path is None):
        path = "/"
    try:
        r = requests.get(f"http://{url}:{port}{path}")
        if (r.status_code == 200):
            return True
        else:
            return False
    except:
        return False
    
    
def print_banner() -> None:
    print("""
     _   _  _   ___   __  _   _ _____ _____   _   ___   _____________  ___  
| \ | || | | \ \ / / | \ | |  _  |_   _| | | | \ \ / /  _  \ ___ \/ _ \ 
|  \| || |_| |\ V /  |  \| | | | | | |   | |_| |\ V /| | | | |_/ / /_\ \\
| . ` ||  _  | \ /   | . ` | | | | | |   |  _  | \ / | | | |    /|  _  |
| |\  || | | | | |   | |\  \ \_/ / | |   | | | | | | | |/ /| |\ \| | | |
\_| \_/\_| |_/ \_/   \_| \_/\___/  \_/   \_| |_/ \_/ |___/ \_| \_\_| |_/
    """)