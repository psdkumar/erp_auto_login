# Main Code for the ERP Login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AutoLoginERP :
	# Initialising Web Driver
	browser = webdriver.Firefox()

	def __init__(self) :
		# Initialise Details
		details = open('details.txt','r')
		allDetails = details.readlines()
		self.__lgnid   = allDetails[0][:-1]
		self.__passwrd = allDetails[1][:-1]
		self.__qstn1   = allDetails[2][:-1]
		self.__ans1    = allDetails[3][:-1]
		self.__qstn2   = allDetails[4][:-1]
		self.__ans2    = allDetails[5][:-1]
		self.__qstn3   = allDetails[6][:-1]
		self.__ans3    = allDetails[7][:-1]
		self.__title   = "Welcome " + allDetails[8][:-1] + " to ERP, IIT Kharagpur"
		self.__dict    = {self.__qstn1 : self.__ans1, self.__qstn2 : self.__ans2, self.__qstn3 : self.__ans3}
		details.close()

	def openERP(self) :
		# Open ERP Webpage
		self.browser.get('http://erp.iitkgp.ernet.in/')
		success = "Welcome to ERP" in self.browser.title
		if success != True : self.openERP()
		return self	                          

	def enterDetails(self) :
		# Enter Login Id
		loginId = self.browser.find_element_by_id("user_id")
		loginId.send_keys(self.__lgnid)

		# Enter Password
		password = self.browser.find_element_by_id("password")
		password.send_keys(self.__passwrd)

		# Finding Secuirty Question 
		self.browser.implicitly_wait(20)
		qstn = self.browser.find_element_by_xpath("//label[@for = 'answer']").text

		# Finding & Entering Answer for Secuirty Question
		ans = self.__dict[qstn]
		self.browser.implicitly_wait(20)
		self.answer = self.browser.find_element_by_id("answer")
		self.answer.send_keys(ans)
		return self

	def login(self) :	
		# Logging In
		self.answer.send_keys(Keys.RETURN)
		self.browser.implicitly_wait(20)
		success = self.__title in self.browser.title
		if success != True :
			self.openERP().enterDetails().login()
		return self	

	def home(self) :
		# Go to Home Page
		return

	def mails(self) :
		# Go to Mails Section
		self.browser.find_element_by_xpath("//i[@class = 'fa fa-lg fa-envelope']").click()  # Mails	

	def academic(self) :
		# Go to Academic Section
		self.browser.find_element_by_xpath("//a[@href = 'menulist.htm?module_id=16']").click()  # Academic
	
	def cdc(self) :
		# Go to CDC Section
		self.browser.find_element_by_xpath("//a[@href = 'menulist.htm?module_id=26']").click()  # CDC
	
	def companies(self) :
		# Go to Company's list Section
		self.browser.find_element_by_xpath("//a[@href = 'menulist.htm?module_id=26']").click()  # CDC
		self.browser.find_element_by_xpath("//a[@class = 'text-primary']").click()              # Student
		self.browser.implicitly_wait(20)
		self.browser.find_element_by_xpath("//*[contains(text(), 'Application of Placement/Internship')]").click()	# Application of Placement/Internship
