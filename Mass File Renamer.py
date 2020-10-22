import os
import sys
os.system("mode con cols=80 lines=20")
def fileRenamer():
    print(" Mass File Renamer ".center(80, '#'))
folderDir = input("Folder Directory:")
fileName = input("New File Name:")
os.chdir(folderDir)
i = 1
for file in os.listdir():
    src = file
oldext = os.path.splitext(file)[1]
dst = fileName + str(i) + oldext
os.rename(src, dst)
i += 1
answer = input("\nFinished! \nWant To Rename Other Files? (y/n):")
if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
    os.system('cls'
        if os.name == 'nt'
        else 'clear')
fileRenamer()
if answer in ['n', 'N', 'no', 'No', 'NO']:
    exit()



fileRenamer()
