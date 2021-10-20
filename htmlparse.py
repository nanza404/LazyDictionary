import main
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime


wordCount = 0

def grabHtml():
    # grabs the full html of the url
    source = requests.get(main.sendUrl()).text
    # parses the html
    soup = bs(source, 'lxml')
    return soup 


def parse():
    formatedDefinition = ''
    # extracts the dictionary definitions
    defSection = grabHtml().find_all('span', attrs={'class':'dtText'})
    # makes sure the definition isnt empty
    if defSection != []:
        # parses the list of dictionary definitions
        for text in defSection:
            formatedDefinition += '\n' + text.get_text()
        # calls function to put it all together and print to file
        writeToDictFile(formatedDefinition)


def writeToDictFile(formatedDefinition):
    # increment amount of words added to dictionary
    global wordCount
    wordCount += 1
    # some text formating
    word = main.paste().upper()
    dictHeader = '<' + 5*'-' + 'Definition of ' + word + 5*'-' + '>\n'
    dateAndTime = datetime.now().strftime('------%m/%d/%y  %I:%M %p------')
    dictCapstone = '\n<' + (26+len(word))*'-' + '>\n\n\n'
    # putting it all together
    dictEntry = dictHeader + dateAndTime + formatedDefinition + dictCapstone
    # opens up a file to append the dictionary definitions
    with open('Dictionary.txt', 'a') as f:
        f.write(dictEntry)

