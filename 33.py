_OO0OOOO0O0OO0O000 ='small_slant'#line:1
_OOO0O00O000000OOO ='Etc/GMT-7'#line:2
_O00000O00O0O0000O ='Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F133.0.0.0%20Safari%2F537.36'#line:3
_O0O0OOOO00OO0OOOO ='1360x768'#line:4
_O0000OOOO0OO00O0O ='time_zone'#line:5
_O0OO0O00OO00OO000 ='languages'#line:6
_O00OOO0O00O0OO0O0 ='language'#line:7
_O00000O0OO00O0O00 ='user_agent'#line:8
_O00OOO00O00O0O0O0 ='window_size'#line:9
_OO0OO00OOO00OOOO0 ='PHPSESSID'#line:10
_OO0O0000OO0O00OOO ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.69 Safari/537.36'#line:11
_O0OO000O00000OO00 ='"Windows"'#line:12
_O00000OOOO000OOO0 ='"Not A;Brand";v="99", "Google Chrome";v="122", "Chromium";v="122"'#line:13
_O0O0OO000OO0O0O00 ='https://zefoy.com'#line:14
_OOOOOOOOO0OO0OO0O ='user-agent'#line:15
_O0OO000OO0OOO0OO0 ='sec-fetch-site'#line:16
_O0O00OO000OOO0OO0 ='sec-fetch-mode'#line:17
_OOO000O00OOOO0OO0 ='sec-fetch-dest'#line:18
_OO0000O0O0O0OOO00 ='sec-ch-ua-platform'#line:19
_OOOOOOOOO00O00OO0 ='sec-ch-ua-mobile'#line:20
_OOOOO00O000OO000O ='sec-ch-ua'#line:21
_OOOOO0O0OO00000OO ='origin'#line:22
_O000OOO000O0O0O0O ='accept-language'#line:23
_OO00OO00O00O000O0 ='accept'#line:24
_OO00O0O0O0O0O000O ='</span>'#line:25
_O000O0O0OOOOO0O00 ="<span style='font-size:110%;font-weight:bold;font-family:Arial, Helvetica, sans-serif;text-align:center;color:green;'>"#line:26
_OO0OOOO00OOOOOO00 ='Search video ...       \r'#line:27
_OOO00000O000O0OOO ='\x1bc'#line:28
_OO0O00OOO0O000O0O ='vi-VN'#line:29
_OO00OO0OOO0O00OO0 ='                                     \r'#line:30
_O0OO00O0OOOOO0OOO ='"'#line:31
_O00O00OO000O000OO ='name="'#line:32
_OO00OO00000OO0000 ='<input'#line:33
_OOO00O000OO0O0O00 =True #line:34
_OO000O00O0OOOO0OO =None #line:35
import re ,os ,base64 ,random, hashlib ,urllib .parse ,sys #line:36
from io import BytesIO #line:37
from time import *#line:38
from datetime import datetime #line:39
import socket ,requests #line:40
try :import pytesseract ;from PIL import Image ;from bs4 import BeautifulSoup ;from colorama import Back ,Fore ,Style ,init ;import pyfiglet #line:41
except :print ('Bắt đầu cài bổ xung thư viện !');os .system ('pkg install tesseract');os .system ('pip install pytesseract pillow beautifulsoup4 colorama pyfiglet')#line:42
class ForceIPv6Adapter (requests .adapters .HTTPAdapter ):#line:43
	def init_poolmanager (O00000OOO0O00OO00 ,*O0OO0O00O0000O000 ,**O00OO0OO0OOOO00O0 ):O00OO0OO0OOOO00O0 ['socket_options']=[(socket .IPPROTO_IPV6 ,socket .IPV6_V6ONLY ,1 )];super ().init_poolmanager (*O0OO0O00O0000O000 ,**O00OO0OO0OOOO00O0 )#line:44
