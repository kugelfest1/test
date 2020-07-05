import requests

""" example using requests"""
def test():
    r=requests.get('http://ip.jsontest.com/')
    print("Response object:", r)
    print("Response text:", r.text)

""" example using selenoum
    remember to install selenium, and download geckodriver
"""
from selenium import webdriver
def test2():
    browser = webdriver.Firefox()
    print "Webdriver object", browser
    browser.get('https://facebook.com')

test2()
