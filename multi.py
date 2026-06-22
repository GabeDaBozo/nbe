import os
import random
import time
import colorama
from colorama import Fore, Style
import json
import requests
import discord
import asyncio
from time import sleep
from discord.ext import commands

colorama.init()

nbe_watermark = """███╗   ██╗██████╗ ███████╗
████╗  ██║██╔══██╗██╔════╝
██╔██╗ ██║██████╔╝█████╗  
██║╚██╗██║██╔══██╗██╔══╝  
██║ ╚████║██████╔╝███████╗
╚═╝  ╚═══╝╚═════╝ ╚══════╝
                          """

nbe_start = "Pick Option: "

print(nbe_watermark)

time.sleep(2.5)

print(nbe_start)


print("1: IP TO INFO/GEO")
print("2: DOX CREATOR")
print("3: DISCORD SELFBOT")
print("4: CUSTOM OSINT")
print("5: IP GRABBER")
print("6: MALWARE BUILDER")


choice = input("What Do You Pick: ")

def ip_to_geo(ip):
    url = f"http://ip-api.com/json/{ip}"
    req = requests.get(url)
    dat = req.json()

    if dat["status"] == "success":
        print(f"IP: {dat['query']}")
        print(f"COUNTRY: {dat['country']}")
        print(f"REGION: {dat['regionName']}")
        print(f"CITY: {dat['city']}")
        print(f"ISP: {dat['isp']}")
        print(f"LATITUDE COORD: {dat['lat']}")
        print(f"LONGITUDE COORD: {dat['lon']}")
    else:
        print("Invalid IP")

if choice == "1":
    print("Selected IP TO INFO")
    ip = input("Enter Your Dedicated IP: ")
    ip_to_geo(ip)

elif choice == "2":
    print("Selected Dox Creator")

    name = input("Enter Name/Full Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    country = input("Enter Country: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    social_users = input("Enter All Social Usernames (blank if none): ")
    pedo_or_not = input("Is This Person A Pedophile (yes/no): ")

    dox_data = {
        "name": name,
        "age": age,
        "location": {
            "city": city,
            "state": state,
            "country": country
        },
        "contact": {
            "phone": phone,
            "email": email
        },
        "social_users": social_users,
        "pedo_or_not": pedo_or_not
    }

    print("\nGenerated DOX JSON:")
    print(json.dumps(dox_data, indent=4))