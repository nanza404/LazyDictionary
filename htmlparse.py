import main
from bs4 import BeautifulSoup as bs
import requests
import re

def getDefinition():
    # grabs the full html of the url
    source = requests.get(main.Dict.sendUrl()).text
    # parses the html
    soup = bs(source, 'lxml')
    # grab section of html
    string_section = soup.find_all('span', attrs={'class':'dtText'})
    return string_section


def parse():
    text = getDefinition()
    for snippets in text:
        print(snippets.get_text())
    #print(text[0].find_all('span', attrs={'class':'dtText'}).text)
    #return 0


def writeToDictFile():
    # opens up a file to append the dictionary definitions
    with open('Dictionary.txt', 'a') as f:
        f.write(definition)
