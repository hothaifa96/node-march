import requests

url = 'https://jsonplaceholder.typicode.com/users'

res = requests.get(url) # fire http get request to json api

users = res.json()# convert the data to a list of dict

print(users)
file =open('email.txt','w') # open new email file or override it if its exists
for user in users: # iterate all the users and enter the new email to the file
    file.write(user['name'].replace(' ','')+'@'+user['address']['city'].replace(' ' ,'')+'.com\n')
    #replace all spaces with nothing and build an email with the username

