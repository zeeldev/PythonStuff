"""
Git Tool to add, commit then push multiple files

------------------------------------------------
date           author              description
Feb-2023       Lem                 Initial make (draft/test from Jupyter Notebook)
"""
import os
import shutil
import subprocess


FOLDER = r"c:\temp\for_git_repo" # change if necessary
GIT_PATH = r"C:\dev\workspace\ts-support\TS Solution\support-cases" # change if necessary
GIT_URL = r"https://git.pointclickcare.com/projects/TS/repos/ts-support/browse/TS%20Solution/support-cases/"
for file in os.listdir(FOLDER):
    os.chdir(FOLDER)
    print(file)
    case_name = file.split('_')[0] 
    print('/*=======================================================================')
    print(GIT_URL + case_name)
    print('========================================================================*/')
    comment = file.split('_')[-1:][0].split('.')[0]
    #src = folder + "\\" + "\'" + file + "\'"
    tgt = GIT_PATH + "\\" + case_name
    try:
        os.mkdir(tgt) # create the new folder
    except: pass #don't care if folder already exists    
    try:
        shutil.move(file, tgt) # move the file to the new folder
    except: pass #don't care if file already exists    
    os.chdir(tgt) #now go to the new folder
    subprocess.run(["git", "status"])
    subprocess.run(["git", "add", "./"])
    subprocess.run(["git", "status"])
    subprocess.run(["git", "commit", "-m", comment])
# end of for loop
    
subprocess.run(["git", "pull"])
#add a delay before push?
subprocess.run(["git", "push"])

