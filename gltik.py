import requests, os, time, sys
from time import sleep
from prettytable import PrettyTable  # Thêm thư viện prettytable
from pystyle import Colors, Colorate
import random
# Màu sắc
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
vt="\033[1;38;5;226m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
n = "\033[1;3m\033[1;38m"
e = "\033[0m"
cy= "\033[1;38;5;51m"
hd="\033[1;38;5;213m"
cam="\033[1;38;5;202m"
ce="\033[1;38;5;195m"
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
# Kiểm tra hoặc tạo file lưu Authorization và token
author = input("Nhập Authorization: ")
token = input("Nhập T: ")
with open("Authorization.txt", "w") as auth_file:
	auth_file.write(author)
	with open("token.txt", "w") as token_file:
		token_file.write(token)
readfile = open('Authorization.txt','r')
file = readfile.read()
ses = requests.Session()
User_Agent=random.choice([
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N910V Build/LRX22C) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/54.0.1548.302 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/53.0.2480.357 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 7 Build/NME91E) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/55.0.1165.180 Mobile Safari/535.4",
"android|Mozilla/5.0 (Android; Android 4.4.4; IQ4502 Quad Build/KOT49H) AppleWebKit/603.22 (KHTML, like Gecko) Chrome/55.0.3246.371 Mobile Safari/535.0",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G925FQ Build/KOT49H) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/49.0.2349.273 Mobile Safari/533.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935S Build/LMY47X) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/51.0.1541.177 Mobile Safari/603.6",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 6 Build/NME91E) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/52.0.3581.331 Mobile Safari/602.0",
"android|Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NME91E) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/47.0.2862.396 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; Android 5.0.1; LG-D725 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko) Chrome/54.0.3919.385 Mobile Safari/601.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/600.8 (KHTML, like Gecko) Chrome/47.0.1683.316 Mobile Safari/534.4",
"android|Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925M Build/LRX22G) AppleWebKit/533.12 (KHTML, like Gecko) Chrome/48.0.3195.222 Mobile Safari/534.1",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; MOTOROLA XT1021 Build/LXB22) AppleWebKit/602.21 (KHTML, like Gecko) Chrome/51.0.3324.323 Mobile Safari/536.2",
"android|Mozilla/5.0 (Linux; Android 4.4; LG-D350 Build/KOT49I) AppleWebKit/601.4 (KHTML, like Gecko) Chrome/50.0.1490.201 Mobile Safari/602.6",
"android|Mozilla/5.0 (Linux; Android 7.0; Xperia Build/NDE63X) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/48.0.3885.393 Mobile Safari/602.7",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 9X Build/NPD90G) AppleWebKit/536.38 (KHTML, like Gecko) Chrome/52.0.2441.242 Mobile Safari/601.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9600 Build/KTU84P) AppleWebKit/602.14 (KHTML, like Gecko) Chrome/53.0.2318.108 Mobile Safari/534.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTO XT1570 MOTO X STYLE Build/LMY47Z) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/55.0.1855.292 Mobile Safari/602.5",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/50.0.1695.312 Mobile Safari/535.3",
"android|Mozilla/5.0 (Android; Android 4.4; MOTOROLA MOTOG Build/KVT49L) AppleWebKit/533.8 (KHTML, like Gecko) Chrome/55.0.3923.147 Mobile Safari/600.9",
"android|Mozilla/5.0 (Linux; U; Android 6.0; HTC One801e dual sim Build/MRA58K) AppleWebKit/536.39 (KHTML, like Gecko) Chrome/47.0.3811.339 Mobile Safari/601.7",
"android|Mozilla/5.0 (Linux; Android 6.0.1; HTC OneS Build/MRA58K) AppleWebKit/600.47 (KHTML, like Gecko) Chrome/51.0.1432.312 Mobile Safari/535.4",])
headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent':User_Agent,
            "Authorization" : file,
            'Content-Type':'application/json;charset=utf-8'            
}

url1 = 'https://gateway.golike.net/api/users/me'
checkurl1 = ses.get(url1,headers=headers).json()
username = checkurl1['data']['username']
coin = checkurl1['data']['coin']
user_id = checkurl1['data']['id']
#pending_coin = checkurl1["data"]["pending_coin"]
try:
    open("Authorization.txt", "x").close()
    open("token.txt", "x").close()
except:
    pass
# Lựa chọn nhập Authorization
print(f"{luc}1.{trang} Sử dụng Authorization đã lưu")
print(f"{luc}2.{trang} Nhập Authorization mới")
choice = input(f"{trang}Nhập lựa chọn {trang}({luc}1{trang}/{luc}2{trang}): {e}")
if choice == "1":
    try:
        with open("Authorization.txt", "r") as auth_file:
            author = auth_file.read().strip()
        with open("token.txt", "r") as token_file:
            token = token_file.read().strip()
    except:
        print(f"{red}Không tìm thấy Authorization hoặc Token đã lưu. Vui lòng nhập mới.{e}")
        choice = "2"

if choice == "2":
    author = input("Nhập Authorization: ")
    token = input("Nhập T: ")
    with open("Authorization.txt", "w") as auth_file:
        auth_file.write(author)
    with open("token.txt", "w") as token_file:
        token_file.write(token)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}

def chonacc():
    response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers).json()
    return response

def nhannv(account_id):
    params = {'account_id': account_id, 'data': 'null'}
    response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs', params=params, headers=headers).json()
    return response

def hoanthanh(ads_id, account_id):
    json_data = {
        'ads_id': ads_id,
        'account_id': account_id,
        'async': True,
        'data': None,
    }
    response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, json=json_data).json()
    return response

