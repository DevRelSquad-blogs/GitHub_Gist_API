import requests

url = "https://api.github.com/gists"
token = "YOUR_PERSONAL_ACCESS_TOKEN"

headers = {
    "Authorization": f"token {token}",
    "Content-Type": "application/json"
}

data = {
    "description": "My first Gist",
    "public": True,
    "files": {
        "hello_world.py": {
            "content": "print('Hello, world!')"
        }
    }
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print(f"Gist created successfully: {response.json()['html_url']}")
else:
    print(f"Failed to create gist: {response.status_code}")
