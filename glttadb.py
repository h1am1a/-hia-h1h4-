import os
import sys
import base64
import requests
import json
import time
import uuid
import datetime
import subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from time import sleep
from pystyle import Colorate, Colors
from colorama import Fore, Style
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)        
    except (requests.exceptions.ReadTimeout, requests.ConnectionError):
        print("Vui lòng kiểm tra kết nối mạng !!!")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")    
def check_adb_connection():
    try:
        result = subprocess.check_output(["adb", "devices"], stderr=subprocess.STDOUT, universal_newlines=True)
        devices = [line.split("\t")[0] for line in result.splitlines() if "\tdevice" in line]
        if len(devices) > 0:
            print("Thiết bị đã được kết nối qua ADB.")
            return True, devices[0]
        else:
            print("Không có thiết bị nào được kết nối qua ADB.")
            return False, None
    except subprocess.CalledProcessError:
        print("Không thể chạy lệnh ADB. Vui lòng kiểm tra lại và cài đặt ADB.")
        return False, None
def save_device_info(device_id):
    with open("ADB.txt", "w") as file:
        file.write(device_id)
    print("[<∆>] Đã lưu thông tin thiết bị.")
def load_device_info():
    if os.path.exists("ADB.txt"):
        with open("ADB.txt", "r") as file:
            device_id = file.read().strip()
            print('══════════════════════════════════════════════════════════════')
            print(f"Đã tải thông tin kết nối từ thiết bị.")
            return device_id
    else:
        print("Không tìm thấy file thông tin thiết bị.")
        return None
def save_coordinates(follow_x, follow_y, like_x, like_y):
    with open("coordinates_tiktok.txt", "w") as file:
        file.write(f"follow_x={follow_x}\n")
        file.write(f"follow_y={follow_y}\n")
        file.write(f"like_x={like_x}\n")
        file.write(f"like_y={like_y}\n")
    print("[<∆>] Đã lưu tọa độ vào thiết bị.")
