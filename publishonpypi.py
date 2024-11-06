import os
from shutil import copy
import jlkutils
import platform
apikey = input("Enter your PyPi Api Key: ")
name = input("What should the package be named? ")
opsy = input("Which operating system does your package require? (Press Enter if it doesn't matter): ")
description = input("Briefly describe your package: ")
print("Select your package.")
def listtostring(liste):
    return ", ".join(liste)
modulepath = jlkutils.choose_file()
def convert_input(input_string):
    # Split the input string by commas and strip any leading/trailing whitespace
    items = [item.strip() for item in input_string.split(',')]
    # Format each item with double quotes
    formatted_items = ', '.join([f'"{item}"' for item in items])
    return formatted_items

if opsy == "":
    opsy = "OS Independent"
if platform.system == "Windows":
    modulepathwin = modulepath.replace("/", "\\")
    modulepathlist = modulepathwin.split("\\")
else:
    modulepathlist = modulepathwin.split("/")
filename = modulepathlist[len(modulepathlist) - 1]
filenamelist = filename.split(".")
filenamenopy = filenamelist[len(filenamelist) - 2]
os.system(f'mkdir {name}')
os.chdir(name)
packages = jlkutils.get_imports(modulepath)
jlkutils.writenewline("secrets.py", f'apikey = "{apikey}"')
jlkutils.writenewline("secrets.py", f'packages = {packages}')
jlkutils.writenewline("secrets.py", f'name = "{name}"')
jlkutils.writenewline("secrets.py", f'opsy = "{opsy}"')
jlkutils.writenewline("secrets.py", f'description = "{description}"')
os.system("curl -O https://raw.githubusercontent.com/jkramer5103/easypublish-python/refs/heads/main/setup.py")
os.system("curl -O https://raw.githubusercontent.com/jkramer5103/easypublish-python/refs/heads/main/build.py")
os.system(f"mkdir {name}")
os.chdir(name)
destination_path = os.getcwd()
copy(modulepath, destination_path)
if platform.system() == "Windows":
    commands = jlkutils.getcoms(destination_path + "\\" + filename)
else:
    commands = jlkutils.getcoms(destination_path + "/" + filename)
liststring = listtostring(commands)
jlkutils.writetofile("__init__.py", f"from .{filenamenopy} import {liststring}")
os.system("cls")
print(f"To publish it, just run build.py in the folder called {name}.")
