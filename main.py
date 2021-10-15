import htmlparse as hp 
import pyxhook as ph
import pyperclip as pc
import webbrowser as wb

class Dict:
    url = ''

    def paste():
        word = pc.paste()
        return word
    
    def sendUrl():
        # sets url
        url = 'https://www.merriam-webster.com/dictionary/' + Dict.paste() 
        return url
    
    def openDict():
        # opens up the url in a web browser
        wb.open_new(Dict.sendUrl())
        hp.parse()

        ## if invalid word is entered it is not written to dictionary
        #if hp.errorHandle():
        #    # calls the html parse function
        #    hp.parse()


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

