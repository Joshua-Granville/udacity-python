import os

def rename_files():
    # get all file names
    file_list = os.listdir(r"c:\git\udacity-python\secret-message\prank\prank")
    print (file_list)
    
    saved_path = os.getcwd()
    os.chdir (r"c:\git\udacity-python\secret-message\prank\prank")

    to_remove = "0123456789"
    table = str.maketrans("", "", to_remove)
    
    #rename each file
    for file in file_list:
        print("Old Name - "+file)
        print("New Name - "+file.translate(table))
        os.rename(file, file.translate(table))

    os.chdir(saved_path)
    
rename_files()

