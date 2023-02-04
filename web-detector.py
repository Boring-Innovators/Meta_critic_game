import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

base_url = "https://www.metacritic.com/game/playstation-4/"

with open("top.txt", "r") as f:
    names = f.readlines()

with open("existing_websites_top.txt", "w") as f_exist, open("non_existing_websites.txt", "w") as f_not_exist:
    for name in names:
        name = name.strip()
        url = base_url + name
        session = requests.Session()
        response = session.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 404:
            f_not_exist.write(f"{name}\n")
        else:
            f_exist.write(f"{name}\n")