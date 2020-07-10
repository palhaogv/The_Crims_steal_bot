import requests
from bs4 import BeautifulSoup, SoupStrainer
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from random import randint, random


#LOGIN
driver_l = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
driver_l.get('https://www.thecrims.com/#/')
time.sleep(2)

username = driver_l.find_element_by_xpath("//input[@placeholder='Username']")
username.send_keys('palhaogv')
time.sleep(2)

password = driver_l.find_element_by_xpath("//input[@placeholder='Password']")
password.send_keys('2a60f69c6199')
time.sleep(2)

driver_l.find_element_by_css_selector('.btn.btn-large.btn-inverse').click()
time.sleep(2)

while True:

    #ABA ROUBO
    driver_l.get('https://www.thecrims.com/alley#/robberies')
    time.sleep(2)

    select = Select(driver_l.find_element_by_id('singlerobbery-select-robbery'))
    select.select_by_value('29')
    time.sleep(1)

    driver_l.find_element_by_xpath('//*[@id="full"]').click()

    driver_l.find_element_by_xpath('//*[@id="singlerobbery-rob"]').click()
    time.sleep(1)

    while True:
        #ABA NIGHT LIFE
        driver_l.find_element_by_id('menu-nightlife').click()
        time.sleep(1.3)

        driver_l.find_element_by_css_selector('.btn.btn-inverse.btn.btn-inverse.btn-small.pull-right').click()
        time.sleep(1.1)

        #ABA MANSÃO
        driver_l.find_element_by_xpath('//*[@id="content_middle"]/div/div[3]/table[2]/tbody/tr/td[4]/button').click()
        time.sleep(1)


        driver_l.find_element_by_xpath("//*[contains(text(), 'Sair')]").click()
        time.sleep(1.5)
        # ABA ROUBO
        driver_l.get('https://www.thecrims.com/newspaper#/robberies')
        time.sleep(1)

        driver_l.find_element_by_xpath('//*[@id="singlerobbery-rob"]').click()
        time.sleep(1)

        try:
            driver_l.find_element_by_xpath("//*[contains(text(), 'Vício: 10%')]")
            driver_l.get('https://www.thecrims.com/newspaper#/hospital')
            time.sleep(2)
            driver_l.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(0.25)
            driver_l.find_element_by_xpath("//*[contains(text(), 'Desintoxicar por dinheiro')]").click()
            time.sleep(2)
            driver_l.execute_script("window.scrollTo(0,-1080)")

        except:
            pass

'''except:
        time.sleep(10)'''
'''# ABA NIGHT LIFE
        driver_l.find_element_by_id('menu-nightlife').click()
        time.sleep(1)
    
        driver_l.find_element_by_css_selector('.btn.btn-inverse.btn.btn-inverse.btn-small.pull-right').click()
        time.sleep(0.8)
    
        # ABA MANSÃO
        driver_l.find_element_by_xpath('//*[@id="content_middle"]/div/div[3]/table[2]/tbody/tr/td[4]/button').click()
        time.sleep(1)
        # driver_l.find_element_by_css_selector('.btn.btn-inverse').click()
        driver_l.find_element_by_xpath("//*[contains(text(), 'Sair')]").click()
        time.sleep(1)'''



