# This is my attempt at making a Notepad-clone with a dark theme using Python and PySimpleGUI.
# References I've used: "Notepad In Python | PySimpleGUI" guide by Izzy Analytics and the PySimpleGUI Cookbook.
# I have added character- and word-counters that use lists to determine the correct numbers.
# I am Currently in the process of figuring out how to correctly open files with unicode-characters.

import PySimpleGUI as sg
import pathlib

# Setting up the dark theme
sg.theme('Black')
sg.theme_input_background_color("black")
sg.theme_background_color("black")
sg.theme_progress_bar_color("black")

WIN_W = 90
WIN_H = 25
file = None

#Setting up the menu and general layout
menu_layout = [["File", ["New", "Open", "Save", "Save As", "---", "Exit"]],
              ["Tools", ["Character Count", "Word Count"]], ["Help", ["About"]]]

layout = [[sg.Menu(menu_layout)],
         [sg.Text("Default file", font = ("Consolas",10), size = (WIN_W, 1), key = "_INFOKEY_")],
         [sg.Multiline(font = ("Consolas", 12), size = (WIN_W, WIN_H), key = "_BODYKEY_")]]

window = sg.Window("Nightpad", layout = layout, margins = (0,0), resizable = True, finalize = True)
window.maximize()
window["_BODYKEY_"].expand(expand_x = True, expand_y = True)

#Defining functions for the menu options
def new_file():
    window["_BODYKEY_"].update(value = "")
    window["_INFOKEY_"].update(value = "> New File <")
    file = None
    return file

def open_file():
    filename = sg.popup_get_file("Open", no_window = True,)
    if filename:
        file = pathlib.Path(filename)
        window["_BODYKEY_"].update(value = file.read_text())
        window["_INFOKEY_"].update(value = file.absolute())
        return file

def save_file(file):
    if file:
        file.write.text(values.get("_BODYKEY_"))
    else:
        save_file_as()

def save_file_as():
    filename = sg.popup_get_file("Save as", save_as = True, no_window = True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get("_BODYKEY_"))
        window["_INFOKEY_"].update(value = file.absolute())
        return file

#Defining the character/word counter and about me-functions
def character_count():
    characters: list = values["_BODYKEY_"]
    character_count: int = len(characters)
    sg.PopupQuick("Character count: {:,d}".format(character_count))

def word_count():
    words: list = [w for w in values["_BODYKEY_"].split(" ") if w!="\n"]
    word_count: int = len(words)
    sg.PopupQuick("Word Count: {:,d}".format(word_count))

def about_me():
    sg.popup_no_wait("Not a very original app.\nhttps://www.hugoheino.com/")

#Setting up the loop based on the functions above
while True:
    event, values = window.read()

    if event in (None, "Exit"):
        break
    if event in ("New (Ctrl+N)"):
        filename = new_file()
    if event in ("Open (Ctrl+O"):
        filename = open_file()
    if event in ("Save (Ctrl+S"):
        save_file(file)
    if event in ("Save As",):
        filename = save_file_as()
    if event in ("Character Count",):
        character_count()
    if event in ("Word Count",):
        word_count()
    if event in ("About",):
        about_me()
