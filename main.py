from keylog import OnKeyPress as kp
import htmlparse as hp 
import pyperclip as pc
import webbrowser as wb

class Dict:
    url = 'https://www.merriam-webster.com/dictionary/' 
    word = ''
    
    def paste():
        word = pc.paste()
        return word
    
    
    def openDict():
        if kp == True:
            url = 'https://www.merriam-webster.com/dictionary/' + paste() 
            # opens up the url in a web browser
            wb.open_new(url)
            # calls the html parse function
            hp.wordLogger()


