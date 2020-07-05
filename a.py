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
    email = browser.find_element_by_name('email')
    pwd = browser.find_element_by_name('pass')
    print "Html elements:"
    print "Email:", email, "\npassword:", pwd
    email.send_keys('edkan1@gmail.com')
    pwd.send_keys('5!dearms')
    browser.find_element_by_id('loginbutton').click()

test2()
