import requests

class RandoUserAPI():
	def __init__(self, 
		title="",
		first="", 
		last="", 
		picture=None,
		email="",
		cell="",
		gender="",

		):
		self.base_url = "http://api.randomuser.me"
		self.title = title
		self.first = first
		self.last = last
		self.picture = picture
		self.email = email
		self.cell = cell
		self.gender = gender

	

	def generate_rando(self):
		url = "{}{}".format(self.base_url, "/results=10")
		r = requests.get(url)
		result = r.json()




		self.title = result["results"][0]["name"]["title"]
		self.first = result["results"][0]["name"]["first"]
		self.last = result["results"][0]["name"]["last"]
		self.picture = result["results"][9]["picture"]["thumbnail"]
		self.email = result["results"][2]["email"]
		self.cell = result["results"][7]["cell"]
		self.gender = result["results"][0]["gender"]
			
		return self.title, self.first, self.last, self.picture, self.email, self.cell, self.gender