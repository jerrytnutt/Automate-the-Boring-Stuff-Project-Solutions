# Selective Copy 
# Walk a folder tree and searches certain file extension (such as .pdf or .jpg) 
# Copy these files into a new folder

import shutil, os

old_location = "Path to old folder"
new_location = "Path to new location"
extension = '.pdf'

for foldername, subfolders, filenames in os.walk(old_location):
    print('The current folder is ' + foldername)
    for subfolder in subfolders:
        pass
    for filename in filenames:
        # Check the chosen extension for the current filename
        # if there is a match use shutil.copy to move the files
      if filename.endswith(extension):
        moving_file = os.path.join(foldername,filename)
        shutil.copy(moving_file,new_location)