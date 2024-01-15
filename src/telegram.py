#!/usr/bin/env python3

import requests
from birthday import divContent, config
from bs4 import BeautifulSoup

bot_token = config['credentials']['bot_token']
base_url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"

# Initialize an empty list to store the parameters for each birthday
all_parameters = []

soup = BeautifulSoup(divContent, 'html.parser')
# Loop through the soup.find_all('div') elements
for div in soup.find_all('div'):
    name = div.text.strip()
    link = div.find('img')['src']

    # Create the parameters dictionary directly in the loop
    parameters = {
        "chat_id": config['credentials']['chatid'],
        "photo": link,
        "caption": "Happy Birthday " + name + "🎂"
    }

    # Append the parameters to the list
    all_parameters.append(parameters)

for parameters in all_parameters:
    resp = requests.get(base_url, params=parameters)
    print(resp)
