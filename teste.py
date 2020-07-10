from selenium import webdriver
import time

#LOGIN
driver_l = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
driver_l.get('https://www.thecrims.com/#/')
time.sleep(2)

driver_l.find_element_by_xpath("//*[contains(text(), 'Ganhe dinheiro')]") == True



