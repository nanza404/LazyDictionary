import htmlparse as hp 
import pyxhook as ph
import pyperclip as pc
import webbrowser as wb

class Dict:
    url = 'https://www.merriam-webster.com/dictionary/' 
    word = ''
    
    def paste():
        word = pc.paste()
        return word
    
    
    def openDict():
        url = 'https://www.merriam-webster.com/dictionary/' + Dict.paste() 
        # opens up the url in a web browser
        wb.open_new(url)
        # calls the html parse function
        hp.getDefinition()


class keyLog:

    #Keylogger(pyxhook)
    # logs users key strokes waiting for trigger input
    def OnKeyPress(event):
        # registers when F1 is pressed
        if event.Key == 'F1':
            Dict.openDict()

    def keyLogStart():
        hm = ph.HookManager()
        hm.KeyDown = keyLog.OnKeyPress
        hm.HookKeyboard()
        hm.start()


# starts logging keys
keyLog.keyLogStart()

