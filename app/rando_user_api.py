import requests

class Randomly():
	def __init__(self, 
		title="",
		first="", 
		last="", 
		picture=None,
		email="",
		cell="",
		gender="",

		):
		
		self.title = title
		self.first = first
		self.last = last
		self.picture = picture
		self.email = email
		self.cell = cell
		self.gender = gender

class RandoUserAPI():
	def __init__(self):
		self.base_url = "https://randomuser.me/api/"


	def generate_rando(self):


		url = "{}{}".format(self.base_url, "?results=10")
		r = requests.get(url)
		result = r.json()

		rando_list = []

		x = 9
		while x > 0:
			bootilicious = Randomly(
				title = result["results"][x]["name"]["title"],
				first = result["results"][x]["name"]["first"],
				last = result["results"][x]["name"]["last"],
				picture = result["results"][x]["picture"]["thumbnail"],
				email = result["results"][x]["email"],
				cell = result["results"][x]["cell"],
				gender = result["results"][x]["gender"]
			)

			rando_list.append(bootilicious)

			x -= 1

		return rando_list