import requests, os, bs4, chromedriver_binary, time, smtplib, yagmail, keyring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
emailValue = "gmiller290488@gmail.com"
winnerPostcode = ""


def loadBrowser():
    url = "https://pickmypostcode.com/account/"
    browser.maximize_window()
    browser.get(url)

def enterDetails():
    postcodeValue = "n44eb"
    postcodeElemValue = "confirm-ticket"
    postcodeElem = browser.find_element_by_id(postcodeElemValue)
    postcodeElem.click()
    postcodeElem.send_keys(postcodeValue)

    emailElemValue = "confirm-email"
    emailElem = browser.find_element_by_id(emailElemValue)
    emailElem.click()
    emailElem.send_keys(emailValue)

def goToHomePage():
    signinXpath = "/html/body/div[2]/div[3]/main/div/div[1]/ul/li[1]/div/div/section/div/form/button"
    signinButtonElem = browser.find_element_by_xpath(signinXpath)
    signinButtonElem.click()

    mainPageXpath = "/html/body/div[2]/header/div/h1/a/img[2]"
    mainpageElem = browser.find_element_by_xpath(mainPageXpath)
    mainpageElem.click()

def acceptCookies():
    cookiesXpath = "/html/body/div[1]/div/div[1]/div/button[2]"
    cookiesElem = browser.find_element_by_xpath(cookiesXpath)
    cookiesElem.click()

def getWinningPostCode():
    global winnerPostcode
    winningTextXpath = "/html/body/div[2]/div[2]/div/main/div/section/div/div[1]/p[2]"
    winnerPostcodeText = browser.find_element_by_xpath(winningTextXpath)
    winnerPostcode = winnerPostcodeText.text.split('\n')[0]

def sendEmail():
    global winnerPostcode
    emailFrom = "postcoderwinner@gmail.com"
    emailSubject = "Your postcode is the winner!"
    emailBody = "Congratulations! % s is the winning postcode today! Log in at https://pickmypostcode.com/account/ to claim"% winnerPostcode
    yag = yagmail.SMTP(emailFrom, keyring.get_password('gmail', emailFrom))
    yag.send(emailValue, emailSubject, emailBody)

def start():
    loadBrowser()
    time.sleep(1)
    enterDetails()
    goToHomePage()
    time.sleep(1)
    acceptCookies()
    getWinningPostCode()
    sendEmail()

def check_postcode():
    start()
