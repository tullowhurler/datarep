import requests
from bs4 import BeautifulSoup 
with open("../week02-carview\carviewer.html") as fp:     
    soup = BeautifulSoup(fp,'html.parser') 
print (soup.prettify()) 
 
 