from selenium import webdriver
from selenium.webdriver.common import Keys
import time

class InstagramBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome()

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		#use source code for login
		driver = self.driver
		driver.get("https://www.instagram.com/")
		time.sleep(2)
		login_button = driver.find_element_by_xpath("//a[@href'accounts/login']]")
		login_button.click()
		time.sleep(2)
		user_name_elem = driver.find_element_by_xpath("//input[@name = 'username']")
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)
		password_elem = driver.find_element_by_xpath("//input[@name = 'username']")
		password_elem.clear()
		password_elem.send_keys(self.password)
		password_elem.send_keys(Keys.RETURN)

	def like_photo(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/" +hashtag + "/?hl=en")
		time.sleep(2)
		for i in range(1,3):
			driver.execute()

