# Program that finds all files with a given prefix (spam001.txt, spam002.txt) 
# Locates any gaps in the numbering and renames all later files to close this gap
# Write another program that inserts gaps into numbered files so that a new file can be added.

import os
# Add a path for the files to be searched in
directoryPath = ENTER_PATH

def locateGaps(directoryPath):
  currentNum = 1
  for filename in os.listdir(directoryPath):
    # Check if the file contains the correct next increment number
    if filename.find(str(currentNum)) != -1:
    # Grab the location of the currentNum  within the file
      index = filename.index(str(currentNum))
      currentNum = currentNum + 1
    else:
      oldPath = os.path.join(directoryPath,filename)
      # Give the file with the incorrect number the currentNum integer
      filename = filename[:index] + str(currentNum) + filename[index + 1:]
      # After the file is given currentNum the file is now in order and will be renamed
      currentNum = currentNum + 1
      newPath = os.path.join(directoryPath,filename)
      os.rename(oldPath,newPath)


def createGap(directoryPath,currentNum):
  # CurrentNum will be where you want the gap to be added
  reverseList = []
  for filename in os.listdir(directoryPath):
    # Append all files after the file containing currentNum 
    if filename.find(str(currentNum)) != -1:
        index = filename.index(str(currentNum))
        currentNum = currentNum + 1
        reverseList.append(str(index) + filename)
  for filename in reversed(reverseList):
    # Loop all files in reverse so no current existing files will be overwritten causing an error
    oldPath = os.path.join(directoryPath,filename[1:])
    index = int(filename[0]) + 1
    filename = filename[1:index] + str(int(filename[index]) + 1) + filename[index + 1:]
    newPath = os.path.join(directoryPath,filename)
    #os.rename(oldPath,newPath)
    

