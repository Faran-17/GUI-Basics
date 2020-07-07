import tkinter
import os  # to import the data for list directly form OS

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo ")
mainWindow.geometry('900x600-8-200')
mainWindow['padx'] = 10              # Will give extra space in leftmost area of the window

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=2, columnspan=2)  # column span helps the title to expand in multiple columns

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)  # column configure
mainWindow.columnconfigure(3, weight=3)  # adjusting weights
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)  # row configure
mainWindow.rowconfigure(3, weight=3)  # adjusting weights
mainWindow.rowconfigure(4, weight=3)

mainWindow.configure(bg='light grey')      # background color

# ListBox
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)  # rowspan same as column span
fileList.config(border=2, relief='sunken')

# To fill data in the list
for zone in os.listdir('/Windows/System32'):  # standard path for windows
    fileList.insert(tkinter.END, zone)

# Scrollbar    # orient command for positioning of scroll bar and yview means y-axis
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set  # To set the scrollbar

# frame for file details radio buttons  # labelframe for labelling the frame
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=1, sticky='ne')
rbValue = tkinter.IntVar()  # To select only one radio button at a time

# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Time Stamo", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=2, column=0, sticky='w')
radio3.grid(row=3, column=0, sticky='w')

# Result
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
# Result Dialogue Box
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for time
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')
# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0, 24)))  # 0 to 23
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to_=59)  # accurate from 0 to 59
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to_=59)  # _ because from is already a function
# adding spinner to time frame
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=":").grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=":").grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36  # To locate the spin boxes to center inside a widget or frame

# Frame for date
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# Date labels
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
# Adding Date labels to Frame
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='')
yearLabel.grid(row=0, column=2, sticky='')
# Date Spinner
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to_=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5,
                            values=("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept",
                                    "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=1900, to_=2099)
# Adding spinner to Date Frame
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# OK and Cancel Buttons
okButton = tkinter.Button(mainWindow, text="OK")                                       # destroy should not have ()
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)  # enables the function of cancel
# Adding button on grid
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

print(rbValue.get())
