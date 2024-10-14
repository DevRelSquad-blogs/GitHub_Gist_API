import requests

token = "YOUR_PERSONAL_ACCESS_TOKEN"

headers = {
    "Authorization": f"token {token}",
    "Content-Type": "application/json"
}

gist_id = "GIST_ID"

update_data = {
    "description": "Updated description",
    "files": {
        "hello_world.py": {
            "content": "print('Hello, updated world!')"
        }
    }
}

response = requests.patch(f"https://api.github.com/gists/{gist_id}", json=update_data, headers=headers)

if response.status_code == 200:
    print(f"Gist updated: {response.json()['html_url']}")
else:
    print(f"Failed to update gist: {response.status_code}")
