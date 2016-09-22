import requests

class UserRepo():
	def __init__(self, name=""):
		self.name = name
		self.base_url = "https://api.github.com/users/"

	def get_repos(self, username):

		url = "{}{}{}".format(self.base_url, username, "/repos")
		r = requests.get(url)
		result = r.json()

		repo_list = []

		for index in result:
			if result[index]["name"]:
				repo_list.append(result[index]["name"])

		print(repo_list)