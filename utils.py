import requests
import urllib

def try_connection(url, follow_redirects=True):
    try:
        response = requests.get(url, timeout=10, allow_redirects=follow_redirects)
        if response.status_code in (200, 3):
            return {"success": True, "message":"Connection successful"}
        else:
            return {"success": False, "message": f"Connection failed. Status code: {response.status_code}"}
    except requests.ConnectionError as e:
        return {"success": False, "message":f"Connection failed: This may be due to a bad internet network or DNS resolution issue."}
    except requests.Timeout as e:
        return {"success": False, "message": f"Connection timed out."}
    except requests.RequestException as e:
        return {"success":False, "message": f"An error occurred during the request: {str(e)}"}
    
    
def print_banner() -> None:
    print("""
     _   _  _   ___   __  _   _ _____ _____   _   ___   _____________  ___  
| \ | || | | \ \ / / | \ | |  _  |_   _| | | | \ \ / /  _  \ ___ \/ _ \ 
|  \| || |_| |\ V /  |  \| | | | | | |   | |_| |\ V /| | | | |_/ / /_\ \\
| . ` ||  _  | \ /   | . ` | | | | | |   |  _  | \ / | | | |    /|  _  |
| |\  || | | | | |   | |\  \ \_/ / | |   | | | | | | | |/ /| |\ \| | | |
\_| \_/\_| |_/ \_/   \_| \_/\___/  \_/   \_| |_/ \_/ |___/ \_| \_\_| |_/
    """)
    
if __name__ == "__main__":
    print_banner()
    url1 = "https://google.com/"
    url2 = "http://example.com"
    url3 = "http://qwdvqvqrevwerc.com"
    url4 = "https://twitter.com/unexistingpageervwerwer"
    print(try_connection(url1))
    print(try_connection(url2))
    print(try_connection(url3))
    print(try_connection(url4))
    