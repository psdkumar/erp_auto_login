#!usr/bin/env python

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class AnimeDownloader :
	fp = webdriver.FirefoxProfile()
	fp.set_preference("browser.download.folderList",2)
	fp.set_preference("browser.download.manager.showWhenStarting",False)
	fp.set_preference("browser.download.dir", "/home/Documents/")
	fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-msdos-program")

	browser = webdriver.Firefox()
	searched = 0

	def __init__(self) :
		self.browser_link   = "http://kissanime.to/Login"
		self.user_name      = "shubhamwaghe"
		self.login_title    = "Login"
		self.loggedin_title = "KissAnime - Watch anime online in high quality"
		self.search_flag    = False
		self.search_keyword = "Dragon Ball (Sub)"
		self.search_url     = "http://kissanime.to/Anime/Dragon-Ball"
		self.user_password  = self.user_name

	def openBrowser(self) :
		self.browser.get(self.browser_link)
		time.sleep(5)
		self.browser.implicitly_wait(20)
		if self.browser.title != self.login_title : self.openBrowser()
		return self

	def login(self) :
		self.browser.implicitly_wait(20)
		self.browser.find_element_by_id("username").send_keys(self.user_name)      # Enter Username 
		self.browser.find_element_by_id("password").send_keys(self.user_password)  # Enter Password
		self.browser.find_element_by_id("btnSubmit").click()                       # Login

		self.browser.implicitly_wait(20)
		if self.browser.title != self.loggedin_title : self.openBrowser().login()  # Check for Login
		return self

	def search(self) :
		self.browser.implicitly_wait(20)
		self.browser.find_element_by_id("keyword").send_keys(self.search_keyword)              # Enter Search Keyword
		self.browser.find_element_by_id("imgSearch").click()    # Search
		self.search_url = self.browser.current_url
		return self

	def openEpisodes(self) :
		if self.search_flag : 
			self.search()
		else :	
			self.browser.get(self.search_url)   # Open Episodes page

		# Get links of all episodes
		episodeLinks = self.browser.find_elements_by_css_selector("table[class='listing'] a")
		for link in episodeLinks :
			episodeLink = link.get_attribute("href")
			print episodeLink
			self.openEpisode(episodeLink)
			return

	def openEpisode(self,episodeLink) :
		self.browser.get(episodeLink)  # Open Episode Page
		videoLink = self.browser.find_element_by_id("my_video_1_html5_api").get_attribute("src")
		self.browser.get(videoLink)    # Open Video Page
		video = self.browser.find_element_by_xpath("//video")
		ActionChains(self.browser).context_click(video).send_keys(Keys.SHIFT,"v").perform()


obj = AnimeDownloader()
#obj.openBrowser().openEpisode("http://kissanime.to/Anime/Dragon-Ball/Episode-153?id=17495")		
obj.openBrowser().login().openEpisodes()		
