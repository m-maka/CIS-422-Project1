from tkinter import filedialog
from tkinter import *

#User uploads file using tkinter for user interface
def openFile():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "Select file",filetypes = (("gpx files","*.gpx"),("all files","*.*")))
    return root.filename

def main():
    openFile()

if __name__ == '__main__':
    main()

    
