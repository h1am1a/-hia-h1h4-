from urllib import response
import string
import random
import requests
import time
import os
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import socket
import psutil
import signal
from pystyle import *       
from packaging import version
import time 
import os, sys
from pystyle import Write,Colors
import subprocess
from argparse import ArgumentParser
from colorama import Fore
from colorama import Style
from pystyle import Write,Colors
import subprocess

def get_ip():
    try:
        ip = socket.gethostbyname(requests.get("http://kiemtraip.com/raw.php").text.strip())
    except requests.exceptions.ConnectionError:
        print(f"{chars} \033[1;36;40m Lỗi Mạng !!!\033[1;37;40m")
        sys.exit()
    if ip in ['0.0.0.0']:
        print(f"{chars} \033[1;36;40mBật Mạng Lên Em Iu \033[1;31;40m<3\033[1;37;40m")
        sys.exit()
    return ip

ip = get_ip()    
times = str(time.strftime("%H:%M:%S"))    
ngay = str(time.strftime("%d"))
thang = str(time.strftime("%m"))
nam = str(time.strftime("%Y"))
os.system("cls" if os.name == "nt" else "clear")
def banner():
    banner = f"""
██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

TOOL BY: DUY KHÁNH             PHIÊN BẢN : 1.0
════════════════════════════════════════════════  
[</>] BOX ZALO : https://zalo.me/g/nguadz335
[</>] KÊNH YOUTUBE : REVIEWTOOL247NDK
[</>] ADMIN TOOL : DUYKHANH
❤ CHÀO MỪNG BẠN ĐÃ ĐẾN VỚI TOOL ❤
════════════════════════════════════════════════  
[</>] GIỚI HẠN THIẾT BỊ : 1 🚦
[</>] NGƯỜI MUA : USER.....
[</>] KEY : NDK*********
[</>] Date Time ( {times} - {ngay}/{thang}/{nam} )
[</>] Ip ( {ip} )
════════════════════════════════════════════════  
                  [THÔNG BÁO]
>>>>TOOL ĐANG TRONG QUÁ TRÌNH PHÁT TRIỂN THÊM<<<<     
════════════════════════════════════════════════                                
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
os.system("cls" if os.name == "nt" else "clear")
banner()
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
endpoint = 'https://dropmail.me/api/graphql/'
token = ''

def start(interval):
    request = queried_request(session_query())
    if not request.ok:
        raise Exception('Không thể hoàn thành yêu cầu: #' + str(request.status_code))
    response = request.json()
    session = response['data']['introduceSession']
    session_id = session['id']
    email = session['addresses'][0]['address']
    success('Địa chỉ email của bạn: ' + email)
    success('Đang làm mới hộp thư...')
    while True:
        mailbox = queried_request(mailbox_query(session_id)).json()
        mails = mailbox['data']['session']['mails']
        if mails:
            success('Đã nhận mail:')
            print('-----------------------\n')
            print(mails[0]['text'])
            return
        else:
            time.sleep(interval)

def session_query():
    return 'mutation {introduceSession {id, addresses{address}}}'

def mailbox_query(id):
    return 'query ($id: ID!){session(id:$id) {mails{downloadUrl, text}}}&variables={"id":"' + id + '"}'

def get_token(chars):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=chars))

def queried_request(body):
    query = '?query=' + body
    return requests.get(endpoint + token + query)

def success(str, as_input=False):
    output = f'[</>] {str}'
    if as_input:
        input(output)
    else:
        print(output)

def error(str, e='', as_input=False):
    output = f'[ERROR] {str}: {e}'
    if as_input:
        input(output)
    else:
        print(output)

parser = ArgumentParser()
parser.add_argument('-i', '--interval', metavar='interval', type=int, nargs=1, help='Khoảng thời gian làm mới (s)')
args = parser.parse_args()

if __name__ == '__main__':
    print(token)
    try:
        token = get_token(8)
        interval = 3
        if args.interval:
            interval = args.interval[0]
        start(interval)
    except Exception as e:
        error('LỖI TÙM LUM', e, True)