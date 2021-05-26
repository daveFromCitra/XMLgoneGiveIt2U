#           
#           __   ____  __ _                             _____ _           _____ _   ___  _    _ 
#           \ \ / /  \/  | |                           / ____(_)         |_   _| | |__ \| |  | |
#            \ V /| \  / | |     __ _  ___  _ __   ___| |  __ ___   _____  | | | |_   ) | |  | |
#             > < | |\/| | |    / _` |/ _ \| '_ \ / _ \ | |_ | \ \ / / _ \ | | | __| / /| |  | |
#            / . \| |  | | |___| (_| | (_) | | | |  __/ |__| | |\ V /  __/_| |_| |_ / /_| |__| |
#           /_/ \_\_|  |_|______\__, |\___/|_| |_|\___|\_____|_| \_/ \___|_____|\__|____|\____/ 
#                                __/ |                                                          
#                               |___/        
#                           Knock knock open up the door it's real!
#
#
#   Dave Blois
#   Version 1.0
# This is designed to be a pretty basic bulk XML editor
import os
import shutil
import tkinter
import csv
import re
import math

from tkinter import filedialog
from tkinter import *

window = Tk()
window.title("TechStyles File Renamer Pro")
window.geometry('400x250')
window.configure()

def fileCheck(dirCheck):
    for file in os.listdir(dirCheck):
        #is it an xml file?
        if file.endswith('.xml'):
            
        else:
            print("nah")

def folderPath():
    window.foldername =  filedialog.askdirectory()
    global dirSel
    dirSel = window.foldername

def submitter():
    fileCheck(dirSel)

infoLabel = Label(window, text="Add your Print files, InfoTech files and csv files to a folder")
infoLabel2 = Label(window, text="Press Submit. Profit")
infoLabel3 = Label(window, text="")

infoLabel.grid(column=1, row=1)
infoLabel.configure()
infoLabel2.grid(column=1, row=2)
infoLabel2.configure()
infoLabel3.grid(column=1, row=3)
infoLabel3.configure()
uploader = Button(window, text="Select Folder",  fg='black', bg='white', command=folderPath)
uploader.grid(column=1, row=4)
submitButton = Button(window, text=" - Submit - ", command=submitter, fg='black', bg='#6a3d58')
submitButton.grid(column=1, row=5)
#txtConsole = Text(window)
#txtConsole.grid(column=1, row=5)

window.mainloop()
