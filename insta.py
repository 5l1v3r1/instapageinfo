# -*- coding: utf-8 -*-
import os,time,requests,json,random,sys,options,unicodedata,urllib
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
        pass 
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
        print y + "[" + r + "+" + y + "] " + g + "Name : " + b + unicodedata.normalize('NFKD', get_name).encode('ascii', 'ignore') 
        get_id = js['Result']['Id']
        print y + "[" + r + "+" + y + "] " + g + "Id : " + b + unicodedata.normalize('NFKD', get_id).encode('ascii','ignore')
        get_bio = js['Result']['Biography']
        print y + "[" + r + "+" + y + "] " + g + "Biography : " + b + unicodedata.normalize('NFKD', get_bio).encode('ascii', 'ignore')
        get_url = js['Result']['ProfileUrl']
        print y + "[" + r + "+" + y + "] " + g + "ProfileUrl : " + b + unicodedata.normalize('NFKD', get_url).encode('ascii', 'ignore')
        get_profile = js['Result']['ProfilePhoto']
        print y + "[" + r + "+" + y + "] " + g + "Now im going too Download the profile photo ..."
        time.sleep(2)
        print y + "[" + r + "+" + y + "] " + g + "Downloading . . ."
        urllib.urlretrieve(get_profile, "Profile.jpg")
        time.sleep(1)
        print y + "[" + r + "+" + y + "] " + g + "Downloaded ~> Profile.jpg"
        get_priv8 = js['Result']['PrivatePage']
        if get_priv8:
            print y + "[" + r + "+" + y + "] " + g + "Is private page ? : " + b + "Yes"
            profile_count = js['Result']['Posts']['count']
            print y + "[" + r + "+" + y + "] " + g + "Post Counts : " + b + unicode(str(profile_count))
            get_F = js['Result']['Followers']
            print y + "[" + r + "+" + y + "] " + g + "Followers : " + b + unicode(str(get_F))
            get_Fo = js['Result']['Following']
            print y + "[" + r + "+" + y + "] " + g + "Followings : " + b + unicode(str(get_Fo))
        else:
            print y + "[" + r + "+" + y + "] " + g + "Is private page ? : " + b + "No"
            profile_count = js['Result']['Posts']['count']
            print y + "[" + r + "+" + y + "] " + g + "Post Counts : " + b + unicode(str(profile_count))
            get_P = js['Result']['Posts']['Urls']
            print y + "[" + r + "+" + y + "] " + g + "Posts : "
            for post in get_P:
                print r + "[ " + Fore.LIGHTMAGENTA_EX + post + r + " ]"
            get_F = js['Result']['Followers']
            print y + "[" + r + "+" + y + "] " + g + "Followers : " + b + unicode(str(get_F))
            get_Fo = js['Result']['Following']
            print y + "[" + r + "+" + y + "] " + g + "Followings : " + b + unicode(str(get_Fo))
            print res




insta = InstaPageInfo()
try:
    insta.run()
except KeyboardInterrupt:
    print "\nNice To meet You <3\nGoodbye"
    sys.exit()