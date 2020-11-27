import pyxhook as ph





def OnKeyPress(event):
    print(event.Key)


hm = ph.HookManager()
hm.KeyDown = OnKeyPress
hm.HookKeyboard()
hm.start()