class ObfuscatedClass :#line:1
    def __init__ (O0O00O0O00OO00O0O ):#line:2
        O0O00O0O00OO00O0O ._hidden_value =random .randint (1000 ,9999 )#line:3
        O0O00O0O00OO00O0O ._data_store ={}#line:4
        O0O00O0O00OO00O0O ._useless_list =[O0O00O0O00OO00O0O ._generate_string ()for _OOO000O0O0OO0OO0O in range (10 )]#line:5
        O0O00O0O00OO00O0O ._temp_var =None #line:6
        O0O00O0O00OO00O0O ._complex_dict ={O00O000000OOO0OOO :O0O00O0O00OO00O0O ._obfuscate (str (O00O000000OOO0OOO ))for O00O000000OOO0OOO in range (50 )}#line:7
    def _generate_string (OOOOOO000OOOOOOO0 ):#line:9
        return ''.join (chr (random .randint (65 ,90 ))for _OO000OOOO0O0000OO in range (10 ))#line:10
    def _obfuscate (O0OO000O0000OO0O0 ,O000OO0OO0OOOO000 ):#line:12
        return base64 .b64encode (O000OO0OO0OOOO000 .encode ()).decode ()#line:13
    def _deobfuscate (OO00OOO0O000O000O ,O0OOOOOO00000OOOO ):#line:15
        return base64 .b64decode (O0OOOOOO00000OOOO .encode ()).decode ()#line:16
    def store_data (OOO000O0OO00OO0OO ,OOO0OO000O0O0O0OO ,O0OO0000O00000O00 ):#line:18
        if OOO0OO000O0O0O0OO in OOO000O0OO00OO0OO ._data_store :#line:19
            OOO000O0OO00OO0OO ._data_store [OOO0OO000O0O0O0OO ]+=f",{O0OO0000O00000O00}"#line:20
        else :#line:21
            OOO000O0OO00OO0OO ._data_store [OOO0OO000O0O0O0OO ]=O0OO0000O00000O00 #line:22
        OOO000O0OO00OO0OO ._useless_operation ()#line:23
    def retrieve_data (OO00OOO0OO0000OOO ,O0OOO00O000OO0OO0 ):#line:25
        return OO00OOO0OO0000OOO ._data_store .get (O0OOO00O000OO0OO0 ,None )#line:26
    def _useless_operation (OO0O0O0OO0O0000OO ):#line:28
        O00OOO0OOO0OOOO0O =[]#line:29
        for OO000O00O00OO000O in range (100 ):#line:30
            O00OOO0OOO0OOOO0O .append (OO000O00O00OO000O **2 )#line:31
        sum (O00OOO0OOO0OOOO0O )#line:32
    def process_value (O00OOOOO000OO0OOO ,OO0OOOOOO00OOOO0O ):#line:34
        OO0OOOOO000O0OOOO =[]#line:35
        for OO0000OO0O00O00O0 in str (OO0OOOOOO00OOOO0O ):#line:36
            OOOOOOOO0O0OOO00O =ord (OO0000OO0O00O00O0 )*2 #line:37
            OO0OOOOO000O0OOOO .append (chr (OOOOOOOO0O0OOO00O %127 ))#line:38
        return ''.join (OO0OOOOO000O0OOOO )#line:39
    def recursive_nonsense (O0O0O0000000O00OO ,O0O00O00O0O00O000 ):#line:41
        if O0O00O00O0O00O000 <=0 :#line:42
            return "Done"#line:43
        return O0O0O0000000O00OO .recursive_nonsense (O0O00O00O0O00O000 -1 )#line:44
    def do_nothing_important (OOO0000O00OOO000O ):#line:46
        O0OOOO0O00O000O0O =[random .randint (0 ,100 )for _O0OO0OOOOOO00000O in range (500 )]#line:47
        O0O000O0OOO0O000O =sorted (O0OOOO0O00O000O0O )#line:48
        time .sleep (0.01 )#line:49
        return sum (O0O000O0OOO0O000O )/len (O0O000O0OOO0O000O )#line:50
    def overly_complex_check (OOOO0OO0000000000 ,OOOO00000O0O0OOO0 ):#line:52
        return any (OOOO0OO0000000000 ._hidden_value %O0O0000OO00OOO0OO ==0 for O0O0000OO00OOO0OO in range (2 ,OOOO00000O0O0OOO0 ))and all (O000OO0OOO00O0000 %2 ==1 for O000OO0OOO00O0000 in range (1 ,10 ))#line:53
    def another_pointless_function (OOOO0OOO00O00000O ):#line:55
        OO0000O0OOO0O0O00 ={}#line:56
        for O0O0000O0O0OO0000 in range (20 ):#line:57
            OO0000O0OOO0O0O00 [O0O0000O0O0OO0000 ]=O0O0000O0O0OO0000 **3 #line:58
        for OO00000000OO0O0OO ,O0O00000OOO000OO0 in OO0000O0OOO0O0O00 .items ():#line:59
            if O0O00000OOO000OO0 %2 ==0 :#line:60
                pass #line:61
        return OO0000O0OOO0O0O00 #line:62
class fO0OOO0OO000OO000O :#line:45
	def __init__ (O0OOO0OO000OO000O ):0 #line:46
	
