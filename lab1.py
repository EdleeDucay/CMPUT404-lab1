import requests

#print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/EdleeDucay/CMPUT404-lab1/main/lab1.py")

print(resp.text)