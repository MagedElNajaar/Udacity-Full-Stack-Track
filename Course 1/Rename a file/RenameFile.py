#we try to rename a files and delete number from it
#download this file https://s3.amazonaws.com/udacity-hosted-downloads/ud036/prank.zip
#unzip this file

import os

def rename_file():
    #(1)get file names from a folder
    #put the Directory of your prank file
    file_list = os.listdir(r"E:\WORK&STUDY\project\Udicty FULL STACK\Course 1\Rename_file\prank")
    saved_path = os.getcwd()
    print("Current Working Director is "+saved_path)
    os.chdir(r"E:\WORK&STUDY\project\Udicty FULL STACK\Course 1\Rename_file\prank")
    #(2)for each file, rename filename
    for file_name in file_list:
        print("old Name - "+file_name)
        print("New Name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    
rename_file()