def load_coordinates():
    if os.path.exists("coordinates_tiktok.txt"):
        coordinates = {}
        with open("coordinates_tiktok.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                coordinates[key] = int(value)
        print("Đã tải tọa độ từ thiết bị.")
        return coordinates
    else:
        print('══════════════════════════════════════════════════════════════')
        print("Không tìm thấy file tọa độ.")
        return None
def connect_android_11():
    while True:
        try:
            ip = input("Nhập IP Thiết Bị: ").strip()
            debug_port = input("Nhập Cổng Thiết Bị: ").strip()
            pair_port = input("Nhập Cổng Mã Ghép Nối: ").strip()
            wifi_code = input("Nhập Mã Ghép Nối Wi-Fi: ").strip()
            check_connection()
            os.system(f"adb pair {ip}:{pair_port} {wifi_code}")
            os.system(f"adb connect {ip}:{debug_port}")
            is_connected, device_id = check_adb_connection()
            if is_connected:
                save_device_info(device_id)
                print("Thiết bị đã kết nối thành công qua ADB!")
                return True
            else:
                print("Không thể kết nối thiết bị. Vui lòng kiểm tra lại thông tin.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
def connect_android_10():
    while True:
        try:
            ip = input("Nhập IP Thiết Bị: ").strip()
            debug_port = input("Nhập Cổng Thiết Bị: ").strip()
            check_connection()
            os.system(f"adb connect {ip}:{debug_port}")
            is_connected, device_id = check_adb_connection()
            if is_connected:
                save_device_info(device_id)
                print("Thiết bị đã kết nối thành công qua ADB!")
                return True
            else:
                print("Không thể kết nối thiết bị. Vui lòng kiểm tra lại thông tin.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
def tap_screen(x, y):
    os.system(f"adb shell input tap {int(x)} {int(y)}")
def banner():
 os.system("cls" if os.name == "nt" else "clear")
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

banner()    
try:
    Authorization = open("user_tiktok.txt", "x")
    t = open("t_tiktok.txt", "x")
    Authorization.close()
    t.close()
except FileExistsError:
    pass
if os.path.exists("user_tiktok.txt") and os.path.exists("t_tiktok.txt"):
    with open("user_tiktok.txt", "r") as Authorization:
        author = Authorization.read().strip()
    with open("t_tiktok.txt", "r") as t:
        token = t.read().strip()
else:
    author = ""
    token = ""
while author == "" or token == "":
    author = input("[</>] ➩ Authorization Golike: ").strip()
    check_connection()
    token = input("[</>] ➩ T Golike: ").strip()
    check_connection()
    with open("user_tiktok.txt", "w") as Authorization:
        Authorization.write(author)
    with open("t_tiktok.txt", "w") as t:
        t.write(token)
        
print('Đăng Nhập Thành Công!')
time.sleep(3)        
banner()
print("[</>] ➩ Nhập Số | 1 | Để Vào Tool TikTok")
print('[</>] ➩ Nhập Số | 2 | Để Xóa Authorization Hiện Tại')
print('══════════════════════════════════════════════════════════════')
while True:
    try:
        choose = int(input('[</>] ➩ Nhập Số: '))
        check_connection()
        if choose not in [1, 2]:
            print("Vui lòng nhập lại!")
            continue
        break
    except ValueError:
        print("Vui lòng nhập lại!")
if choose == 2:
    if os.path.exists("user_tiktok.txt"):
        os.remove("user_tiktok.txt")
        print("[<∆>] Đã xóa user_tiktok.txt")
    if os.path.exists("t_tiktok.txt"):
        os.remove("t_tiktok.txt")
        print("[<∆>] Đã xóa t_tiktok.txt!")
        exit()
    
    
if choose == 1:    
    time.sleep(0000.1)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}
def chonacc():
    json_data = {}
    response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
    return response
def nhannv(account_id):
    params = {
        'account_id': account_id,
        'data': 'null',
    }
    json_data = {}
    response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs', params=params, headers=headers, json=json_data).json()
    return response
def hoanthanh(ads_id, account_id):
    json_data = {
        'ads_id': ads_id,
        'account_id': account_id,
        'async': True,
        'data': None,
    }
    response = requests.post(
        'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
        headers=headers,
        json=json_data,
    ).json()
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
    response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()
    json_data = {
        'ads_id': ads_id,
        'object_id': object_id,
        'account_id': account_id,
        'type': loai,
    }
    response = requests.post(
        'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
        headers=headers,
        json=json_data,
    ).json()
chontktiktok = chonacc()
def dsacc():
    while True:
        try:
            if chontktiktok["status"] != 200:
                print("Vui lòng nhập lại!")
                quit()
            banner()
            for i in range(len(chontktiktok["data"])):
                print(f'[</>] ➩ STT | {i + 1} | => Id: {chontktiktok["data"][i]["unique_username"]}')
            print('══════════════════════════════════════════════════════════════')
            break
        except:
            print(f"{chontktiktok}")
            sleep(10)
dsacc()
d = 0
while True:
    idacc = str(input('[</>] ➩ Nhập Id: '))
    check_connection()
    banner()
    for i in range(len(chontktiktok["data"])):
        if chontktiktok["data"][i]["unique_username"] == idacc:
            d = 1
            account_id = chontktiktok["data"][i]["id"]
            break
    if d == 0:
        print("Acc này chưa được thêm vào golike hoặc id sai!")
        continue
    break
while True:
    try:
        delay = int(input(f'[</>] ➩ Nhập Delay: '))
        break
    except:
        print("Vui lòng nhập lại!")
while True:
    try:
        lannhan = input(f'[</>] ➩ Nhận tiền lần 2 nếu lần 1 lỗi? (y/n): ')
        if lannhan != "y" and lannhan != "n":
            print("Vui lòng nhập lại!")
            continue
        break
    except:
        pass
while True:
    try:
        doiacc = int(input(f'[</>] ➩ Số job lỗi sẽ đổi acc khác: '))
        break
    except:
        print("Vui lòng nhập lại!")        
check_connection()
banner()
while True:
    try:
        auto_follow = input("Bạn có muốn sử dụng ADB không? (y/n): ").strip().lower()
        if auto_follow not in ["y", "n"]:
            print("Vui lòng nhập lại!")
            continue        
        if auto_follow == "y":
            device_id = load_device_info()
            if not device_id:
                print("Thiết bị chưa được kết nối ADB. Vui lòng thêm thiết bị.")
                while True:
                    try:
                        print('══════════════════════════════════════════════════════════════')
                        print("[</>] ➩ Nhập Số | 1 | Để Thêm Thiết Bị Android 10 ")
                        print("[</>] ➩ Nhập Số | 2 | Để Thêm Thiết Bị Android 11 ")
                        print('══════════════════════════════════════════════════════════════')
                        choose_reviewtool = input('[</>] ➩ Nhập Số: ')
                        check_connection()
                        print('══════════════════════════════════════════════════════════════')
                        if choose_reviewtool not in ["1", "2"]:
                            print("Vui lòng nhập lại!")
                            continue
                        if choose_reviewtool == "1":
                            if connect_android_10():
                                break
                        else:
                            if connect_android_11():
                                break
                    except Exception as e:
                        print(f"Đã xảy ra lỗi: {e}")
            coordinates = load_coordinates()
            if not coordinates:
                while True:
                    try:
                        print('══════════════════════════════════════════════════════════════')
                        follow_x = int(input("Nhập Tọa Độ x Nút Follow TikTok: "))
                        follow_y = int(input("Nhập Tọa Độ y Nút Follow TikTok: "))
                        like_x = int(input("Nhập Tọa Độ y Nút Like TikTok: "))
                        like_y = int(input("Nhập Tọa Độ y Nút Like TikTok: "))
                        check_connection()
                        print('══════════════════════════════════════════════════════════════')
                        save_coordinates(follow_x, follow_y, like_x, like_y,)
                        break
                    except ValueError:
                        print("Vui lòng nhập lại!")
            else:
                while True:
                    print('══════════════════════════════════════════════════════════════')
                    choose = input("Bạn có muốn sử dụng tọa độ đã lưu? (y/n): ").strip().lower()
                    check_connection()
                    if choose not in ["y", "n"]:
                        print("Vui lòng nhập lại!")
                        continue                    
                    if choose == "y":
                        follow_x = coordinates["follow_x"]
                        follow_y = coordinates["follow_y"]
                        like_x = coordinates["like_x"]
                        like_y = coordinates["like_y"]
                        print(f"Sử dụng tọa độ đã lưu: Follow ({follow_x}, {follow_y}), Like ({like_x}, {like_y})")
                        break
                    else:
                        if os.path.exists("coordinates_tiktok.txt"):
                            os.remove("coordinates_tiktok.txt")
                            print("[<∆>] Đã xóa tọa độ đã lưu.")                       
                        while True:
                            try:
                                print('══════════════════════════════════════════════════════════════')
                                follow_x = int(input("Nhập Tọa Độ x Nút Follow TikTok: "))
                                follow_y = int(input("Nhập Tọa Độ y Nút Follow TikTok: "))
                                like_x = int(input("Nhập Tọa Độ y Nút Like TikTok: "))
                                like_y = int(input("Nhập Tọa Độ y Nút Like TikTok: "))
                                check_connection()
                                print('══════════════════════════════════════════════════════════════')
                                save_coordinates(follow_x, follow_y, like_x, like_y,)
                                break
                            except ValueError:
                                print("Vui lòng nhập lại!")
                        break
        else:
            print("Bỏ qua kết nối ADB.")
        break

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
banner()                
while True:
    try:
        print("[</>] ➩ Nhập Số | 1 | Nhiệm Vụ Follow")
        print("[</>] ➩ Nhập Số | 2 | Nhiệm Vụ Like")
        print("[</>] ➩ Nhập chữ | all | Nhiệm Vụ Follow + Like")
        print('══════════════════════════════════════════════════════════════')
        chedo = int(input('[</>] ➩ Nhập Số: '))
        check_connection()
        if chedo in [1, 2, all]:
            break
        else:
            print("Vui lòng nhập lại!")
    except:
        print("Vui lòng nhập lại!")
lam = []
if chedo == 1:
    lam = ["follow"]
elif chedo == 2:
    lam = ["like"]
elif chedo == all:
    lam = ["follow", "like"]
dem = 0
tong = 0
checkdoiacc = 0
checkdoiacc1 = 0
dsaccloi = []
accloi = ""
banner()
while True:
    if checkdoiacc == doiacc:
        dsacc()
        idacc = str(input(f'[</>] ➩ Job lỗi đạt giới hạn! Nhập id acc mới để đổi: '))
        check_connection()
        time.sleep(2)
        banner()
        d = 0
        for i in range(len(chontktiktok["data"])):
            if chontktiktok["data"][i]["unique_username"] == idacc:
                d = 1
                account_id = chontktiktok["data"][i]["id"]
                break
        if d == 0:
            print("Acc này chưa được thêm vào golike hoặc id sai!")
            continue
        checkdoiacc = 0
    print("                                     ", end="\r")
    print("Đang lọc nhiệm vụ!", end="\r")
    while True:
        try:
            nhanjob = nhannv(account_id)
            break
        except:
            pass
    if "status" in nhanjob and nhanjob["status"] == 200:
        ads_id = nhanjob["data"]["id"]
        link = nhanjob["data"]["link"]
        object_id = nhanjob["data"]["object_id"]
        loai = nhanjob["data"]["type"]
        if nhanjob["data"]["type"] not in lam:
            try:
                baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                print("                                             ", end="\r")
                print(f"Đang bỏ qua job {loai}", end="\r")
                sleep(1)
                continue
            except:
                pass
        if loai == "follow":
            loainv = "follow"
        elif loai == "like":
            loainv = " like "
        os.system(f"termux-open-url {link}")
        time.sleep(3)
        if auto_follow == "y":
            if loai == "follow":
                tap_screen(follow_x, follow_y)
                time.sleep(2)
            elif loai == "like":
                tap_screen(like_x, like_y)
        for remaining_time in range(delay, -1, -1):
            colors = [
                "[</>] REVIEWTOOL247 ",
                "[</>] REVIEWTOOL247 ",
                "[</>] REVIEWTOOL247 ",
                "[</>] REVIEWTOOL247 ",
                "[</>] REVIEWTOOL247 ",
                "[</>] REVIEWTOOL247 ",
                "[</>] REVIEWTOOL247 ",
            ]
            for color in colors:
                print(f"\r{color}|{remaining_time}| ", end="")
                time.sleep(0.12)
        print("\r                          \r", end="")
        print("Đang Nhận Tiền Job        ",end = "\r")
        while True:
            try:
                nhantien = hoanthanh(ads_id, account_id)
                break
            except:
                pass
        if lannhan == "y":
            checklan = 1
        else:
            checklan = 2
        ok = 0
        while checklan <= 2:
            if "status" in nhantien and nhantien["status"] == 200:
                ok = 1
                dem += 1
                tien = nhantien["data"]["prices"]
                tong += tien
                local_time = time.localtime()
                hour = local_time.tm_hour
                minute = local_time.tm_min
                second = local_time.tm_sec
                h = hour
                m = minute
                s = second
                if hour < 10:
                    h = "0" + str(hour)
                if minute < 10:
                    m = "0" + str(minute)
                if second < 10:
                    s = "0" + str(second)
                print("                                                    ", end="\r")
                chuoi = (f"| {dem}  | "
                         f"{h}:{m}:{s}  | "
                         f"{nhantien['data']['type']}  | "                                    
                         f"success  | "
                         f"+{tien}đ  | "
                         f"{tong} Vnđ")
                print(chuoi)
                checkdoiacc = 0
                break
            else:
                checklan += 1
                if checklan == 3:
                    break
                print("                                 ", end="\r")
                print("Đang Nhận Tiền Job Lần 2", end="\r")
                nhantien = hoanthanh(ads_id, account_id)
        if ok != 1:
            while True:
                try:
                    baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                    print("                                              ", end="\r")
                    print("Bỏ Qua Nhiệm Vụ !", end="\r")
                    sleep(1)
                    checkdoiacc += 1
                    break
                except:
                    qua = 0
                    pass
    else:
        sleep(10)