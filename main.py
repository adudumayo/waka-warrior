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
rank = soup.find_all('a', {'name':'100'})
print(rank)

tags = soup.find_all('a')

'''for tag in tags:
    print(str(tag) + '\n')
    '''
