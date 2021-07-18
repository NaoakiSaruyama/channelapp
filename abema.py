from urllib import request
from bs4 import BeautifulSoup, element

url = "https://abema.tv/timetable"

open = request.urlopen(url)

soup = BeautifulSoup(open, "html.parser")
elements=soup.select('body')

for element in elements:
  print(element)