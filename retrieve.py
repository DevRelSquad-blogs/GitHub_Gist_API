import requests

token = "YOUR_PERSONAL_ACCESS_TOKEN"

headers = {
    "Authorization": f"token {token}",
    "Content-Type": "application/json"
}

gist_id = "GIST_ID"
response = requests.get(f"https://api.github.com/gists/{gist_id}", headers=headers)

if response.status_code == 200:
    print(f"Gist content: {response.json()['files']}")
else:
    print(f"Failed to retrieve gist: {response.status_code}")