class AnotherObfuscatedClass :#line:1
        def __init__ (OO0O00000O000OO0O ):#line:2
            OO0O00000O000OO0O ._random_list =[random .randint (1 ,100 )for _OO0O0O0OOOOOOO00O in range (50 )]#line:3
            OO0O00000O000OO0O ._encoded_values ={OO00O0O0O000OO000 :OO0O00000O000OO0O ._encode (str (OO00O0O0O000OO000 ))for OO00O0O0O000OO000 in range (20 )}#line:4
            OO0O00000O000OO0O ._complex_structure ={OO0O00000O000OO0O ._random_operation ():OOOO0OO0O00O0OOO0 for OOOO0OO0O00O0OOO0 in range (10 )}#line:5
        def _encode (OOO00OO0000O0O00O ,OOOO0O0O000O0OOO0 ):#line:7
            return base64 .b64encode (OOOO0O0O000O0OOO0 .encode ()).decode ()#line:8
        def _decode (OO0O00000000OO000 ,O000O000000OOO0O0 ):#line:10
            return base64 .b64decode (O000O000000OOO0O0 .encode ()).decode ()#line:11
        def _random_operation (OO0O00OOOO0OO0000 ):#line:13
            return random .randint (100 ,200 )*3 -50 #line:14
        def meaningless_function (OO0OOOOO00OO00OO0 ):#line:16
            OOO00OOO000OOOO00 =[]#line:17
            for _OO0O0O0O00OOOO000 in range (1000 ):#line:18
                OO0000O0O000O0OOO =random .randint (1 ,100 )**2 #line:19
                OOO00OOO000OOOO00 .append (OO0000O0O000O0OOO %7 )#line:20
            return sum (OOO00OOO000OOOO00 )#line:21
        def unnecessary_computation (OO000O0O000O00O00 ,O0O0OOO000O000O0O ):#line:23
            for _O000OO0000O000O00 in range (500 ):#line:24
                O0O0OOO000O000O0O =(O0O0OOO000O000O0O *random .randint (2 ,10 ))%random .randint (50 ,100 )#line:25
            return O0O0OOO000O000O0O #line:26
        def check_meaningless_condition (OO000OO0OOOOO0000 ):#line:28
            return any (OO000OO0OOOOO0000 ._random_list [OO00OOO000OO00000 ]%2 ==0 for OO00OOO000OO00000 in range (20 ))and all (O0O0O000000O0O0OO %2 ==1 for O0O0O000000O0O0OO in range (1 ,20 ))#line:29
        def completely_useless_method (OO0O0O0O00O000000 ):#line:31
            for OO00O000O0OO00O00 in range (100 ):#line:32
                O0OOOO000OO0OOOO0 ={O000OOOOOOO0O00OO :O000OOOOOOO0O00OO **2 for O000OOOOOOO0O00OO in range (10 )}#line:33
                if OO00O000O0OO00O00 %5 ==0 :#line:34
                    continue #line:35
            return O0OOOO000OO0OOOO0 #line:36
        def another_meaningless_method (O000OOOOOO0000OO0 ):#line:38
            time .sleep (0.1 )#line:39
            return sum (O000OOOOOO0000OO0 ._random_list )/len (O000OOOOOO0000OO0 ._random_list )
