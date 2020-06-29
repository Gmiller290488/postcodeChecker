import requests
from .models import User

cookies = {
    '_fbp': 'fb.1.1589980394392.1210488137',
    '_ga': 'GA1.2.554155135.1589980395',
    'ntv_as_us_privacy': '1---',
    '__gads': 'ID=2a55f8f6d3bc91df:T=1590079782:S=ALNI_MbOpi4oACNJG4UWIHCcEGKhuAzXzQ',
    '_cmpQcif3pcsupported': '1',
    'PHPSESSID': '01260b9c07960f515ae50ddc05b4a7a7',
    '_hjid': '517e8638-36cd-4a16-8604-e78c448f0cc8',
    'GED_PLAYLIST_ACTIVITY': 'W3sidSI6IkFFU0kiLCJ0c2wiOjE1OTIzMTQxODMsIm52IjoxLCJ1cHQiOjE1OTIzMTQxNTIsImx0IjoxNTkyMzE0MTgzfV0.',
    'referralWidget': 'closed',
    'hotjar': 'norecord',
    'crfgL0cSt0r': 'true',
    'googlepersonalization': 'Ozs8E_O1wSsPgA',
    'eupubconsent': 'BOzs8E_O1wSsPAKAiAENAAAA-AAAAA',
    'euconsent': 'BOzs8E_O1wSsPAKAiBENDQ-AAAAwdrv7_77e_9f-_f__9uj3Gr_v_f__32ccL5tv3hv7v-_7fi_-0nV4u_1tft9ydk1-5ctDztp507iakiPHmqNeb1n_mz1eZpRP58E09j53z5Ew_v8_v-b7BCPN_Y3v-8K96lA',
    'FPL-SplitTest': 'v2-without-trustpilot',
    'FPL-LandingTracking': '5ef9b7443d9dd--v2-without-trustpilot--1593423684',
    'fplCdn': 'useCdn',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://pickmypostcode.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://pickmypostcode.com/?action=loggedout',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

data = {
  'email': '',
  'postcode': ''
}

def login():
    make_login_request()

def make_login_request():
    users = User.objects.all()
    for user in users:
        data['email'] = user.email
        data['postcode'] = user.postcode
        response = requests.post('https://pickmypostcode.com/api/index.php/login/from/main', headers=headers, cookies=cookies, data=data)