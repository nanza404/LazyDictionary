import main
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime

def grabHtml():
    # grabs the full html of the url
    source = requests.get(main.Dict.sendUrl()).text
    # parses the html
    soup = bs(source, 'lxml')
    return soup 


def parse():
    formatedDefinition = ''
    # extracts the dictionary definitions
    defSection = grabHtml().find_all('span', attrs={'class':'dtText'})
    if defSection != []:
        # parses the list of dictionary definitions
        for text in defSection:
            formatedDefinition += '\n' + text.get_text()
        # calls function to put it all together and print to file
        writeToDictFile(formatedDefinition)


def writeToDictFile(formatedDefinition):
    # some text formating
    word = main.Dict.paste().upper()
    dictHeader = '<' + 5*'-' + 'Definition of ' + word + 5*'-' + '>\n'
    dateAndTime = datetime.now().strftime('------%m/%d/%y  %I:%M %p------')
    dictCapstone = '\n<' + (26+len(word))*'-' + '>\n\n\n'
    # putting it all together
    dictEntry = dictHeader + dateAndTime + formatedDefinition + dictCapstone
    # opens up a file to append the dictionary definitions
    with open('Dictionary.txt', 'a') as f:
        f.write(dictEntry)


#def errorHandle():
#    text = grabHtml() 
#    # is None then there is no definition(word to malformed)
#    text1 = text.find('div', attrs={'class':'words_fail_us_cont search-results'})
#    # word is some how misspelled and the website offers suggestions
#    text2 = text.find('p', attrs={'class':'missing-query'})
#    # if text1 or text2 return None then it is a dictionary webpage
#    if text1 == None:
#        if text2 == None:
#            text1, text2 = ' ', ' '
#            print('text1 true')
#            return True
#    else:
#        text1, text2 = ' ', ' '
#        print('false')
#        return False




