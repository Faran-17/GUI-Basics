import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello welcome to my main window ")
mainWindow.geometry('900x600-8-200')

label = tkinter.Label(mainWindow, text="Hello world")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=2, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=5)
canvas.grid(row=1, column=1)

# button4 = tkinter.Button(leftFrame, text="Button4")
# button4.grid(row=1, column=1)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")

button1.grid(row=0, column=0, sticky='ew')
button2.grid(row=1, column=0, sticky='ew')
button3.grid(row=2, column=0, sticky='ew')

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=2)
rightFrame.config(relief='sunken', borderwidth=2)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')
rightFrame.columnconfigure(0, weight=2)
button2.grid(sticky='ew')

mainWindow.mainloop()