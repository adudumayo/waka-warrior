from bs4 import BeautifulSoup
import requests

african_countries = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", 
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", 
    "Democratic Republic of the Congo", "Djibouti", "Egypt", "Equatorial Guinea", 
    "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", 
    "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", 
    "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", 
    "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", 
    "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", 
    "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", 
    "Tunisia", "Uganda", "Zambia", "Zimbabwe"
]

url = "https://wakatime.com/leaders"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all('a', {'class':'tip'})

for tag in tags:
    for country in african_countries:
        if country in str(tag):
            print(tag)

''' next step is crawling
    I will do it tomorrow
    I have work in the morning
'''