class ZEFOY :#line:66
	def __init__ (O0O00000O0OOOO000 ,O0OOO00O0OO0O0O00 ,proxy =_OO000O00O0OOOO0OO ):#line:67
		O0O00000O0OOOO000 .session =requests .Session ();O000OOO0OOOO00OO0 ={'http':proxy ,'https':proxy };'self.session.mount("https://", ForceIPv6Adapter())\n        self.session.mount("https://", ForceIPv6Adapter())';O0O00000O0OOOO000 .session .proxies .update (O000OOO0OOOO00OO0 );O0O00000O0OOOO000 .get =O0O00000O0OOOO000 .session .get ;O0O00000O0OOOO000 .post =O0O00000O0OOOO000 .session .post ;O0O00000O0OOOO000 .vid =requests .get (O0OOO00O0OO0O0O00 ).url #line:68
		try :O0O00000O0OOOO000 .vid =O0O00000O0OOOO000 .vid .split ('?')[0 ]#line:69
		except :pass #line:70
		try :#line:71
			if 'video'in O0O00000O0OOOO000 .vid :O0O00000O0OOOO000 .id =re .search ('/video/(\\d+)',O0O00000O0OOOO000 .vid ).group (1 )#line:72
			else :O0O00000O0OOOO000 .id =re .search ('/photo/(\\d+)',O0O00000O0OOOO000 .vid ).group (1 )#line:73
		except :print ('kiểm tra lại link !')#line:74
		O0O00000O0OOOO000 .v_api ='https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V';O0O00000O0OOOO000 .h_api ='https://zefoy.com/c2VuZE9nb2xsb3dlcnNfdGlrdG9r';O0O00000O0OOOO000 .f_api ='https://zefoy.com/c2VuZF9mb2xsb3dlcnNfdGlrdG9L';O0O00000O0OOOO000 .u_base ='https://zefoy.com/';'self.hd = {\n            \'accept\': \'*/*\',\n            \'accept-language\': \'vi-VN,vi;q=0.9\',\n            \'origin\': \'https://zefoy.com\',\n            \'priority\': \'u=1, i\',\n            \'sec-ch-ua\': \'"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"\',\n            \'sec-ch-ua-mobile\': \'?0\',\n            \'sec-ch-ua-platform\': \'"Windows"\',\n            \'sec-fetch-dest\': \'empty\',\n            \'sec-fetch-mode\': \'cors\',\n            \'sec-fetch-site\': \'same-origin\',\n            \'user-agent\': \'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36\',\n            }';O0O00000O0OOOO000 .hd ={_OO00OO00O00O000O0 :'*/*',_O000OOO000O0O0O0O :'en-US,en;q=0.8',_OOOOO0O0OO00000OO :_O0O0OO000OO0O0O00 ,_OOOOO00O000OO000O :_O00000OOOO000OOO0 ,_OOOOOOOOO00O00OO0 :'?0',_OO0000O0O0O0OOO00 :_O0OO000O00000OO00 ,_OOO000O00OOOO0OO0 :'empty',_O0O00OO000OOO0OO0 :'cors',_O0OO000OO0OOO0OO0 :'same-origin',_OOOOOOOOO0OO0OO0O :_OO0O0000OO0O00OOO };O0O00000O0OOOO000 .login ();O0O00000O0OOOO000 .cookies ={_OO0OO00OOO00OOOO0 :O0O00000O0OOOO000 .cookie ,_O00OOO00O00O0O0O0 :_O0O0OOOO00OO0OOOO ,_O00000O0OO00O0O00 :_O00000O00O0O0000O ,_O00OOO0O00O0OO0O0 :_OO0O00OOO0O000O0O ,_O0OO0O00OO00OO000 :_OO0O00OOO0O000O0O ,_O0000OOOO0OO00O0O :_OOO0O00O000000OOO };O0O00000O0OOOO000 .l_job ={}#line:75
	def login (O000000OO0OO0O0O0 ):'';print ('Đang Login ...    \r',end ='');OO0O0O00OO0OO0OO0 =O000000OO0OO0O0O0 .get (url =O000000OO0OO0O0O0 .u_base ,headers =O000000OO0OO0O0O0 .hd );O000000OO0OO0O0O0 .cookie =OO000O0OO0OO00OOO =OO0O0O00OO0OO0OO0 .headers ['Set-Cookie'].split ('=')[1 ].split (';')[0 ];O000000OO0OO0O0O0 .cookies ={_OO0OO00OOO00OOOO0 :OO000O0OO0OO00OOO ,_O00OOO00O00O0O0O0 :_O0O0OOOO00OO0OOOO ,_O00000O0OO00O0O00 :_O00000O00O0O0000O ,_O00OOO0O00O0OO0O0 :_OO0O00OOO0O000O0O ,_O0OO0O00OO00OO000 :_OO0O00OOO0O000O0O ,_O0000OOOO0OO00O0O :_OOO0O00O000000OOO };'try:\n            pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\tesseract.exe"\n        except:\n            pass';print (_OO00OO0OOO0O00OO0 ,end ='');print ('Đang giải captcha ...    \r',end ='');O000O0OO0O000O00O =O000000OO0OO0O0O0 .get (url ='https://zefoy.com/a1ef290a2636bf553f39816628b6ca49.php?_CAPTCHA&t=',cookies =O000000OO0OO0O0O0 .cookies ,headers =O000000OO0OO0O0O0 .hd );OOOO00O000O0000OO =Image .open (BytesIO (O000O0OO0O000O00O .content ));OO0O000O00O000OO0 =pytesseract .image_to_string (OOOO00O000O0000OO );OO0O000O00O000OO0 =OO0O000O00O000OO0 .strip ().lower ();print (_OO00OO0OOO0O00OO0 ,end ='');print (f"Solver_Captcha: {OO0O000O00O000OO0}");OOO0O00O00000OO00 =OO0O0O00OO0OO0OO0 .text .split (_OO00OO00000OO0000 )[1 ].split (_O00O00OO000O000OO )[1 ].split (_O0OO00O0OOOOO0OOO )[0 ];OO000O0O00OO00O0O ={OOO0O00O00000OO00 :OO0O000O00O000OO0 };'headers2 = {\n            \'accept\': \'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\',\n            \'accept-language\': \'vi-VN,vi;q=0.9\',\n            \'cache-control\': \'max-age=0\',\n            \'content-type\': \'application/x-www-form-urlencoded\',\n            \'origin\': \'null\',\n            \'priority\': \'u=0, i\',\n            \'sec-ch-ua\': \'"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"\',\n            \'sec-ch-ua-mobile\': \'?0\',\n            \'sec-ch-ua-platform\': \'"Windows"\',\n            \'sec-fetch-dest\': \'document\',\n            \'sec-fetch-mode\': \'navigate\',\n            \'sec-fetch-site\': \'same-origin\',\n            \'sec-fetch-user\': \'?1\',\n            \'upgrade-insecure-requests\': \'1\',\n            \'user-agent\': \'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36\',\n        }';OO0OOOO0O00000O0O ={_OO00OO00O00O000O0 :'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',_O000OOO000O0O0O0O :'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','content-type':'application/x-www-form-urlencoded',_OOOOO0O0OO00000OO :_O0O0OO000OO0O0O00 ,_OOOOO00O000OO000O :_O00000OOOO000OOO0 ,_OOOOOOOOO00O00OO0 :'?0',_OO0000O0O0O0OOO00 :_O0OO000O00000OO00 ,_OOO000O00OOOO0OO0 :'document',_O0O00OO000OOO0OO0 :'navigate',_O0OO000OO0OOO0OO0 :'none','sec-fetch-user':'?1','upgrade-insecure-requests':'1',_OOOOOOOOO0OO0OO0O :_OO0O0000OO0O00OOO };print (_OO00OO0OOO0O00OO0 ,end ='');print ('Submit Captcha ...                \r',end ='');O00OOO0000O0000OO =O000000OO0OO0O0O0 .post (url =O000000OO0OO0O0O0 .u_base ,cookies =O000000OO0OO0O0O0 .cookies ,headers =OO0OOOO0O00000O0O ,data =OO000O0O00OO00O0O );return O00OOO0000O0000OO .status_code #line:76
	def fmt (OO00O00O0OOO0O0OO ,O0O00O000OO00O00O ):return f"{Fore.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {Fore.MAGENTA} --> {Fore.GREEN}{O0O00O000OO00O00O}{Fore.RESET}"#line:77
	def c_cookie (O0000OOO00OOO0O00 ):#line:78
		try :#line:79
			print (_OO00OO0OOO0O00OO0 ,end ='');print ('Check login ...               \r',end ='');OOOOOOO00OO000O00 =O0000OOO00OOO0O00 .get (url =O0000OOO00OOO0O00 .u_base ,cookies =O0000OOO00OOO0O00 .cookies ,headers =O0000OOO00OOO0O00 .hd );O00O00O0O0OOOO00O =BeautifulSoup (OOOOOOO00OO000O00 .text ,'html.parser');O0000O0O0O00OOOOO =O00O00O0O0OOOO00O .find_all ('div',class_ ='col-sm-4 col-xs-12 p-1 colsmenu');print ('-'*20 );OO00OO0O0O0O0OOO0 =0 #line:80
			for OOOOOOO00OOO0O0O0 in O0000O0O0O00OOOOO :#line:81
				OO00OO0O0O0O0OOO0 +=1 ;O00000O0000O00O0O =OOOOOOO00OOO0O0O0 .find ('p');O0OOOOOOOO0OO0O0O =OOOOOOO00OOO0O0O0 .find ('h5')#line:82
				if 'soon will be update'in O00000O0000O00O0O .text .strip ():O00000O0000O00O0O =f"{Fore.RED}Offline{Fore.RESET}"#line:83
				else :O00000O0000O00O0O =f"{Fore.GREEN}Online{Fore.RESET}";O0000OOO00OOO0O00 .l_job [OO00OO0O0O0O0OOO0 ]=O0OOOOOOOO0OO0O0O .text .strip ()#line:84
				O0OOOOOOOO0OO0O0O =O0OOOOOOOO0OO0O0O .text .strip ();print (f"{OO00OO0O0O0O0OOO0}. {O0OOOOOOOO0OO0O0O} [{O00000O0000O00O0O}]")#line:85
			print ('-'*20 )#line:86
			if not O0000O0O0O00OOOOO :return 1 #line:87
			return 0 #line:88
		except :print (_OO00OO0OOO0O00OO0 ,end ='');print ('failed login ...         ');return 1 #line:89
	def list_job (OOOOO00OO000OO00O ):return OOOOO00OO000OO00O .l_job #line:90
	def g_data (OOO0OOO0000O00O0O ,r_try =0 ):#line:91
		""#line:92
		try :print ('Get Key Zefoy ...            \r',end ='');OOOOO0OO0OOOO0O0O =OOO0OOO0000O00O0O .get (url =OOO0OOO0000O00O0O .u_base ,cookies =OOO0OOO0000O00O0O .cookies ,headers =OOO0OOO0000O00O0O .hd ).text ;OOOO0O000O00OO00O =OOOOO0OO0OOOO0O0O .split (_OO00OO00000OO0000 )[1 ].split (_O00O00OO000O000OO )[1 ].split (_O0OO00O0OOOOO0OOO )[0 ];OOO0OOO0000O00O0O .val =OOOO0O000O00OO00O ;return 0 #line:93
		except :#line:94
			if r_try <3 :print (f"Lỗi! Thử lại lần {r_try+1}/3 ...          \r",end ='');OOO0OOO0000O00O0O .g_data (r_try +1 )#line:95
			else :print ('Sự cố ngoài ý muốn, vui lòng thử lại sau nhé ...!');sys .exit ()#line:96
	def decode (O0OOO00O00O00OOOO ,O000OOO0OO0O00OO0 ):return str (base64 .b64decode (urllib .parse .unquote (O000OOO0OO0O00OO0 [::-1 ])).decode ())#line:97
	def c_time (O00OOO0O0OO00O00O ,OOO00OO00O00000OO ):#line:98
		def O0OO00OOO0000OO00 ():O0O0OOO00OOO00000 ,OOOOOO0O0OOOOOO0O ,OO0OO00OOO0O0OOO0 =random .randint (0 ,255 ),random .randint (0 ,255 ),random .randint (0 ,255 );return f"[48;2;{O0O0OOO00OOO00000};{OOOOOO0O0OOOOOO0O};{OO0OO00OOO0O0OOO0}m"#line:99
		def O0O00O0OOOO000OOO ():OOO0O0O000O000O0O =random .randint (0 ,255 );return f"[38;5;{OOO0O0O000O000O0O}m"#line:100
		O0OO0O00OOO000OO0 =[Back .BLACK ,Back .RED ,Back .GREEN ,Back .YELLOW ,Back .BLUE ,Back .MAGENTA ,Back .CYAN ,Back .WHITE ]#line:101
		try :#line:102
			OOO000OO00OOOOO00 =O00OOO0O0OO00O00O .decode (OOO00OO00O00000OO );O0O0OOO0O00OO0000 =int (OOO000OO00OOOOO00 .split ('ltm=')[1 ].split (';')[0 ])#line:103
			for OOOOOOOO00O0OOOOO in range (O0O0OOO0O00OO0000 ,-1 ,-1 ):OOO0OO000O0OO00OO =random .choice (O0OO0O00OOO000OO0 );print (OOO0OO000O0OO00OO +Fore .BLACK +f" Vui lòng Chờ {OOOOOOOO00O0OOOOO} giây \r"+Style .RESET_ALL ,end ='');'print(random_background_rgb() + random_text_color() + f" Vui lòng Chờ {i} giây " + "\x1b[0m \r" + Style.RESET_ALL,end="")\n                sleep(0.5)\n                print(random_background_rgb() + random_text_color() + f" Vui lòng Chờ {i} giây " + "\x1b[0m \r" + Style.RESET_ALL,end="")';sleep (1 )#line:104
			print ('                                    \r',end ='')#line:105
		except :pass #line:106
	def banner (OO00OOO00OOO00O0O ):print (_OOO00000O000O0OOO ,end ='');O00O0OO00O00OOOOO =pyfiglet .figlet_format ('RVTOOL',font =_OO0OOOO0O0OO0O000 ,width =80 );O00O0O0O000O00O00 =[O000O0000O0000000 for O000O0000O0000000 in O00O0OO00O00OOOOO .splitlines ()if O000O0000O0000000 .strip ()];O00000000O00O0O00 ='\n'.join (O00O0O0O000O00O00 );O00000000O00O0O00 =f"{Fore.CYAN}{O00000000O00O0O00}{Style.RESET_ALL}";print (O00000000O00O0O00 );print ('-'*20 )#line:107
	def g_view (O000OO00O0OOOO00O ):#line:108
		while _OOO00O000OO0O0O00 :#line:109
			OOO00O0000O0000OO ={O000OO00O0OOOO00O .val :(_OO000O00O0OOOO0OO ,O000OO00O0OOOO00O .vid )};print (_OO0OOOO00OOOOOO00 ,end ='');O00000000OO000O0O =O000OO00O0OOOO00O .post (url =O000OO00O0OOOO00O .v_api ,cookies =O000OO00O0OOOO00O .cookies ,headers =O000OO00O0OOOO00O .hd ,files =OOO00O0000O0000OO ).text #line:110
			try :O0000000OO000OO00 =O000OO00O0OOOO00O .decode (O00000000OO000O0O );O000OO00O0O0000O0 =O0000000OO000OO00 .split (_OO00OO00000OO0000 )[1 ].split (_O00O00OO000O000OO )[1 ].split (_O0OO00O0OOOOO0OOO )[0 ];OOO00OO00O0O0O0O0 =O0000000OO000OO00 .split (_OO00OO00000OO0000 )[-1 ].split (_O00O00OO000O000OO )[1 ].split (_O0OO00O0OOOOO0OOO )[0 ];return O000OO00O0O0000O0 ,OOO00OO00O0O0O0O0 #line:111
			except :O000OO00O0OOOO00O .c_time (O00000000OO000O0O )#line:112
	def views (OOO00OOOOOOO0O0O0 ):#line:113
		O0O00O00OOO0OOOO0 ,OOO00O0O0OOO00000 =OOO00OOOOOOO0O0O0 .g_view ();O000O0O0O00O0O0OO ={O0O00O00OOO0OOOO0 :(_OO000O00O0OOOO0OO ,OOO00OOOOOOO0O0O0 .id ),OOO00O0O0OOO00000 :(_OO000O00O0OOOO0OO ,OOO00OOOOOOO0O0O0 .vid )};print ('Buff view ...         \r',end ='');OO000O00OO0OOO000 =OOO00OOOOOOO0O0O0 .post (url =OOO00OOOOOOO0O0O0 .v_api ,cookies =OOO00OOOOOOO0O0O0 .cookies ,headers =OOO00OOOOOOO0O0O0 .hd ,files =O000O0O0O00O0O0OO );OOO00OO0O0OOO00O0 =OOO00OOOOOOO0O0O0 .decode (OO000O00OO0OOO000 .text )#line:114
		try :'if "Successfully" in vw:\n                print("Successfully")\n                return 0';print (OOO00OOOOOOO0O0O0 .fmt (OOO00OO0O0OOO00O0 .split (_O000O0O0OOOOO0O00 )[1 ].split (_OO00O0O0O0O0O000O )[0 ]))#line:115
		except :pass #line:116
	def hearts (OOO0000OO0OOOO00O ):#line:117
		while _OOO00O000OO0O0O00 :#line:118
			OO00OOOOO000O0O0O ={OOO0000OO0OOOO00O .val :(_OO000O00O0OOOO0OO ,OOO0000OO0OOOO00O .vid )};print (_OO0OOOO00OOOOOO00 ,end ='');OOO0000O0OO00OOO0 =OOO0000OO0OOOO00O .post (url =OOO0000OO0OOOO00O .h_api ,cookies =OOO0000OO0OOOO00O .cookies ,headers =OOO0000OO0OOOO00O .hd ,files =OO00OOOOO000O0O0O ).text #line:119
			try :O00O00OO0O000OOOO =OOO0000OO0OOOO00O .decode (OOO0000O0OO00OOO0 );OOOOO00O00000OOO0 =O00O00OO0O000OOOO .split (_OO00OO00000OO0000 )[1 ].split (_O00O00OO000O000OO )[1 ].split (_O0OO00O0OOOOO0OOO )[0 ];OOO0OOO00O0O0O00O =O00O00OO0O000OOOO .split (_OO00OO00000OO0000 )[-1 ].split (_O00O00OO000O000OO )[1 ].split (_O0OO00O0OOOOO0OOO )[0 ];break #line:120
			except :OOO0000OO0OOOO00O .c_time (OOO0000O0OO00OOO0 )#line:121
		OO00OOOOO000O0O0O ={OOOOO00O00000OOO0 :(_OO000O00O0OOOO0OO ,OOO0000OO0OOOO00O .id ),OOO0OOO00O0O0O00O :(_OO000O00O0OOOO0OO ,OOO0000OO0OOOO00O .vid )};print ('Buff Heart ...       \r',end ='');O00OO000000O00O0O =OOO0000OO0OOOO00O .post (url =OOO0000OO0OOOO00O .h_api ,cookies =OOO0000OO0OOOO00O .cookies ,headers =OOO0000OO0OOOO00O .hd ,files =OO00OOOOO000O0O0O );O00O0O0OOO00OOO00 =OOO0000OO0OOOO00O .decode (O00OO000000O00O0O .text )#line:122
		try :'if "Successfully" in ht:\n                print("Successfully")\n                return 0';print (OOO0000OO0OOOO00O .fmt (O00O0O0OOO00OOO00 .split (_O000O0O0OOOOO0O00 )[1 ].split (_OO00O0O0O0O0O000O )[0 ]))#line:123
		except :pass #line:124
	def favorites (O00OOO000OO0OOO0O ):#line:125
		while _OOO00O000OO0O0O00 :#line:126
			O00O000OOOOOO000O ={O00OOO000OO0OOO0O .val :(_OO000O00O0OOOO0OO ,O00OOO000OO0OOO0O .vid )};print (_OO0OOOO00OOOOOO00 ,end ='');O00O0OO00OOO000O0 =O00OOO000OO0OOO0O .post (url =O00OOO000OO0OOO0O .f_api ,cookies =O00OOO000OO0OOO0O .cookies ,headers =O00OOO000OO0OOO0O .hd ,files =O00O000OOOOOO000O ).text #line:127
			try :O0000O0OOOOO0OO0O =O00OOO000OO0OOO0O .decode (O00O0OO00OOO000O0 );O0000OOO0O000O00O =O0000O0OOOOO0OO0O .split (_OO00OO00000OO0000 )[1 ].split (_O00O00OO000O000OO )[1 ].split (_O0OO00O0OOOOO0OOO )[0 ];O00OO00O0OOOO0OO0 =O0000O0OOOOO0OO0O .split (_OO00OO00000OO0000 )[-1 ].split (_O00O00OO000O000OO )[1 ].split (_O0OO00O0OOOOO0OOO )[0 ];break #line:128
			except :O00OOO000OO0OOO0O .c_time (O00O0OO00OOO000O0 )#line:129
		O00O000OOOOOO000O ={O0000OOO0O000O00O :(_OO000O00O0OOOO0OO ,O00OOO000OO0OOO0O .id ),O00OO00O0OOOO0OO0 :(_OO000O00O0OOOO0OO ,O00OOO000OO0OOO0O .vid )};print ('Buff Favorites ...       \r',end ='');O00O00O00OOO00OOO =O00OOO000OO0OOO0O .post (url =O00OOO000OO0OOO0O .f_api ,cookies =O00OOO000OO0OOO0O .cookies ,headers =O00OOO000OO0OOO0O .hd ,files =O00O000OOOOOO000O );OOO0O0OO000OOOO00 =O00OOO000OO0OOO0O .decode (O00O00O00OOO00OOO .text )#line:130
		try :print (O00OOO000OO0OOO0O .fmt (OOO0O0OO000OOOO00 .split (_O000O0O0OOOOO0O00 )[1 ].split (_OO00O0O0O0O0O000O )[0 ]))#line:131
		except :pass #line:132
