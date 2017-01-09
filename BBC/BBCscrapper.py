# This program scraps twitter pages for tweets. Is written by jeev20. https://github.com/jeev20
# Thanks to https://textblob.readthedocs.io/en/dev/

####     Features     #####
#This program scraps BBC articles. Converts the News articles to text.
#Saves the article text in Article.txt file
#Converts text to speech and saves to Title.mp3 and Article.mp3 file

from bs4 import BeautifulSoup
from urllib import *
import urllib
from textblob import TextBlob
import sys
import time
import webbrowser
from gtts import gTTS
import pygame


# open a public URL, in this case, the webbrowser
url1 = "http://www.bbc.com/news"
webbrowser.open_new_tab(url1)

time.sleep(3)


# user can input BBC article link
url = raw_input("Please paste link to BBC News article : ")


#input webaddress of the twitter account
webadd = urllib.urlopen(url).read()
soup = BeautifulSoup(webadd, "html.parser")


#tweet title extraction
def title():
	return(soup.title.text)


# loop to print article text
def text():
	t=""
	for article in soup.find('div',class_= "story-body__inner").findAll('p'):
	#for article in soup.find('div', class_="column--primary").findAll('p'):
		t += article.text[0:]
	return t


def time():
	for article in soup.find('div',class_= "date date--v2"):
		time = (article.string)
	return time		


t = text()		
test = TextBlob(t)
sa = (test.sentiment.polarity)


"""
#debugging
print title()
title = title()
print ""
print time()
print ""
print text()
heading = text()
print ""
print "Sentiment anlaysis value is: ",float ("%.4f" %(sa))
"""

tts = gTTS(text= title(), lang = "en")
tts.save("Title.mp3")
pygame.mixer.init()
pygame.mixer.music.load("Title.mp3")
pygame.mixer.music.play()

tts = gTTS(text= text(), lang = "en")
tts.save("Article.mp3")
pygame.mixer.init()
pygame.mixer.music.load("Article.mp3")
pygame.mixer.music.play()


file = open("Article.txt", "w")

reload(sys)
sys.setdefaultencoding('utf-8')
file.write(title() )
file.write("\n")
file.write(time())
file.write("\n")
file.write(text())


file.close()	









