import json
import os

userName = input("Input User Name: ")
password = input("Input Password: ")

data1 = {"username": userName, "password": password}

with open("./user_data.json", 'r', encoding='utf8') as input:
    table_json = json.load(input)


add = True

for acc in table_json["accounts"]:
    if data1["username"] == acc["username"] and data1["password"] == acc["password"]:
        add = False
        print("Admin Logged In")
        os.system("python SecondDiff-BotLine.py")

if add:
    print("ID or Password are wrong , please try again")
