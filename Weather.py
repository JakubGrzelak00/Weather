import requests
from bs4 import BeautifulSoup
import datetime
import os

# get user name to be able to open on a computer with different path
name = os.getlogin()
location = f"C:/Users/{name}/Desktop/Pogoda.txt"

# try to create txt file
try:
    txt = open(location, 'x')
except:
    f"[Errno 17] File exists: {location}"

# overwrite text with 'Pogoda' to not repeat himself
txt = open(location, 'w')
txt.write('Pogoda \n\n')
txt.close()

# open file to edit
txt = open(location, 'a')

# create list of weather descriptions to use later
descriptions_list = []

# create date
date = datetime.date.today() - datetime.timedelta(days=1)

# find and collects information's
side = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-lodz,cId,19059')
soup = BeautifulSoup(side.content, 'html.parser')
temps = soup.find_all(class_='weather-forecast-longterm-list-entry-forecast-temp')
descriptions = soup.find_all(class_='weather-forecast-longterm-list-entry-forecast-phrase')

# makes information's readable
for description in descriptions:
    descriptions_list.append(description.text)
description_number = 0

# writes information's for each temperature
for temp in temps:
    date = date + datetime.timedelta(days=1)
    date_text = str(date)
    txt.write(date_text + '\n')
    txt.write(temp.text + '\n')
    txt.write(descriptions_list[description_number])
    description_number += 1
    txt.write("\n\n")
txt.close()
