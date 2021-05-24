import requests
import re
from bs4 import BeautifulSoup

#TODO: Create food list for each day of all menu types like diet, paleo, dessert, etc
baseUrl = requests.get("https://www.interfood.hu/etlap-es-rendeles/?het=202121")
dietasUrl = requests.get("https://www.interfood.hu/food/foodindex.php?foodpage=etlap-es-rendeles&het=202121&blokk=dietas&lang=hu")
dietas = BeautifulSoup(dietasUrl.content, "html.parser")
menu = []

# Mivel nem tudom elore, hogy Interfood melyik napra csinal etelt es
# tablazatuk nem tartalmazza, hogy melyik nap van az etel, ezert
# napok helyett napszamokat hasznalok az etelek csoportositasara.
days = 0
day0 = []
day1 = []
day2 = []
day3 = []
day4 = []
dayX = []

items = dietas.find_all("span")
for item in items:
    if re.fullmatch(r"D[46789]:.*", item.text):
        menu.append(item.text)
        if "D4:" in item.text:
            days += 1

for i, food in enumerate(menu):
    if i % days == days - days:
        day0.append(food[4:])
    elif i % days == days - (days - 1):
        day1.append(food[4:])
    elif i % days == days - (days - 2):
        day2.append(food[4:])
    elif i % days == days - (days - 3):
        day3.append(food[4:])
    elif i % days == days - (days - 4):
        day4.append(food[4:])
    else:
        dayX.append(food[4:])

print("Heti diétás menü:")
print("Diétás menüt tartalmazó napok száma:", days)
if len(day0) > 0:
    print("Első nap:")
    for food in day0:
        print("\t", food)
else:
    print("Nem található diétás menü a héten.")

if len(day1) > 0:
    print("\nMásodik nap:")
    for food in day1:
        print("\t", food)

if len(day2) > 0:
    print("\nHarmadik nap:")
    for food in day2:
        print("\t", food)

if len(day3) > 0:
    print("\nNegyedik nap:")
    for food in day3:
        print("\t", food)

if len(day4) > 0:
    print("\nÖtodik nap:")
    for food in day4:
        print("\t", food)

if len(dayX) > 0:
    print("\nHétvége?:")
    for food in day3:
        print("\t", food)
