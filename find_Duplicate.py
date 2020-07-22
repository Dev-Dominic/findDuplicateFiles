#   this project aims to:
#       find all duplicate files in the downloads folder
#       move all duplicate files to the "folder_of_duplicate_files" folder
#       the user must then look at each duplicate file found and determine what to delete 

import filecmp
import os
import shutil

def move_duplicate():
    
    files = os.listdir(path)
    num_of_files = len(files)
    num_duplicates = 0
    
    for main_comp in range(num_of_files):
      
        file1 = path + "\\" + files[main_comp]
        sec_comp = main_comp + 1

        for start in range(num_of_files - sec_comp):

            file2 = path + "\\" + files[sec_comp] 
            compare = filecmp.cmp(file1, file2, shallow = False)
            
            if  compare:            
                print(files[main_comp] + " duplicates: " + files[sec_comp])
                num_duplicates += 1
                shutil.move(file1, path + "\\folder_of_duplicate_files")
                break
              

    return "\n" + str(num_duplicates) + " duplicates found"

path = input("Enter path to search: ")

if os.path.isdir(path + "\\folder_of_duplicate_files"):
    print("\nSee folder_of_duplicate_files for possible duplicates.\n")
    print(move_duplicate())
else: 
    try:
        os.mkdir(path + "\\folder_of_duplicate_files")
    except OSError:
        print("\nInvalid path added.")
        print("Here's an example: 'C:\\Users\\John Brown\\Downloads'\n")
    else:
        print("\nA new folder called: folder_of_duplicate_files has been created\n")
        print(move_duplicate())




    
