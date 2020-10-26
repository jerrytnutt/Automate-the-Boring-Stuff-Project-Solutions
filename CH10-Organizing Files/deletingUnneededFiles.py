# Program walks through a folder tree for exceptionally large files/folders, Size > 100MB
# Print these files with their absolute path to the screen
import shutil, os

# Use os.walk to walk the file folder tree
for folderName, subfolders, filenames in os.walk(PATH):
    print('Current Folder: ' + folderName)

    for subfolder in subfolders:
        pass

    for filename in filenames:
      # Create path for current file
      movingFile = os.path.join(folderName,filename)

      size = os.path.getsize(movingFile)
      # os.path.getsize gives the values in bytes
      # The size must therefore exceed 104,857,600 to be greater than 100MB
      if size > 104,857,600:
          print('File with path {} has a size {} Exceeding 100MB'.format(movingFile,size))
          

    

