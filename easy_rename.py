import os
from os import path
from termcolor import colored
import ctypes

os.system('cls')


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def clrscr():
    rep = input('Press ENTER to Proceed'.center(120))
    if rep == '':
        os.system('cls')


def printer(x):
    for _ in range(0, x):
        print()


def welcome():
    printer(2)
    print(colored("Welcome To EZ Renamer", 'magenta').center(130))
    printer(3)
    colored("!! Note that if you don't wanna rename the folder just press ENTER when it asks you to rename it !!", 'red')


def GetPath():
    print("paste the path/dir that contains the file(s) that you wanna rename: ")
    path_name=''
    i=0
    while path.exists(path_name)==False:
        if path.exists(path_name)==False and i>0:
            print()
            print()
            print(colored('!!   Error: this path does not exist, Please enter a valid one   !!','red'))
            Mbox('Error ', "this path does not exist, Please enter a valid one", 1)
        print()
        print()
        print()
        path_name=input('enter path here:  ')
        
        i+=1
    return path_name
    


def PrintList(list):
    i = 1
    for x in list:
        if i > 9:
            print(str(i)+'/ ' + colored(str(x), 'red'))
        else:
            print('0'+str(i)+'/ ' + colored(str(x), 'red'))
        i += 1


def GetExtension(name):
    i = -1
    for x in reversed(name):
        if x == '.':
            break
        i += 1
    posp = (len(name)-(i+1))-1
    return name[posp:]


def renamer(list):
    list2 = []
    for i in range(0, len(list)):
        print("what do you wanna call "+colored(list[i], 'red'))
        name2 = input("=>")
        ext = GetExtension(list[i])
        fullname = name2+ext
        while fullname in list2:
            print(
                colored("This Name already exists in another file, enter another name"), 'red')
            name2 = input("=>")
            fullname = name2+ext
        if not (name2 == ''):
            os.rename(list[i], fullname)
            list2.append(fullname)
        os.system('cls')

def Done():
    os.system('cls')
    printer(4)
    print(colored("Everything went perfect.. ", 'red'))
    Mbox('task succeeded ', "the process completed successfully", 1)


##Callers##
welcome()

path = GetPath()
os.chdir(path)
list = os.listdir(path)
os.system('cls')
renamer(list)
Done()
