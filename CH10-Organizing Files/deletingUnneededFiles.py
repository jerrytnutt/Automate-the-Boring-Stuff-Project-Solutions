# Deleting Unneeded Files
# Walks through a folder tree looking for exceptionally large files/folders, Size > 100MB
# Print these files with their absolute path to the screen

import shutil, os

for folderName, subfolders, filenames in os.walk(path):
    print('Current Folder: ' + folderName)
    for subfolder in subfolders:
        pass
    for filename in filenames:
      file_path = os.path.join(folderName,filename)
      file_size = os.path.getsize(file_path)
      # os.path.getsize gives the values in bytes
      # The size must therefore exceed 104,857,600 to be greater than 100MB
      if file_size > 104_857_600:
        print('File with path {} has a size {} Exceeding 100MB'.format(file_path,file_size))
          

    

