import requests

class UserRepo():
	def __init__(self):
		self.base_url = "https://api.github.com/users/"
		# self.repo_list = []

	def get_repos(self, username):

		url = "https://api.github.com/users/{}/repos".format(username)
		q = requests.get(url)
		result = q.json()

		repo_list = []

		for diction in result:
			repo_list.append(diction["full_name"])

		return repo_list


		# for index in result:
		# 	if result[index]["name"]:
		# 		repo_list.append(result[index]["name"])