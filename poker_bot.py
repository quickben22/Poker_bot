from tkinter import *
import win32gui

toplist, winlist = [], []
def enum_cb(hwnd, results):
   winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


def start():
    try:
        win32gui.EnumWindows(enum_cb, toplist)
        hwnd = [(hwnd, title) for hwnd, title in winlist if e1.get() in title.lower()]
        # just grab the hwnd for first window matching
        hwnd = hwnd[0]
    except:
        print ("Oops!  That was no valid input.  Try again...")

master = Tk()
master.title("Poker BOT - Jacky")
Label(master, text="Ime prozora").grid(row=1,column=1)


e1 = Entry(master)
e1.insert(0,'$')

e1.grid(row=1, column=2)


Button(master, text='Start', command=start).grid(row=3, column=2, sticky=W, pady=4)


ws = master.winfo_screenwidth()#This value is the width of the screen
hs = master.winfo_screenheight()#This is the height of the screen

w = 400 #The value of the width
h = 100 #The value of the height of the window

master.geometry('%dx%d+%d+%d' % (w, h, ws-w-20, 0))

mainloop( )
