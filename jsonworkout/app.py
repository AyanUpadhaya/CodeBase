# The first thing json does is it will convert a json data into python dictionary
# The second thing is it will convert a dictionary/list into json data 

import json
import pandas as pd
json_string='{"name":"Ayan Upadhaya","age": 30,"ismarried":"False","birthday":"28 oct 1992","city": "Rajshahi","country":"Bangladesh"}'
json_dictiionary=[
		{
			"name":"Ayan Upadhaya",
			"age": 30,
			"ismarried":False,
			"birthday":"28 oct 1991",
			"city": "Rajshahi",
			"country":"Bangladesh",
			"email":"ayanu881@gmail.com"
		},
		{
			"name":"Anjan Upadhaya",
			"age": 33,
			"ismarried":True,
			"birthday":"28 oct 1991",
			"city": "Rajshahi",
			"country":"Bangladesh",
			"email":"anjan.ku2005@gmail.com"
		},

		{
			"name":"Ajit Upadhaya",
			"age": 60,
			"ismarried":True,
			"birthday":"01 oct 1954",
			"city": "Santoshpur",
			"country":"Bangladesh",
			"email":"no-email",
		},
]


# data= json.loads(json_string)

# for key,value in data.items():
# 	print(key +' :'+str(value))


# dump list as json data into a json file

with open('data.json','w') as file:
	json.dump(json_dictiionary,file)


# get json data from file and convert to string

with open('data.json') as file:
	data=json.load(file)



# for key in data:
# 	for kn,vl in key.items():
# 		print(kn+':'+str(vl))

df=pd.DataFrame(data)


print(df.to_string())
print('Success!')