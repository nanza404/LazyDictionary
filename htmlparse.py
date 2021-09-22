from bs4 import BeautifulSoup as bs
import requests
import re

url = 'https://www.merriam-webster.com/dictionary/' 
word = ''

def wordLogger():
    curr_entry = 'dictionary-entry-1'
    # grabs the html of the url
    source = requests.get(url).text
    # parses the html
    soup = bs(source, 'lxml')
    # edit up to the first dictionary entery and make it more managable
    # (maybe dont strip strings)
    string_section = soup.find('div', id=curr_entry).stripped_strings
    return string_section


def parse():
    return 0


def writeToDictFile():
    # opens up a file to append the dictionary definitions
    with open('Dictionary.txt', 'a') as f:
        f.write(definition)

