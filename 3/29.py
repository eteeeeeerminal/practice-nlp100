import requests

url = "https://www.mediawiki.org/w/api.php"

response = requests.get(url, params={
    "action": "query", "format": "json", "prop": "imageinfo",
    "titles": "File:Flag of the United Kingdom.svg",
    "iiprop": "url"
})

print(response.json())