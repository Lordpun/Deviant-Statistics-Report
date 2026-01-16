import requests

# Gets the data from a Deviant on DeviantArt throuht the API
def getDeviantData(username):
	url = "https://www.deviantart.com/api/v1/oauth2/user/profile/{username}"
	response = requests.get(url)
	if response.status_code == 200:atu
		return response.json()
	else:
		print('Error: ' + str(response.status_code))
		return None

# Gets the ten most recent posts of that user
def getRecentPosts(userData):
	pass

# Puts the needed data from the API into a dictionary
def getUserInfo(userData):
	pass