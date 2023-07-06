import requests

url = 'https://jsonplaceholder.typicode.com/users'

res = requests.get(url) # fire http get request to json api

users = res.json()# convert the data to a list of dict

print(users)
file =open('email.txt','w')
for user in users:
    file.write(user['name'].replace(' ','')+'@'+user['address']['city'].replace(' ' ,'')+'.com\n')