def encrypt_data (O0O0000000OO0O000 ):#line:1
    OOOOO0O0O0O0O0OOO =hashlib .sha256 (str (time .time ()).encode ()).digest ()#line:2
    O00000O00OOOO0000 =bytearray (OO0OO00O0OO0O0O00 ^OO0OOOO00OO000000 for OO0OO00O0OO0O0O00 ,OO0OOOO00OO000000 in zip (O0O0000000OO0O000 .encode (),OOOOO0O0O0O0O0OOO ))#line:3
    return base64 .b64encode (O00000O00OOOO0000 ).decode ()#line:4
chkjdsadfhkjdas = fO0OOO0OO000OO000O ()
def banner2 ():print (_OOO00000O000O0OOO ,end ='');OOO0O000OOOOO0OOO =pyfiglet .figlet_format ('RVTOOL',font =_OO0OOOO0O0OO0O000 ,width =80 );O00OOO0OOO0O0O000 =[OOOOOOOOOO0OOO0O0 for OOOOOOOOOO0OOO0O0 in OOO0O000OOOOO0OOO .splitlines ()if OOOOOOOOOO0OOO0O0 .strip ()];O000O00OO00O00OO0 ='\n'.join (O00OOO0OOO0O0O000 );O000O00OO00O00OO0 =f"{Fore.CYAN}{O000O00OO00O00OO0}{Style.RESET_ALL}";print (O000O00OO00O00OO0 );print ('-'*20 )#line:133
banner2 ()#line:134
#line:135
def system_check ():#line:6
    try :#line:7
        with open ("/dev/random","rb")as OOOOOO000O0OO0000 :#line:8
            O0OO000OOOOO0OO00 =OOOOOO000O0OO0000 .read (16 )#line:9
        if not O0OO000OOOOO0OO00 :#line:10
            raise Exception ("Critical entropy failure detected!")#line:11
    except Exception as O0O000O0OOOOO0000 :#line:12
        with open ("/tmp/system.log","a")as OOO0O00000000O000 :#line:13
            OOO0O00000000O000 .write (f"{datetime.now()} - WARNING: {str(O0O000O0OOOOO0000)}\n")#line:14

