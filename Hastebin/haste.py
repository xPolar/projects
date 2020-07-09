import requests
from colorama import init
init()
print("\033[0;32;40m")
input = str(input("Please enter what you would like to be hasted! (If you're hasting a file please provide the complete path of the file): "))
try:
    file = open(input, "r")
except FileNotFoundError:
    input = input.replace(r"\n", "\n")
else:
    input = file.read()
if input != "":
    r = requests.post("https://hastebin.com/documents", data = input.encode('utf-8'))
    json = r.json()
    print(f"\033[0;35;40mI hasted that for you!\n\033[1;34;40mhttps://hastebin.com/{json['key']}")
else:
    print("\033[1;31;40mPlease provide some text, you can't haste nothing!")