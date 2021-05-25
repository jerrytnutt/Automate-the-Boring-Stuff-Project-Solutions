# Find all files with a given prefix (spam001.txt, spam002.txt) 
# Locates any gaps in the numbering and rename all later files to close this gap
# Write another program that inserts gaps into numbered files so that a new file can be added.

import os

def locate_gaps(directory_path):
  current_num = 1
  index = 0
  for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
      print(filename)
      # Check if the file contains the correct next increment number
      if filename.find(str(current_num)) != -1:
      # Grab the location of the current_num  within the file
        index = filename.find(str(current_num))
        current_num = current_num + 1
      else :
        old_path = os.path.join(directory_path,filename)
        # Give the file the current_num integer
        filename = filename[:index] + str(current_num) + filename[index + 1:]
        # After the file is given current_num the file is now in order and will be renamed
        current_num = current_num + 1
        new_path = os.path.join(directory_path,filename)
        os.rename(old_path,new_path)
        
def create_gap(directory_path,gap_num):
  files_to_rename = []
  for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
      # Increment and rename all files after reaching gap file
      if filename.find(str(gap_num)) != -1:
        
        old_path = os.path.join(directory_path,filename)
        files_to_rename.append(old_path)
        
        gap_num = gap_num + 1
  for filename in files_to_rename[::-1]:
    gap_num = gap_num - 1
    index = filename.index(str(gap_num))
    new_file = filename[:index] + str(int(filename[index]) + 1) + filename[index + 1:]
    new_path = os.path.join(directory_path,new_file)
    os.rename(filename,new_path)
    
  return directory_path
    
if __name__ == "__main__":
  locate_gaps("PATH")