# Backing Up a Folder into a ZIP File
# Copy an entire folder and it's contents into a ZIP file
# The ZIP file's filename must increment

import os
import zipfile

# Increment number for zip files 
num = 1

def backupToZip(path):
  global num
  # While loop to check if a zip file has already been created
  while True:
    base_name = os.path.basename(path)
    name = base_name +'_'+str(num)

    # Folder path with the zip file and current num
    zip_path = path+"\\"+name+".zip"
    
    # Num will increment until a zip file with that num does not exist
    if not os.path.exists(zip_path):
      break
    else:
      num = num + 1
  # Create a zip file with current base name and num increment

  with zipfile.ZipFile(zip_path,'w') as new_zip:
    # Use os.walk to walk the folder and all subfolders
    for folders, subfolders, filenames in os.walk(path):
      
      print("You are now in folder: {}".format(folders))
      
      new_zip.write(folders)
      for files in filenames:
        print("You are now in file: {}".format(files))
        
      # Do not zip the previous zip files
        if files.endswith('.zip') and files.startswith(base_name):
          print('skip')
        else:
          new_zip.write(os.path.join(folders, files))
    return path
        
          
backupToZip(r"C:\Users\jerry\Documents\chapter9\autor")