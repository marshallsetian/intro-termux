import os,sys,time,os,json,requests,json
from colorama import Fore,Back,init
from requests import get,post
from urllib import request

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

ip=requests.get('https://api.ipify.org').text
visitor=request.urlopen('https://api.countapi.xyz/hit/brutal-spam-wa')
getvisit=json.loads(visitor.read())
localtime=time.asctime(time.localtime(time.time()))

hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

os.system("clear")
autoketik(f"{biru}[{kuning}Warning{biru}] {W}FOLLOW INSTAGRAM KU COEG @Marshall Setian")
time.sleep(3)
os.system("xdg-open https://www.facebook.com/yoelmars1509")
autoketik(f"{biru}[{kuning}Warning{biru}] {W}Thx yang udah FOLLOW YAH.., semoga work")
time.sleep(3)
os.system("clear")
autoketik(f"""

{putih}[{biru}•{putih}] {biru}Author {putih}   : MarshallSetian
{putih}[{biru}•{putih}] {abu}GitHub {putih}   : papaENG
{putih}[{biru}•{putih}] {merah}You{putih}Tube {putih}  : marshall setian
{putih}[{biru}•{putih}] {ungu}Instagram {putih}: @marshall_setian
{W}[{Y}•{W}] Ip Kamu {putih}  :{Y} {ip}
{W}[{Y}•{W}] Waktu/Jam {putih}:{Y} {localtime}
{W}[{Y}•{W}] Total Run {putih}:{Y} {getvisit['value']}
""")
