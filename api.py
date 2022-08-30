import requests

try:
    response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
    print(type(response.json()))
    projects = response.json()

    for project in projects:
        print(project["name"],
              project["web_url"])
except:
    print('An exception occurred')
