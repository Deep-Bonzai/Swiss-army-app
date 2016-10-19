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
		# while x > 0:
		for person in result['results']:
			bootilicious = Randomly(
				title = person["name"]["title"],
				first = person["name"]["first"],
				last = person["name"]["last"],
				picture = person["picture"]["thumbnail"],
				email = person["email"],
				cell = person["cell"],
				gender = person["gender"]
			)

			rando_list.append(bootilicious)


		return rando_list