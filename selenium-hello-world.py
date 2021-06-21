import time
from selenium import webdriver
import pyautogui
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox()

exe_path = 'D:\python\geckodriver.exe'
binary = FirefoxBinary('C:\Program Files\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary, executable_path=exe_path)

browser.get("https://soundcloud.com/smalinux")

x = browser.find_element_by_css_selector("input").send_keys("happy")

pyautogui.press('enter')
time.sleep(10) 
x = browser.find_element_by_css_selector("#onetrust-accept-btn-handler").click()
time.sleep(10) 
x = browser.find_element_by_css_selector(".soundTitle__playButton:first-of-type").click()
time.sleep(10) 
# x = browser.find_element_by_css_selector("div.g:first-of-type a:first-of-type").click()

while True:
    pass
