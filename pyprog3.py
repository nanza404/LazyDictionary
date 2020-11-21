import keyboard as kb
import webbrowser as wb
import os
import sys
#import subprocess

userid = os.geteuid()
url = 'https://www.merriam-webster.com/'
te = True

#if block may need to just contain break
#if os.geteuid() == 0:
#    print("We're root!")
#else:
#    print("We're not root.")
#    subprocess.call(['sudo', 'python3', *sys.argv])
#    sys.exit()

#alternative to above code
#TODO: see if you can make this a linux system box that pops up
if os.geteuid() != 0:
    os.execvp('sudo', ['sudo', 'python3'] + sys.argv)

#takes last selcted item in clip board and searches merriam webster dictionary with it
def clipsrch():
    print('')

def openwb():
    os.seteuid(userid)
    wb.open_new(url)
    te = False

#detects the pressing of the d key
#TODO: while okular is the currently selected window
while te:
    kb.add_hotkey('d', openwb, suppress=True, timeout=2)







