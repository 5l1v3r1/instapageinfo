import time,os,random,sys

def clear():
    l = 'clear'
    w = 'cls'
    os.system([l,w][os.name == 'nt'])
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

         ___           _        ____                  ___        __       
        |_ _|_ __  ___| |_ __ _|  _ \ __ _  __ _  ___|_ _|_ __  / _| ___  
         | || '_ \/ __| __/ _` | |_) / _` |/ _` |/ _ \| || '_ \| |_ / _ \ 
         | || | | \__ \ || (_| |  __/ (_| | (_| |  __/| || | | |  _| (_) |
        |___|_| |_|___/\__\__,_|_|   \__,_|\__, |\___|___|_| |_|_|  \___/ 
                                           |___/                          
                                                Instagram Page info v1.0
            
            iraniancoders.ir - iran-cyber.net | github.com/iwhh
    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" %(random.choice(colors), line, clear))
        time.sleep(0.05)
