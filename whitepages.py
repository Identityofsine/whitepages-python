import requests
import json
from bs4 import BeautifulSoup #pip install bs4
import cloudscraper #pip3 install cloudscraper

class WhitePages: # Create a class
	def __init__(self, firstname, lastname, city, state, result): #Set variables
		self.fistname = firstname
		self.lastname = lastname
		self.city = city
		self.state = state
		self.result = result
		if result < 1 or isinstance(result, int) is False:
			print("Please use a real number")
			return
		url = f"https://www.whitepages.com/name/{firstname}-{lastname}/{state}?fs=1&searchedName={firstname}%20{lastname}"
		#^ General Link for URL Search of White-Pages
		self.scraper = cloudscraper.create_scraper() # use cloudscrapper in-order to bypass Cloudflare Protection
		#page = requests.get(url)
		html = self.scraper.get(url).text # Grab Website and put into text
		soup = BeautifulSoup(html, 'html.parser') #Use bs4 to parse the page
		item = soup.findAll('script', {"type":"application/ld+json"}) #look for the script json file that is responible for querying
		self.jsone = json.loads(item[1 - result].contents[0]) #load json file from Whitepages.com
		self.url = "https://www.whitepages.com" + self.jsone[0]["URL"] #grab URL
		self.Name = self.jsone[0]["name"] #Grab Name
		self.al = self.jsone[0]["address"][0]["addressLocality"] #Grab Loaclity
		self.ar = self.jsone[0]["address"][0]["addressRegion"] #Grab Region


	def GetName(self): #return name
		return self.Name

	def json(self, x): #return json script
		if x == 1:
			return self.jsone
		elif x == 2:
			return self.jsone 

	def GetCityandState(self): #return City and State
		return f"{self.al},{self.ar}"

	def GetMainAddress(self): #return main address if found.
		info_url = self.scraper.get(self.url).text
		info_soup = BeautifulSoup(info_url, 'html.parser')
		info_script = info_soup.find('a', {"class":"mb-1 raven--text text-decoration-none"})
		item_address = info_script.getText().replace("\n", " ")
		return item_address

	def GetMainPhoneNumber(self): #return main phone number if found
		info_url = self.scraper.get(self.url).text
		info_soup = BeautifulSoup(info_url, 'html.parser')
		if info_soup.findAll('div', {"class":"col-md-4 col-12"}) == []:
			return "No Phone Number was Found"
		else:
			numbers = ""
			info_script = info_soup.findAll('a', {"class":"px-5 py-9 pearl v-card v-card--flat v-card--link v-sheet theme--light"})
			for x in info_script:
				numbers = x.getText() + numbers
		return numbers.replace("\n", " ")

