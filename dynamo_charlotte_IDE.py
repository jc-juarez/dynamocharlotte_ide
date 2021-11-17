from tkinter import *
import sys
import dynamocharlotte as dc

window = Tk()
window.title("Dynamo Charlotte IDE")

def runMyCode():
    code = textEditor.get('1.0', END)
    dc.run(code)
    
    
    

textEditor = Text()
textEditor.pack()

menuBar = Menu(window)
runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label = "Run", command = runMyCode)
menuBar.add_cascade(label = "Run", menu = runBar)

window.config(menu = menuBar)
window.mainloop()