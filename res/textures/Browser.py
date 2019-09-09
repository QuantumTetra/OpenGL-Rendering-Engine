from FileFunction import textToClipboard
from FileFunction import textFileExplorer
from FileFunction import writeListToFile
import getpass
import os

## Charles Jones
## This program just recompiles the master list because it was
## easier to write it in python

## python, the programming language that is ONLY good for dealing with files

dir_path = os.path.dirname(os.path.realpath(__file__))

#print(dir_path)

lists = os.listdir(dir_path)

lists2 = []

print(lists)

for item in lists:
    if len(item) >= 5:
        if item[len(item)-4:] == ".png" and item[3:4] == "_":
            lists2.append("file_name=" + item)

print(lists2)

writeListToFile(dir_path + "/Material_Master_List.txt", lists2)

input("good?")
