import os
from shutil import move
import jlkutils
apikey = input("Gib deinen PyPi Api Key ein: ")
author = input("Dein Voller Name (Wenn dieser offentlich sein soll): ")
name = input("Wie soll das Package heißen? ")
opsy = input("Welches Betriebssystem braucht dein Package? (Wenn Egal einfach Enter drücken): ")
description = input("Beschreibe dein Package einfach: ")
print("Wähle dein Package aus.")
def listtostring(liste):
    return ", ".join(liste)
modulepath = jlkutils.choose_file()
if opsy == "":
    opsy = "OS Independent"
packages = input('Welche Packages Werden Benötigt? (Format "package1", "package2") ')
modulepathwin = modulepath.replace("/", "\\")
modulepathlist = modulepathwin.split("\\")
filename = modulepathlist[len(modulepathlist) - 1]
filenamelist = filename.split(".")
filenamenopy = filenamelist[len(filenamelist) - 2]
os.system(f'mkdir {name}')
os.chdir(name)
jlkutils.writenewline("secrets.py", f'apikey = "{apikey}"')
jlkutils.writenewline("secrets.py", f'packages = {packages}')
jlkutils.writenewline("secrets.py", f'name = "{name}"')
jlkutils.writenewline("secrets.py", f'author = "{author}"')
jlkutils.writenewline("secrets.py", f'opsy = "{opsy}"')
jlkutils.writenewline("secrets.py", f'description = "{description}"')
os.system("curl -O https://raw.githubusercontent.com/jkramer5103/easypublish-python/refs/heads/main/setup.py")
os.system("curl -O https://raw.githubusercontent.com/jkramer5103/easypublish-python/refs/heads/main/build.py")
os.system(f"mkdir {name}")
os.chdir(name)
destination_path = os.getcwd()
move(modulepath, destination_path)
commands = jlkutils.getcoms(destination_path + "\\" + filename)
liststring = listtostring(commands)
jlkutils.writetofile("__init__.py", f"from .{filenamenopy} import {liststring}")
#os.system("cls")
print("Um es zu Veröffentlichen, führe einfach nur build.py aus.")
