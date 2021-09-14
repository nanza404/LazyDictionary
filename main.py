from keylog import OnKeyPress as kp
#import keylog.py as kp
import pyperclip as pc
import webbrowser as wb

class Dict:
    global url
    global word    
    
    def paste():
        #paste should be an input from a different file
        word = pc.paste()
    
    
    def openDict():
        if kp == True:
            url = 'https://www.merriam-webster.com/dictionary/' + word 
            wb.open_new(url)
            wordLogger()
    
    
    
