# Backing Up a Folder into a ZIP File
# Copy an entire folder and it's contents into a ZIP file
# The ZIP file's filename must increment

import os
import zipfile

def backup_to_zip(path):
  num = 1
  # While loop to check if a zip file has already been created
  while True:
   
    base_name = os.path.basename(path)
    file_name = base_name +'_'+str(num)

    zip_path = path+"\\"+file_name+".zip"
    
    # Num will increment until a zip file with that num does not exist
    if not os.path.exists(zip_path):
      break
    else:
      num = num + 1
  with zipfile.ZipFile(zip_path,'w') as new_zip:
    
    for folders, subfolders, filenames in os.walk(path):
      print("You are now in folder: {}".format(folders))
      new_zip.write(folders)

      for files in filenames:
        print("You are now in file: {}".format(files))
        
      # Do not zip the previous zip files
        if files.endswith('.zip') and files.startswith(base_name):
          pass
        else:
          new_zip.write(os.path.join(folders, files))
    return path
        
if __name__ == '__main__':         
  backup_to_zip(path)