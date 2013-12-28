#!/usr/bin/python

from bs4 import BeautifulSoup
from urllib2 import urlopen


alist = [] #all songs urls list
singleurl = [] #all songs directel dl links list

#all songs extraction from album page function
def multilink(ul):
 html = urlopen(ul).read()
 soup = BeautifulSoup(html)
 x = soup.find_all("a", class_='autoindex_a')
 c = 0
 for i in x:
  alist.insert(c,i.get('href'))
  c = c +1
 
#direct dl links extractor function
def singlink(x):
 html = urlopen(x).read()
 soup = BeautifulSoup(html)
 x = soup.find("span", {"id": "download_link"})
 y=x.a.get('href')
 e=0
 singleurl.insert(e,y)

#replace space in url with %20 function
def urlencoder(ul):
	aclinks = []
	k=0
	for ii in ul:
	    l =ii.replace(" ", "%20")
	    aclinks.insert(k,l)
	return aclinks

#main codes goes from here
ll=raw_input("Music.com.bd link genereter\nEnter album url:")

multilink(ll);#call function

alist.pop(0) #remove first item

amlinks = []
amlinks = urlencoder(alist) #url spaces remove
for j in amlinks:
	singlink(j) #get direct link 


alinks = []
alinks = urlencoder(singleurl) #url spaces remove

for i in reversed(alinks):
    print i
	





