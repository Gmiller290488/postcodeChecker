import requests
import os
import bs4
import time
import smtplib
import yagmail
import keyring
import requests
import json
from .models import User
from validate_email import validate_email

emailValue = "gmiller290488@gmail.com"
winningPostcodes = []

def sendEmail():
    global winningPostcodes  
    emailToList = buildEmailList()
    emailFrom = "postcoderwinner@gmail.com"
    emailSubject = "Your postcode is a winner!"
    emailBody = "<h1>Congratulations!</h1> The winning postcodes today are: \n % s \n Log in at https://pickmypostcode.com/account/ to claim" % ",\n".join(winningPostcodes)
    yag = yagmail.SMTP(emailFrom, keyring.get_password('gmail', emailFrom))
    yag.send(to = emailToList, bcc = emailValue, subject = emailSubject, contents = emailBody)

def buildEmailList():
    winningPostcodesNoSpaces = [x.strip(' ') for x in winningPostcodes]
    emailTo = User.objects.filter(postcode__in=winningPostcodesNoSpaces)
    emailToList = []
    for user in emailTo:
        if validate_email(email_address=str(user), check_regex=True, check_mx=True, from_address='postcoderwinner@gmail.com', smtp_timeout=10, dns_timeout=10, use_blacklist=True):
            emailToList.append(str(user))
    return emailToList

def make_request():
    cookies = {
        'PHPSESSID': '3666568cee093c3f6ba9d857c93bd318',
        '_cmpQcif3pcsupported': '1',
        '_fbp': 'fb.1.1589014512656.938149904',
        '_hjid': '0d776cee-ae09-433b-aa99-0ca13a852545',
        '_ga': 'GA1.2.1179976700.1589014513',
        '_gid': 'GA1.2.1925405355.1589014513',
        'crfgL0cSt0r': 'true',
        'ntv_as_us_privacy': '1---',
        '__gads': 'ID=98cdb65f4afd9ecc:T=1589014521:S=ALNI_MYQ8-9rdEzaiikx8Ji4bF0do-wahA',
        'googlepersonalization': 'OzIF-5OzIGAwgA',
        'eupubconsent': 'BOzIF-5OzIGAwAKAAAENAAAA-AAAAA',
        'euconsent': 'BOzIF-5OzIGAwAKAACENDJ-AAAAvhr_7__7-_9_-_f__9uj3Gr_v_f__32ccL59v3h_7v-_7fi_-1nV4u_1vft9ydk1-5ctDztp507iakiPHmqNeb1n_mz1eZpRP58k09j5337Ew_v8_v-b7BCPN9Y3v-8K4',
        'FPL-SplitTest': 'v2-without-trustpilot',
        'fplCdn': 'useCdn',
        'FPL-LoggedIn': '2647436LoggedInPdijOeJ6g7xWFoks5hyUN2VTEn8YMu1fpclzQS0wKLB4GvrDCXqbRtmAIH3aZ9%3BLoggedIn%3B1603967283%3B3efc34f2aa477c22c4aff58e0a7f0112258e6746',
        'hotjar': 'norecord',
    }
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://pickmypostcode.com/?action=login-signin',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    params = (
        ('_', '1589103153431'),
    )

    response = requests.get('https://pickmypostcode.com/api/index.php/draws/main/',
                            headers=headers, params=params, cookies=cookies)
    postcodeJson = json.loads(response.text)
    get_all_postcodes(postcodeJson, "result")

def get_all_postcodes(json, key):
    global winningPostcodes
    if type(json) == str:
        json = json.loads(json)
    if type(json) is dict:
        for jsonkey in json:
            if type(json[jsonkey]) in (list, dict):
                get_all_postcodes(json[jsonkey], key)
            elif jsonkey == key:
                addPostcodeToList(json[jsonkey])

    elif type(json) is list:
        for item in json:
            if type(item) in (list, dict):
                get_all_postcodes(item, key)

def addPostcodeToList(postcode):
    winnerPostcodeLength = len(winningPostcodes)
    if winnerPostcodeLength == 0:
        winningPostcodes.append("Main draw: <strong>" + postcode + "</strong>")
    if winnerPostcodeLength == 1:
        winningPostcodes.append("Survey draw: <strong>" + postcode + "</strong>")
    if winnerPostcodeLength == 2:
        winningPostcodes.append("Video draw: <strong>" + postcode + "</strong>")

def start():
    make_request()
    sendEmail()