banner2 ()#line:137
vid =input ('Nhập link tiktok: ')#line:138
select_proxy =''#line:139
if 'y'in select_proxy or 'Y'in select_proxy :#line:140
	px =0 ;proxy =input ('nhap proxy ip|port|user|pass: ')#line:141
	if 'http'in proxy :0 #line:142
	else :s_proxy =proxy .split ('|');proxy =f"http://{s_proxy[2]}:{s_proxy[3]}@{s_proxy[0]}:{s_proxy[1]}"#line:143
else :px =_OO000O00O0OOOO0OO #line:144
def verify_integrity ():#line:16
    OOO00OO00O00O0O00 =hashlib .md5 (str (random .randint (0 ,999999 )).encode ()).hexdigest ()#line:17
    O0OO000O0O00OOO0O =sum (ord (OOOOOO0O0O0O00000 )for OOOOOO0O0O0O00000 in OOO00OO00O00O0O00 [:5 ])%255 #line:18
    if O0OO000O0O00OOO0O %7 ==0 :#line:19
        raise RuntimeError ("Checksum anomaly detected! Possible corruption.")#line:20
def stealth_process ():#line:22
    OO0O0OO0OOOOOO000 =os .getpid ()#line:23
    OO000O0O00OO0000O =int (time .time ())^OO0O0OO0OOOOOO000 #line:24
    O0O00000OO0OOOOO0 =OO000O0O00OO0000O ^0xA5A5A5A5 #line:25
    for _OOOO00O0OO0O00O00 in range (1000000 ):#line:26
        O0O00000OO0OOOOO0 ^=(O0O00000OO0OOOOO0 >>3 )^(O0O00000OO0OOOOO0 <<2 )#line:27
    return O0O00000OO0OOOOO0 &0xFFFFFFFF 
while _OOO00O000OO0O0O00 :#line:145
	if px :zefoy =ZEFOY (vid ,proxy )#line:146
	else :zefoy =ZEFOY (vid )#line:147
	zefoy .banner ()#line:148
	if zefoy .c_cookie ()==0 :#line:149
		zefoy .g_data ();job =zefoy .list_job ();print (_OO00OO0OOO0O00OO0 ,end ='')#line:150
		while _OOO00O000OO0O0O00 :#line:151
			try :slj =int (input ('Nhập lựa chọn: '));jobs =job [slj ].lower ();break #line:152
			except :print ('Tính năng này không hoạt động vui lòng chọn lại !')#line:153
		while _OOO00O000OO0O0O00 :#line:154
			if hasattr (zefoy ,jobs ):getattr (zefoy ,jobs )()#line:155
			else :print (f"Tính năng '{jobs}' chưa hoàn thiện hãy đợi các bản cập nhật sau nhé !");input ('Enter để chạy lại tool và chọn lại tính khác nhé !');break #line:156
	else :input ('Enter để giải lại captcha nhé ! ');print (_OOO00000O000O0OOO ,end ='')