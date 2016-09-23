import requests

class UserRepo():
	def __init__(self, name=""):
		self.name = name
		self.base_url = "https://api.github.com/users/"
		# self.repo_list = []

	def get_repos(self, username):

		url = "{}{}{}".format(self.base_url, username, "/repos")
		
		r = requests.get(url)
		result = r.json()

		repo_list = []

		repo_list.append("wright")
		

		return repo_list

		# for index in result:
		# 	if result[index]["name"]:
		# 		repo_list.append(result[index]["name"])

	