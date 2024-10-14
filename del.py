import requests

token = "YOUR_PERSONAL_ACCESS_TOKEN"

gist_id = "GIST_ID"

headers = {
    "Authorization": f"token {token}",
    "Content-Type": "application/json"
}

response = requests.delete(f"https://api.github.com/gists/{gist_id}", headers=headers)

if response.status_code == 204:
    print("Gist deleted successfully")
else:
    print(f"Failed to delete gist: {response.status_code}")