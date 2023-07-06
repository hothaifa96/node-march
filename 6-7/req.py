import requests

response = requests.get('https://jsonplaceholder.typicode.com/comments')

print(response.status_code)
data = response.json()
for comment in data:
    print(comment['id'])

# https://jsonplaceholder.typicode.com/users
# send get http request to this link
# for each user generate a new email built like this
# user name @ city .com
# and add the email to emails.txt file