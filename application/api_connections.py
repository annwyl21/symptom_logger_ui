import requests

class ApiConnect():
	
	@staticmethod
	def request_visuals(parcel):
		# Make the api request
		endpoint = "https://visualizesl.onrender.com/"
		path = "slvapi/visualize"
		url = endpoint + path

		headers = {
			'Content-Type': 'application/json'
		}

		# Make the request
		#return requests.post(url, headers=headers, data=parcel).text
# data = because we are sending a json string, instead of json= which would be a dictionary
		
		return requests.post(url, headers=headers, data=parcel).json()
		
	