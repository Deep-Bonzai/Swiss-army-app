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

		for index, value in enumerate(result["results"]):
			bootilicious = Randomly(
				title = result["results"][index]["name"]["title"],
				first = result["results"][index]["name"]["first"],
				last = result["results"][index]["name"]["last"],
				picture = result["results"][index]["picture"]["thumbnail"],
				email = result["results"][index]["email"],
				cell = result["results"][index]["cell"],
				gender = result["results"][index]["gender"],
			)

			rando_list.append(bootilicious)

		return rando_list