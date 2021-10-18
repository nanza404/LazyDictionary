import htmlparse as hp 
import pyxhook as ph
import pyperclip as pc
import webbrowser as wb

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

#Keylogger(pyxhook)
# logs users key strokes waiting for trigger input
def OnKeyPress(event):
    # registers when F1 is pressed
    if event.Key == 'F1':
        Dict.openDict()

def keyLogger():
    global hm
    hm = ph.HookManager()
    hm.KeyDown = keyLog.OnKeyPress
    hm.HookKeyboard()
    #hm.start()

def start():
    hm.start()

def end():
    hm.cancel()
