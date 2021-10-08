import main
from bs4 import BeautifulSoup as bs
import requests

def getDefinition():
    # grabs the full html of the url
    source = requests.get(main.Dict.sendUrl()).text
    # parses the html
    soup = bs(source, 'lxml')
    # other alternatives
    #defSection = soup.find_all('div', attrs={'id':'dictionary-entry-1'})
    #defSection = soup.find('div', attrs={'id':'dictionary-entry-1'}).stripped_strings
    # extracts the dictionary definitions
    defSection = soup.find_all('span', attrs={'class':'dtText'})
    return defSection 


def parse():
    defText = getDefinition()
    formatedDefinition = ''
    # parses the list of dictionary definitions
    for text in defText:
        formatedDefinition += '\n' + text.get_text()
    # calls function to put it all together and print to file
    writeToDictFile(formatedDefinition)


def writeToDictFile(formatedDefinition):
    # some formating
    word = main.Dict.paste().upper()
    dictHeader = '<' + 5*'-' + 'Definition of ' + word + 5*'-' + '>'
    dictCapstone = '\n<' + (26+len(word))*'-' + '>\n\n\n'
    # putting it all together
    dictEntry = dictHeader + formatedDefinition + dictCapstone
    # opens up a file to append the dictionary definitions
    with open('Dictionary.txt', 'a') as f:
        f.write(dictEntry)
