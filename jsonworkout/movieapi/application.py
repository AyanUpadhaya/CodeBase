# Get tv show data using python and api
# site - tvmaze.com/api
# script by - Ayan Upadahya
# contact -> ayanU881@gmail.com
# twitter -> https://twitter.com/ayanupadhaya96
# GitHub  -> github.com/AyanUpadhaya
# Youtube -> Code Tech :https://www.youtube.com/channel/UCsjnvE4i5Z-VR-lWhODX99w

import requests
import json

print('Enter your Search:')
search=input()

url="https://api.tvmaze.com/singlesearch/shows?q="+search

response = requests.get(url,timeout=6)

if response.status_code==200:
	data= json.loads(response.text)
	
	print('Show Name: '+data['name'])
	print('Language: '+data['language'])
	print('Genres: '+str(data['genres']))
	print('Status: '+data['status'])
	print("Premiered: "+data['premiered'])
	print("Rating: "+str(data['rating']['average']))
	print('Summary: '+data["summary"])

	with open('moviedata.json','w') as f:
		json.dump(data,f)
else:
	print(f"Error {response.status_code}")

