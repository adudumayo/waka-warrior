from bs4 import BeautifulSoup
import requests


url = "https://wakatime.com/leaders"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

print(soup)
