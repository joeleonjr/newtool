import requests

# Example API call to list repositories of the authenticated user
def list_repositories():
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": "token ghp_aB3dfgH8kL9mN4pQrSt1uVwXyZ2aBcDeFgHiJkLm"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(f"Repository: {repo['name']}")
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")

# Call the function to list repositories
list_repositories()
