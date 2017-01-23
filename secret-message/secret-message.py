import os

def rename_files():
    # get all file names
    file_list = os.listdir(r"c:\git\udacity-python\secret-message\prank\prank")
    print (file_list)

    #rename each file
    for file in file_list:
        os.rename(file, file.translate("0123456789"))

rename_files()
