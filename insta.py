#!/usr/lib/python3.7
# Instagram Page iNFo
# IRAN CYBER SECURITY GROUP

from json import loads
from requests import get
import sys
from random import choice
from colorama import Fore, Style
from os import name, system
from time import sleep
from webbrowser import open

class Instagram(object):
    def __init__(self):
        self.blue = Fore.BLUE
        self.red = Fore.RED
        self.white = Fore.WHITE
        self.yellow = Fore.YELLOW
        self.magenta = Fore.MAGENTA
        self.cyan = Fore.CYAN
        self.green = Fore.GREEN
        self.res = Style.RESET_ALL
        try:
            self.username = sys.argv[1]
            self.getUser(self.username)
        except IndexError:
            self.clear()
            print(f"{self.cyan}===================\n{self.yellow}[{self.red}+{self.yellow}]{self.yellow}{self.blue}python {self.green}{sys.argv[0]} {self.blue}username{self.res}")


    def clear(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")


    def logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = r"""

             ___           _        ____                  ___        __
            |_ _|_ __  ___| |_ __ _|  _ \ __ _  __ _  ___|_ _|_ __  / _| ___
             | || '_ \/ __| __/ _` | |_) / _` |/ _` |/ _ \| || '_ \| |_ / _ \
             | || | | \__ \ || (_| |  __/ (_| | (_| |  __/| || | | |  _| (_) |
            |___|_| |_|___/\__\__,_|_|   \__,_|\__, |\___|___|_| |_|_|  \___/
                                               |___/
                                                    Instagram Page info v2.0
                iran-cyber.net | Wrote by iwHH
                iraniancoders.ir | github.com/iwhh
        """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" %(choice(colors), line, clear))
            sleep(0.05)
    def getUser(self, user):
        self.clear()
        self.logo()
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        self.request = get(f"http://Api.pwrteam.ir/InstaInFo.php?user={user}", headers=headers, timeout=5)
        self.request.encoding = "utf-8"
        self.getInformation(self.request.text)


    def getInformation(self, data):
        try:
            loader = loads(data)
            bio = loader["biography"]
            followers = loader["edge_followed_by"]["count"]
            followings = loader["edge_follow"]["count"]
            name = loader["full_name"]
            id = loader["id"]
            profile_photo = loader["profile_pic_url_hd"]
            post_counter = loader["edge_owner_to_timeline_media"]["count"]
            profile_url = loader["external_url"]
            private = loader["is_private"]
        except TypeError:
            print(f"{self.red}Invalid Username{self.res}")
            sys.exit(1)
        print(f"""
name : {name}
biography : {bio}
followers : {followers}
followings : {followings}
id : {id}
photo Url : {profile_photo}
profile Url : {profile_url}
post counts : {post_counter}
is private ? : {private}""")
        open_it = input("===============\nOpen This page : ? [y/n]")
        if open_it == "y":
            open(f"https://instagram.com/{self.username}")
            print(self.res)
            sys.exit()
        else:
            print(self.res)
if __name__ == "__main__":
    run = Instagram()
