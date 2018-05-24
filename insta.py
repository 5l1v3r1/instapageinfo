# -*- coding: utf-8 -*-
import os,json,random,sys,options,unicodedata,urllib
import time
try:
    import requests
except ImportError:
    l = 'sudo apt install python-requests'
    w = 'pip install requests'
    print " requests Module is not installed yet !\nInstalling ...\nwhen installed start again this script"
    time.sleep(1.5)
    os.system([l,w][os.name == 'nt'])
    sys.exit()
try:
    from colorama import Fore, Style
    r = Fore.RED
    b = Fore.BLUE
    g = Fore.GREEN
    w = Fore.WHITE
    m = Fore.MAGENTA
    y = Fore.YELLOW
    res = Style.RESET_ALL
except ImportError:
    l = 'sudo apt install python-colorama'
    w = 'pip install colorama'
    print " Colorama Module is not installed yet !\nInstalling ...\nwhen installed start again this script"
    time.sleep(1.5)
    os.system([l,w][os.name == 'nt'])
    sys.exit()
class InstaPageInfo:
    def __init__(self):
        self.run() 
    def run(self):
        try:
            username = sys.argv[1]
        except:
            options.clear()
            options.print_logo()
            print y + "[" + r + "-" + y + "] " + g + "python insta.py username\n" + y + "[" + r + "!" + y + "] " + w + "Example ~> " + g + "python insta.py ircoders"
            sys.exit()
        options.clear()
        options.print_logo()
        try:
            req = requests.get("http://api.reloadlife.me/v1/1/instagram/userinfo?user=" + str(username), timeout=5)
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            print y + "[" + r + "-" + y + "] " + g + "Check Your Internet Connection ..."
            sys.exit()
        js = json.loads(req.text)
        print Fore.CYAN + "---------------------------------"
        get_user = js['Result']['Username']
        
        print y + "[" + r + "+" + y + "] " + g + "Username : " + b + unicodedata.normalize('NFKD', get_user).encode('ascii','ignore')
        get_name = js['Result']['DisplayName']
        time.sleep(2.5)
        if get_name:
            print y + "[" + r + "+" + y + "] " + g + "Name : " + b + unicodedata.normalize('NFKD', get_name).encode('ascii', 'ignore') 
        else:
            print y + "[" + r + "+" + y + "] " + g + "Name : " + b + "None"
        get_id = js['Result']['Id']
        time.sleep(2.5)
        if get_id:
            print y + "[" + r + "+" + y + "] " + g + "Id : " + b + unicodedata.normalize('NFKD', get_id).encode('ascii','ignore')
        else:
            print y + "[" + r + "+" + y + "] " + g + "Id : " + b + "None"
        get_bio = js['Result']['Biography']
        time.sleep(2.5)
        if get_bio:
            print y + "[" + r + "+" + y + "] " + g + "Biography : " + b + unicodedata.normalize('NFKD', get_bio).encode('ascii', 'ignore')
        else:
            print y + "[" + r + "+" + y + "] " + g + "Biography : " + b + "None"
        get_url = js['Result']['ProfileUrl']
        time.sleep(2.5)
        if get_url:
            print y + "[" + r + "+" + y + "] " + g + "ProfileUrl : " + b + unicodedata.normalize('NFKD', str(get_url)).encode('ascii', 'ignore')
        else:
            print y + "[" + r + "-" + y + "] " + g + "ProfileUrl : " + b + "None"
        get_profile = js['Result']['ProfilePhoto']
        time.sleep(2.5)
        print y + "[" + r + "+" + y + "] " + g + "Now im going too Download the profile photo ..."
        time.sleep(2)
        print y + "[" + r + "+" + y + "] " + g + "Downloading . . ."
        urllib.urlretrieve(get_profile, "Profile.jpg")
        time.sleep(2.5)
        print y + "[" + r + "+" + y + "] " + g + "Downloaded ~> Profile.jpg"
        get_priv8 = js['Result']['PrivatePage']
        if get_priv8:
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Is private page ? : " + b + "Yes"
            profile_count = js['Result']['Posts']['count']
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Post Counts : " + b + unicode(str(profile_count))
            get_F = js['Result']['Followers']
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Followers : " + b + unicode(str(get_F))
            get_Fo = js['Result']['Following']
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Followings : " + b + unicode(str(get_Fo))
        else:
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Is private page ? : " + b + "No"
            profile_count = js['Result']['Posts']['count']
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Post Counts : " + b + unicode(str(profile_count))
            get_P = js['Result']['Posts']['Urls']
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Posts : "
            for post in get_P:
                time.sleep(2.5)
                print r + "[ " + Fore.LIGHTMAGENTA_EX + post + r + " ]"
            get_F = js['Result']['Followers']
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Followers : " + b + unicode(str(get_F))
            get_Fo = js['Result']['Following']
            time.sleep(2.5)
            print y + "[" + r + "+" + y + "] " + g + "Followings : " + b + unicode(str(get_Fo))
            print res


try:
    insta = InstaPageInfo()
except KeyboardInterrupt:
    print y + "[" + r + "<3" + y + "] " + g + "Nice To meet You <3\nGoodbye"
    sys.exit()
