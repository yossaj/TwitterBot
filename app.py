from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config 

class TwitterBot:
    def __init__(self,username,password):
        self.username = username 
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('http://www.twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)


doggo = TwitterBot(config.username, config.password)
doggo.login()
