# Selective Copy 
# Program that walks a folder tree and searches certain file extension (such as .pdf or .jpg) 
# Copy these files from whatever location they are in to a new folder

import shutil, os

old_location = path
new_location = path
extension = '.pdf'


for foldername, subfolders, filenames in os.walk(old_location):
    print('The current folder is ' + foldername)

    for subfolder in subfolders:
        pass
    for filename in filenames:
      print(filename)
        # Check the chosen extension for the current filename
        # if there is a match use shutil.copy to move the files
      if filename.endswith(extension):
         
        moving_file = os.path.join(foldername,filename)
        
        shutil.copy(moving_file,new_location)

    

