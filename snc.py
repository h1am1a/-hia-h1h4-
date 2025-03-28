import requests
import time
import sys
import os 
import time
import json
import random
from time import sleep
try:
    import os
    import sys
    import time
    import subprocess
    import requests
    from bs4 import BeautifulSoup
    from colorama import Fore
    from pystyle import Colorate, Colors
    from tabulate import tabulate
    from art import *
    from time import sleep
except ImportError:
    os.system("pip install requests tabulate art colorama beautifulsoup4")
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
    print("[✔] Đã lưu thông tin thiết bị.")
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
def save_coordinates(follow_x, follow_y):
    with open("coordinates_snapchat.txt", "w") as file:
        file.write(f"follow_x={follow_x}\n")
        file.write(f"follow_y={follow_y}\n")
    print("[✔] Đã lưu tọa độ vào thiết bị.")
def load_coordinates():
    if os.path.exists("coordinates_snapchat.txt"):
        coordinates = {}
        with open("coordinates_snapchat.txt", "r") as file:
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
  sleep(0.0001)
def reload():
    try:
        url = "https://www.google.com/recaptcha/api2/reload"
        params = {
            "k": "6LfiTfQUAAAAANM8yUWHdhLQ1pwdkaGlaCHUW609",
            "reason": "rresp",
            "v": "v1528855115741",
            "c": "YOUR_RECAPTCHA_RESPONSE",
        }
        response = requests.post(url, params=params)
        response.raise_for_status()
        if response.status_code == 200:
            
            return True
        else:
            print(f"Lỗi khi giải reCAPTCHA: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi giải reCAPTCHA: {e}")
        return False
def get_new_job(account_id, ses, headers):
    """Lấy job mới từ API"""
    url = f'https://gateway.golike.net/api/advertising/publishers/snapchat/jobs?account_id={account_id}&data=null'
    response = ses.get(url, headers=headers).json()
    return response if response['status'] == 200 else None
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
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
def check_snapchat_error():
    """Kiểm tra xem có lỗi trong Snapchat không bằng logcat"""
    try:
        log_output = subprocess.check_output("logcat -d | grep 'Snapchat'", shell=True, text=True)
        if "LỖI !!!" in log_output or "link này không hoạt động" in log_output:
            return True
    except subprocess.CalledProcessError:
        pass
    return False    