def baoloi(ads_id, object_id, account_id, loai):
    json_data1 = {
        'description': 'Tôi đã làm Job này rồi',
        'users_advertising_id': ads_id,
        'type': 'ads',
        'provider': 'tiktok',
        'fb_id': account_id,
        'error_type': 6,
    }
    requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)

    json_data = {
        'ads_id': ads_id,
        'object_id': object_id,
        'account_id': account_id,
        'type': loai,
    }
    requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', headers=headers, json=json_data)

loat = int(input(f"{trang}Nhập delay (giây): "))
thay = int(input(f"{trang}Nhập số lần lỗi để đổi tài khoản: "))
# Lấy danh sách tài khoản TikTok
chontktiktok = chonacc()

def dsacc():
    if chontktiktok["status"] != 200:
        print(f"{red}Authorization hoặc Token không hợp lệ!{e}")
        quit()
    # Hiển thị danh sách tài khoản bằng PrettyTable
    tabl = PrettyTable()
    tabl.title = f"Thông Tin ACC GOLIKE"
    tabl.field_names = [f"{hd} Golile {e}", f"{vt}Hiện Tại{e}",f"Chx Duyêt"]
    tabl.add_row([f"{username}", luc+str(coin)+e,"Chx Code"])
    table = PrettyTable()
    table.title = f"{cy}Danh Sách ACC TIK TOK{e}"
    table.field_names = [f"{ce}STT{e}", f"{hd}Tên Tài Khoản{e}",f"ID" ,f"{vt}Trạng Thái{e}"]
    for i, acc in enumerate(chontktiktok["data"], start=1):
        table.add_row(["\033[1;38;5;202m"+str(i)+"\033[0m", "\x1b[1;36m"+(acc["nickname"])+"\033[0m",(acc["id"]), f"{luc}Hoạt Động {e}"])
        os.system("clear")
    print(tabl)
    print(table)
dsacc()
# Người dùng chọn tài khoản TikTok
while True:
    try:
        luachon = int(input(f"{vang}Chọn tài khoản để chạy: {e}"))
        while luachon > len(chontktiktok["data"]):
            luachon = int(input("Tài khoản không tồn tại. Hãy nhập lại: "))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        break
    except:
        print(f"{red}Sai định dạng !{e}")
        sleep(1)
# Nhập thông số delay và số lần đổi tài khoản
while True:
    try:
        delay = loat
        break
    except:
        print(f"{red}Sai định dạng !{e}")
        sleep(1)
while True:
    try:
        doiacc = thay
        break
    except:
        print("Nhập một số hợp lệ!")
        sleep(1)
# Các biến khởi tạo
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
print("STT        Tiền       Tổng")
# Chạy nhiệm vụ
while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
        print(f"Các tài khoản gặp lỗi: {dsaccloi}")
        dsacc()
        while True:
            try:
                luachon = int(input("Chọn tài khoản để chạy: "))
                while luachon > len(chontktiktok["data"]):
                    luachon = int(input("Tài khoản không tồn tại. Hãy nhập lại: "))
                account_id = chontktiktok["data"][luachon - 1]["id"]
                checkdoiacc = 0
                break
            except:
                print("Sai định dạng!")
                sleep(1)
    nhanjob = nhannv(account_id)
    if nhanjob["status"] == 200:
        ads_id = nhanjob["data"]["id"]
        link = nhanjob["data"]["link"]
        object_id = nhanjob["data"]["object_id"]

        if nhanjob["data"]["type"] != "follow":
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            continue
        os.system(f"termux-open-url {link}")
        for i in range(delay, -1, -1):
            print(Colorate.Diagonal(Colors.red_to_yellow, f"Vui Lòng Chờ [{i}].."), end="\r")
            sleep(1)

        nhantien = hoanthanh(ads_id, account_id)
        if nhantien["status"] == 200:
            dem += 1
            tien = nhantien["data"]["prices"]
            tong += tien
            print(f"                   ", end="\r")
            print (Colorate.Diagonal(Colors.cyan_to_green, f" {dem}         +{tien}         {tong}"))
            checkdoiacc = 0
        else:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            checkdoiacc += 1


    # Menu after encountering an error
    if checkdoiacc >= doiacc:
        print(f"{red}Tài khoản {chontktiktok['data'][luachon - 1]['nickname']} đã gặp quá nhiều lỗi!{e}")
        while True:
            print(f"{trang}Nhập {luc}1 {trang}Để Chạy Lại Acc")
            print(f"{trang}Nhập {luc}2 {trang}Để Thay Acc")
            print(f"{trang}Nhập {luc}3 {trang}Để thoát Tool")
            choice = input(f"{trang}Lựa Chọn : {luc}")
            if choice == '1':
                print(f"{trang}Tiếp tục với tài khoản này...")
                checkdoiacc = 0  # Reset error count for this account
                break
            elif choice == '2':
                dsacc()  # List available accounts again
                while True:
                    try:
                        luachon = int(input(f"{vang}Chọn tài khoản để chạy: {e}"))
                        while luachon > len(chontktiktok["data"]):
                            luachon = int(input("Tài khoản không tồn tại. Hãy nhập lại: "))
                        account_id = chontktiktok["data"][luachon - 1]["id"]
                        checkdoiacc = 0  # Reset error count for new account
                        break
                    except:
                        print("Sai định dạng!")
                        sleep(1)
                break
            elif choice == '3':
                print("Thoát tool...")
                quit()  # Exit the script
            else:
                print(f"{red}Lựa chọn không hợp lệ! Hãy nhập lại.{e}")
