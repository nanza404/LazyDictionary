from bs4 import BeautifulSoup as bs
import requests

source = requests.get('https://www.merriam-webster.com/dictionary/spontaneous').text

soup = bs(source, 'lxml')

definition = []
#loop through the html and when you find <span class="num">1</span> add a new
#line character after the number. Veiw the block of html before span class=num
#as a block and then view span class=num as a block and then the html after as a
#block until the next span class=num

#extract the text from those blocks(add nesisarry newline characters)
#and then append to the definitions list

string_section = soup.find('div', id='dictionary-entry-1').stripped_strings
l_amp = False

for string in string_section:
    if string == ('Definition of'):
        pass
    elif string.isdigit() == True:
        definition.append(string + '\n')
        l_amp = True
    elif l_amp:
        l_amp = False
        pass
    elif False:
        #this is for putting ---word--- around the definition
        #definition.append(string)
        pass
    else:
        definition.append(string)

print(definition)
#why does it just print out a memory address
#print([string_section])