def SNAPCHAT():
    url1_2 = 'https://gateway.golike.net/api/snapchat-account'
    checkurl1_2 = ses.get(url1_2, headers=headers).json()
    user_snapchat1 = []
    account_ids = []
    STT = []
    STATUS = []
    tong = 0
    dem = 0
    i = 1
    for data in checkurl1_2['data']:
        name = data['name']
        account_id = data['id']
        STT.append(i)
        account_ids.append(account_id)
        print(f'[</>] ➩ Nhập Số | {i} | => Tài Khoản: {name}')
        i += 1
    print('══════════════════════════════════════════════════════════════')
    choose = int(input('[</>] ➩ Nhập Số: ')) - 1
    check_connection()
    os.system('cls' if os.name== 'nt' else 'clear')
    banner()
    if choose < 0 or choose >= len(account_ids):
        print("Lựa chọn không hợp lệ!")
        return
    account_id = account_ids[choose]
    while True:
        try:
            job_count = int(input(f'[</>] ➩ Nhập Số Lượng Job: '))
            break
        except:
            print("Vui lòng nhập lại!")
    while True:
        try:
            DELAY = int(input(f'[</>] ➩ Nhập Delay: '))
            break
        except:
            print("Vui lòng nhập lại!")
    while True:
        try:
            print('══════════════════════════════════════════════════════════════')
            auto_follow = input("Bạn có muốn sử dụng ADB không? (y/n): ").strip().lower()
            check_connection()
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
                            follow_x = int(input("Nhập Tọa Độ x Nút Follow SnapChat: "))
                            follow_y = int(input("Nhập Tọa Độ y Nút Follow SnapChat: "))
                            check_connection()
                            print('══════════════════════════════════════════════════════════════')
                            save_coordinates(follow_x, follow_y,)
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
                            print(f"Sử dụng tọa độ đã lưu: Follow ({follow_x}, {follow_y})")
                            break
                        else:
                            if os.path.exists("coordinates_snapchat.txt"):
                                os.remove("coordinates_snapchat.txt")
                                print("[✔] Đã xóa tọa độ đã lưu.")                       
                            while True:
                                try:
                                    print('══════════════════════════════════════════════════════════════')
                                    follow_x = int(input("Nhập Tọa Độ x Nút Follow SnapChat: "))
                                    follow_y = int(input("Nhập Tọa Độ y Nút Follow SnapChat: "))
                                    check_connection()
                                    print('══════════════════════════════════════════════════════════════')
                                    save_coordinates(follow_x, follow_y,)
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
    for i in range(job_count):
        reload()
        print("Đang lọc nhiệm vụ!", end="\r")
        job_data = get_new_job(account_id, ses, headers)
        if not job_data or 'data' not in job_data:
            print(f"Không tìm thấy job hoặc Golike hết job!")
            countdown(DELAY)
            continue  
        linkjob = job_data['data']['link']
        ads_id = job_data['data']['id']
        object_id = job_data['data']['object_id']
        type = job_data['data']['type']
        subprocess.run(['termux-open-url', linkjob], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)
        if check_snapchat_error():
            print(f"Snapchat báo lỗi: Link không hoạt động! {linkjob}")            
            skipjob_url = 'https://gateway.golike.net/api/advertising/publishers/snapchat/skip-jobs'
            skip_params = {
                'ads_id': ads_id,
                'account_id': account_id,
                'object_id': object_id,
            }
            check_skipjob = ses.post(skipjob_url, params=skip_params).json()
            if check_skipjob.get('status') == 200:
                message = check_skipjob.get('message', 'Đã skip job thành công!')
                print(str(message))
            else:
                print("Lỗi khi gửi skip job!")
            continue
        
        if type == "follow":
            loainv = "follow"
        if auto_follow == "y":
            if type == "follow":
                tap_screen(follow_x, follow_y)
                time.sleep(2)
        complete_params = {
            'ads_id': ads_id,
            'account_id': account_id,
            'object_id': object_id,
            'data': 'null',
            'type': type,
        }
        countdown(DELAY)
        url3 = 'https://gateway.golike.net/api/advertising/publishers/snapchat/complete-jobs'
        checkurl3 = ses.post(url3, params=complete_params).json()
        if checkurl3['status'] == 200:
            dem += 1
            local_time = time.localtime()
            h = f"{local_time.tm_hour:02d}"
            m = f"{local_time.tm_min:02d}"
            s = f"{local_time.tm_sec:02d}"
            prices = checkurl3['data']['prices']
            tong += prices
            chuoi = (
                f"| {dem} | "
                f"{h}:{m}:{s} | "
                f"{type} | "
                f"success | "
                f"+{prices}đ | "
                f"{tong} Vnđ"
            )
            print(chuoi)
        else:
            print("Lỗi khi hoàn thành job!")       
            # Gửi skip job
            skipjob_url = 'https://gateway.golike.net/api/advertising/publishers/snapchat/skip-jobs'
            skip_params = {
                'ads_id': ads_id,
                'account_id': account_id,
                'object_id': object_id,
                'async': 'true',
                'data': 'null',
                'type': type,
            }
            check_skipjob = ses.post(skipjob_url, params=skip_params).json()
            if check_skipjob.get('status') == 200:
                message = check_skipjob.get('message', 'Đã skip job thành công!')
                print(str(message))
            else:
                print("Lỗi khi gửi skip job!")
            continue

banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input('[</>] ➩ Authorization Golike: ')
    check_connection()
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()

ses = requests.Session()
try:
    headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
                'Referer':'https://app.golike.net/',
                'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':"Windows",
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-site',
                'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                "Authorization" : file,
                'Content-Type':'application/json;charset=utf-8'            
    }

    url1 = 'https://gateway.golike.net/api/users/me'
    checkurl1 = ses.get(url1,headers=headers).json()
except requests.exceptions.InvalidHeader:
    os.remove('user.txt')
    #user
if checkurl1['status']== 200 :
        print('Đăng Nhập Thành Công!')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        banner()
        ses.headers.update(headers)
        print("[</>] ➩ Nhập Số | 1 | Để Vào Tool SnapChat")
        print('[</>] ➩ Nhập Số | 2 | Để Xóa Authorization Hiện Tại')
        print('══════════════════════════════════════════════════════════════')
        choose = int(input('[</>] ➩ Nhập Số: '))
        check_connection()
        if choose == 1:
                os.system('cls' if os.name== 'nt' else 'clear')
                banner()
                ses.headers.update(headers)
                SNAPCHAT()
        elif choose == 2:
                os.remove('user.txt')
                print(Fore.GREEN + "[✔] Đã xóa user.txt!")
else:
    print('Đăng Nhập Thất Bại!')
    os.remove('user.txt')