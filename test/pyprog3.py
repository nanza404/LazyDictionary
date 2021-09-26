import webbrowser as wb
import pyxhook as ph
import pyperclip as pc
from bs4 import BeautifulSoup as bs
import requests
import re


url = 'https://www.merriam-webster.com/dictionary/' 
word = ''


def wordLogger():
    source = requests.get(url).text
    soup = bs(source, 'lxml')
    definition = ''
    definit = ''
    curr_entry = 'dictionary-entry-1'
    string_section = soup.find('div', id=curr_entry).stripped_strings
    mainWord = True 
    colon = False

    for string in string_section:
        if re.search('Entry \d of \d', string):
            def_num = re.findall('\d', string)
            while int(def_num[0]) <= int(def_num[1]):
                string_section = soup.find('div', id=curr_entry).stripped_strings
                for string in string_section:
                    if string == ('Definition of'):
                        pass
                    elif (string == word and mainWord): 
                        definit += ('---'+string+'---\n')
                        mainWord = False
                    elif re.search('^..+.$', string):
                        definit += string+' '
                    elif ord(string) in range(49, 58) or ord(string) in range(97, 110):
                        definit += '\n'+string
                        colon = True
                    elif (string == ':' and colon):
                        definit += string+' '
                        colon = False
                    else:
                        definit += string
                #the list definit needs to be earsed after it is printed
                print(definit)
                definition += definit
                definit = ''
                def_num[0] = str(int(def_num[0])+1)
                curr_entry = 'dictionary-entry-'+def_num[0]

#opens up a file to append the dictionary definitions
    with open('Dictionary.txt', 'a') as f:
        f.write(definition)


######-Keylogger(pyxhook)-#####
def OnKeyPress(event):
#global keyword means these variables modify the global varibles
    global word
    global url
    word = pc.paste()
    url = 'https://www.merriam-webster.com/dictionary/' + word 
    if event.Key == 'd':        
        wb.open_new(url)
        wordLogger()


hm = ph.HookManager()
hm.KeyDown = OnKeyPress
hm.HookKeyboard()
hm.start()
#####-End of Keylogger-#####

