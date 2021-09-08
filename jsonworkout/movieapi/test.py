import json
#json text example
todo = '''
[
	{
		"text":"send the mails",
		"phone":"01516166485",
		"mail":"json@gmail.com",
		"date":"10-08-2021",
		"isCompleted":"False"
	},

	{
		"text":"send the mails",
		"phone":"01516166485",
		"mail":"json@gmail.com",
		"date":"10-08-2021",
		"isCompleted":"True"
	},

	{
		"text":"Set Doctors appointment",
		"phone":"01516169485",
		"mail":"doctor@gmail.com",
		"date":"10-08-2021",
		"isCompleted":"True"
	}
]

'''


#how to dump json into a json file
with open('task.json','w') as f:
	json.dump(todo,f)


#how to read a json file
with open('task.json','r') as f:
	data = json.load(f)


#how to convert json string into list
text = json.loads(data)


#how to fetch data from json list
for items in text:
	print(items['text'])
	print(items['mail'])
	print()
