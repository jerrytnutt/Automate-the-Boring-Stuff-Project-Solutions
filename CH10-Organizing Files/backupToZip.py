# backupToZip.py - Copies an entire folder and its contents into a ZIP file
# The ZIP file's filename must increment
import os
import zipfile


# Increment number for zip files 
num = 1

def backupToZip(path):
  global num
  # While loop to check if a zip file has already been created
  while True:
    baseName = os.path.basename(path)
    name = baseName +'_'+str(num)
    # Folder path with the zip file and current num
    zipPath = folderPath+"\\"+name+".zip"
    
    # Num will increment until a zip file with that num does not exist
    if not os.path.exists(zipPath):
      
      break
    else:
      num = num + 1
  # Create a zip file with current base name and num increment
  with zipfile.ZipFile(name+'.zip','w') as mzip:
    # Use os.walk to walk the folder and all subfolders
    for root,dirs,files in os.walk(path):
      for folders in dirs:
      for filenames in files:
        # Do not zip the previous zip files
        if filenames.endswith('.zip') and filenames.startswith(baseName):
          print(filenames.startswith(baseName))
          
        else:
          
          # Join the files to their root and write
          mzip.write(os.path.join(root,filenames))
          
          
          
 
  
  


backupToZip(FOLDERPATH)