# Selective Copy - Program that walks a folder tree and searches certain file extension (such as .pdf or .jpg) 
# Copy these files from whatever location they are in to a new folder


import shutil, os

# Choose new location to move the files
new_Location = PATH

# Use os.walk to walk the file folder tree
for folderName, subfolders, filenames in os.walk(PATH):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        pass

    for filename in filenames:
        # Check the chosen extension for the current filename
        # if there is a match use shutil.copy to move the files
        if filename.endswith('.pdf'):
            movingFile = os.path.join(folderName,filename)
            shutil.copy(movingFile,new_Location)

    

