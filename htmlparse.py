import main
from bs4 import BeautifulSoup as bs
import requests
import re


def getDefinition():
    # grabs the html of the url
    source = requests.get(main.Dict.url).text
    # parses the html
    soup = bs(source, 'html.parser')
    # edit up to the first dictionary entery and make it more managable
    # (maybe dont strip strings)
    #string_section = soup.find('div', id=curr_entry).stripped_strings
    string_section = soup.find
    return string_section


def parse(string):

    return 0


def writeToDictFile():
    # opens up a file to append the dictionary definitions
    with open('Dictionary.txt', 'a') as f:
        f.write(definition)

