# AhriMAN

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


sec1 = range(3,11)
sec2 = range(1,3)

class Instagram_Bot:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def Exit_bot(self):
        driver = self.driver
        driver.close()
        # driver.quit()
        pass
    
    def Login_bot(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(random.choice(sec2))
        driver.find_element_by_xpath('//a[@href = "/accounts/login/?source=auth_switcher"]').send_keys(Keys.ENTER)
        time.sleep(5)
        item_username = driver.find_element_by_xpath('//input[@name = "username"]')
        item_username.clear()
        item_username.send_keys(self.username)
        time.sleep(random.choice(sec2))
        item_password = driver.find_element_by_xpath('//input[@name = "password"]')
        item_password.clear()
        item_password.send_keys(self.password)
        time.sleep(random.choice(sec2))
        item_password.send_keys(Keys.ENTER)
        time.sleep(random.choice(sec2))

        driver.find_element_by_xpath('//button[@class = "aOOlW   HoLwm "]').send_keys(Keys.ENTER)
        # self.Likes_Automatic_Following_bot()
    
    def Likes_Automatic_Following_bot(self):
        driver = self.driver
        pic_hrefs = []

        for i in range(1,5):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(random.choice(sec1))
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]
            except Exception:
                continue

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(random.choice(sec1))
            try:
                time.sleep(random.choice(sec1))
                driver.find_element_by_xpath('//span[@aria-label = "Like"]').click()
            except Exception:
                time.sleep(random.choice(sec2))

