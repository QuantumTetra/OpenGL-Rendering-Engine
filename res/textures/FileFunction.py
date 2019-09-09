import os
import shutil
import getpass
import glob
import string
from os.path import exists, join
from os import pathsep


def RepresentsInt(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def moveFilePrompt():
    user = getpass.getuser()
    src_name = input("What is the name of the source directory: ")
    src = ""
    if __name__ == '__main__':
        for item in findDirsWithName(r'C:\\Users\\charl\\Desktop\\', src_name):
            src = item
    if(src == ""):
        src = input("Source could not be found, please provide path: ")

    dest_name = input("What is the name of the source directory: ")
    dest = ""
    if __name__ == '__main__':
        for item in findDirsWithName(r'C:\\Users\\charl\\Desktop\\', dest_name):
            dest = item
    if(dest == ""):
        dest = input("Destination could not be found, please provide path: ")
        
    filetype = input("What file type would you like to move (only the name): ")
    filetype = "*." + filetype
    os.chdir(src)

    file_amount = 0
    for file in glob.glob(filetype):
        file_amount += 1
    print(file_amount)
    
    uin3 = "no"
    uin3 = input("Would you like to move all files of this type: ")
    uin4 = "copy"
    if(uin3 == "yes"):
        uin4 = input("Would you like to copy/move all files of this type: ")
    for file in glob.glob(filetype):
        if(uin3 == "no"):
            uin = input("Would you like to move file \"" + file + "\": ")
            if(uin == "yes"):
                uin2 = input("Would you like to copy or move: ")
                if(uin2 == "copy"):
                    shutil.copy(file, dest)
                elif(uin2 == "move"):
                    shutil.move(file, dest)
        else:
            if(uin4 == "copy"):
                shutil.copy(file, dest)
            elif(uin4 == "move"):
                shutil.move(file, dest)

def copyFile(file, dest):
    shutil.copy(file, dest)

def moveFile(file, dest):
    shutil.move(file, dest)

def createFile(dirs, file_name):
    new_name = str(dirs) + str(file_name)
    try:
        f = open(new_name, "w+")
    except PermissionError:
        print("Permission Denied")
    f.close()

def createFileDialog():
    dir_name = ""
    file_name = ""
    isGood = False
    os.system('cls')
    while not isGood:
        in2 = input("What do you want to name file (include extension): ")
        in3 = input("What directory would you like to put the file in: ")
        os.system('cls')
        val = isDir(in3)
        if val:
            isGood = True
            dir_name = in3
            file_name = in2
        else:
            print("Not a directory, please try again")
    if "/" in dir_name:
        if dir_name[(len(dir_name)-1):] != '/':
            dir_name = str(dir_name) + "/"
    elif "\\" in dir_name:
        if dir_name[(len(dir_name)-1):] != '\\':
            dir_name = str(dir_name) + "\\"
    else:
        dir_name = str(dir_name) + "/"
    val = doesFileExist(str(dir_name) + str(file_name))
    if val:
        print("file already exists")
    else:
        print(dir_name + file_name)
        createFile(dir_name, file_name)
        print("file created")


def createFileDialogStartPoint(dir_name):
    file_name = ""
    isGood = False
    os.system('cls')
    print(dir_name)
    in2 = input("What do you want to name file (include extension): ")
    file_name = in2
    os.system('cls')
    if "/" in dir_name:
        if dir_name[(len(dir_name)-1):] != '/':
            dir_name = str(dir_name) + "/"
    elif "\\" in dir_name:
        if dir_name[(len(dir_name)-1):] != '\\':
            dir_name = str(dir_name) + "\\"
    else:
        dir_name = str(dir_name) + "/"
    val = doesFileExist(str(dir_name) + str(file_name))
    if val:
        print("file already exists")
    else:
        createFile(dir_name, file_name)
        print("[INFO]: FILE CREATED:", dir_name + file_name)


def writeListToFile(file_name, lists):
    f = open(file_name, "w")
    for item in lists:
        f.write(str(item))
        f.write("\n")
    f.close()

def readStringListFromFile(file):
    ## r - read, w - write, a - append, r+ - read/write
    lists = []
    data = open(file, "r")
    for line in data:
        lists.append(line)
    data.close()
    return lists

def isDir(dir_name):
    return os.path.isdir(dir_name)

def doesFileExist(file_dir):
    return os.path.exists(file_dir)

def findDirsWithName(head_dir, dir_name):
    """Return a list of the full paths of the subdirectories
    under directory 'head_dir' named 'dir_name'"""
    dirList = []
    denied = False
    try:
        os.listdir(head_dir)
    except OSError:
        denied = True
        print("access denied",head_dir)
    if not denied:
        for fn in os.listdir(head_dir):
            dirfile = os.path.join(head_dir, fn)
            if os.path.isdir(dirfile):
                if fn.upper() == dir_name.upper():
                    dirList.append(dirfile)
                    #print(dirfile)
                else:
                    # print "Accessing directory %s" % dirfile
                    dirList += findDirsWithName(dirfile, dir_name)
    return dirList

def search_file(filename, search_path):
    file_found = 0
    paths = string.split(search_path, pathsep)
    for path in paths:
        if exists(join(path, filename)):
            file_found = 1
            break
    if file_found:
        return abspath(join(path, filename))
    else:
        return None
    if __name__ == '___main__':
        search_path = '/bin' + pathsep + '/usr/bin'  # ; on windows, : on unix
        find_file = search_file('ls',search_path)
        if find_file:
            print("File found at %s" % find_file)
        else:
            print("File not found")

def findFileWithName(head_dir, file_name):
    return search_file(file_name, head_dir)

def deleteFile(file_dir):
    good = True
    try:
        os.remove(file_dir)
    except OSError:
        good = False
        print("[ERROR]: ACCESS DENIED")
    if good:
        print("[INFO]: FILE DELETED:", file_dir)

def deleteFolder(file_dir):
    good = True
    try:
        os.rmdir(file_dir)
    except OSError:
        good = False
        print("[ERROR]: ACCESS DENIED")
    if good:
        print("[INFO]: DIRECTORY DELETED:", file_dir)

def createFolder(dir_name):
    good = True
    try:
        os.mkdir(dir_name)
    except OSError:
        good = False
        print("[ERROR]: ERROR")
    if good:
        print("[INFO]: DIRECTORY CREATED:", dir_name)

def executeProgram(file_name):
    good = True
    try:
        #args = [""]
        #os.execv(file_name, args)
        exec(open(file_name).read())
    except OSError and SyntaxError:
        good = False
        print("[ERROR]: ERROR")
    if good:
        os.system("cls")
        print("[INFO]: PROGRAM EXECUTED:", file_name)

def textFileExplorer(head_dir):
    copy = []
    cut = []
    if head_dir.find("\\") != -1:
        head_dir.replace("\\", "/")
    cur_dir = head_dir
    quit_bool = False
    try:
        os.listdir(head_dir)
    except OSError:
        quit_bool = True
        print("[ERROR]: ACCESS DENIED:",head_dir)
        print(OSError)
    os.system('cls')
    boarder = "================================================================"
    p = len(boarder)
    while not quit_bool:
        lista = os.listdir(cur_dir)
        x = 1
        print(boarder)
        o = ""
        for y in range(0, p - 3 - len(cur_dir)):
            o = o + " "
        o = o + "|"
        print("|",cur_dir + o)
        print(boarder)
        for f in lista:
            typeS = ""
            if os.path.isdir(cur_dir + str(f)):
                typeS = "[DIR]"
            else:
                typeS = "[FIL]"
            if x<10:
                print("(0" + str(x) + ") :", typeS, ":", f)
            else:
                print("(" + str(x) + ") :", typeS, ":", f)
            x+=1
        print(boarder)
        print("| q = quit | .. = back | c [name] = create file | d # = delete |")
        print("| cd # = choose directory | mkdir [name] = make dir| r # = run |")
        print("| o # = open file | co # = copy | cu # = cut | p co/cu = paste |")
        print("================================================================")
        ins1 = input(": ")
        os.system('cls')
        if ins1 == "q":
            return ""
        elif ins1[:2] == "co" and RepresentsInt(ins1[2:]):
            ins1 = int(ins1[2:])
            if ins1 > 0 and ins1 < x:
                y = ins1 - 1
                if os.path.isdir(cur_dir + str(lista[y])):
                    print("[ERROR]: CHOICE IS DIRECTORY")
                else:
                    if (cur_dir + str(lista[y])) in copy:
                        print("[WARN]: ITEM ALREADY IN COPY BOARD")
                    elif not (cur_dir + str(lista[y])) in cut:
                        copy.append(cur_dir + str(lista[y]))
                    else:
                        print("[WARN]: ITEM ALREADY IN CUT BOARD")
        elif ins1[:2] == "cu" and RepresentsInt(ins1[2:]):
            ins1 = int(ins1[2:])
            if ins1 > 0 and ins1 < x:
                y = ins1 - 1
                if os.path.isdir(cur_dir + str(lista[y])):
                    print("[ERROR]: CHOICE IS DIRECTORY")
                else:
                    if (cur_dir + str(lista[y])) in cut:
                        print("[WARN]: ITEM ALREADY IN CUT BOARD")
                    elif not (cur_dir + str(lista[y])) in copy:
                        cut.append(cur_dir + str(lista[y]))
                    else:
                        print("[WARN]: ITEM ALREADY IN COPY BOARD")
        elif ins1[:2] == "p " and (ins1[2:] == "cu" or ins1[2:] == "co"):
            print(cur_dir)
            if ins1[2:] == "cu":
                print(cut)
                for item in cut:
                    moveFile(item, cur_dir)
                cut.clear()
            elif ins1[2:] == "co":
                print(copy)
                for item in copy:
                    copyFile(item, cur_dir)
                copy.clear()
        elif ins1[:2] == "c ":
            #createFileDialogStartPoint(cur_dir)
            fm = ins1[2:]
            val = doesFileExist(str(cur_dir) + str(fm))
            if val:
                print("[WARN]: FILE ALREADY EXISTS")
            else:
                createFile(cur_dir, fm)
                print("[INFO]: FILE CREATED:", cur_dir + fm)
        elif ins1[:2] == "d " and RepresentsInt(ins1[2:]):
            ins1 = int(ins1[2:])
            if ins1 > 0 and ins1 < x:
                y = ins1 - 1
                if os.path.isdir(cur_dir + str(lista[y])):
                    deleteFolder(cur_dir + str(lista[y]))
                else:
                    deleteFile(cur_dir + str(lista[y]))
            else:
                print("[ERROR]: NOT AN OPTION")
        elif ins1[:2] == "r " and RepresentsInt(ins1[2:]):
            ins1 = int(ins1[2:])
            if ins1 > 0 and ins1 < x:
                y = ins1 - 1
                if os.path.isdir(cur_dir + str(lista[y])):
                    print("[ERROR]: CHOICE IS DIRECTORY")
                else:
                    executeProgram(cur_dir + str(lista[y]))
            else:
                print("[ERROR]: NOT AN OPTION")
        elif ins1[:2] == "o " and RepresentsInt(ins1[2:]):
            ins1 = int(ins1[2:])
            if ins1 > 0 and ins1 < x:
                y = ins1 - 1
                if os.path.isdir(cur_dir + str(lista[y])):
                    print("[ERROR]: CHOICE IS DIRECTORY")
                else:
                    os.system("cls")
                    fileL = open(cur_dir + str(lista[y]))
                    try:
                        for line in fileL:
                            print(line, end = "")
                    except UnicodeDecodeError:
                        print("[ERROR]: WELP")
                    n = input()
                    fileL.close()
                    os.system("cls")
            else:
                print("[ERROR]: NOT AN OPTION")
        elif ins1 == "..":
            test_dir = cur_dir[::-1]
            ind1 = test_dir.find("/")
            ind2 = (test_dir[(ind1+1):].find("/"))
            test_dir = (test_dir[(ind2+1):])[::-1]
            good = True
            try:
                os.listdir(test_dir)
            except OSError:
                print("[ERROR]: ACCESS DENIED:",test_dir)
                good = False
            if good:
                cur_dir = test_dir
        elif ins1[:6] == "mkdir ":
            createFolder(cur_dir + ins1[6:])
            #print(ins1[6:])
        elif ins1[:3] == "cd " and RepresentsInt(ins1[3:]):
            ins1 = int(ins1[3:])
            if ins1 > 0 and ins1 < x:
                y = ins1 - 1
                if os.path.isdir(cur_dir + str(lista[y])):
                    good = True
                    try:
                        os.listdir(cur_dir + str(lista[y]) + "/")
                    except OSError:
                        print("[ERROR]: ACCESS DENIED:",cur_dir + str(lista[y]) + "/")
                        good = False
                    if good:
                        cur_dir = cur_dir + str(lista[y]) + "/"
                else:
                    return cur_dir + str(lista[y])
            else:
                print("[ERROR]: NOT AN OPTION")
        else:
            print("[ERROR]: NOT AN OPTION")
    return ""
        
def textToClipboard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)
