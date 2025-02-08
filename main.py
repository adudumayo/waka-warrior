from bs4 import BeautifulSoup
import requests


url = "https://wakatime.com/leaders"

response = requests.get(url)

print(response)
