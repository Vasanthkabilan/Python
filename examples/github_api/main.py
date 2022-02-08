from urllib import response
import requests
response = requests.get("https://api.github.com/users/vasanthkabilan/repos")
my_repo = response.json()
# my_repo_name = my_repo[0]['name']
# print(my_repo_name)
for repo in my_repo:
    print(f"My repo name is: {my_repo[0]['name']}")
