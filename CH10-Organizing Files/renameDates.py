# Rename Files with American-Style Dates to European-Style Dates
# Search all the filenames in the current working directory for American-style dates.
# Renames the file with date swapped to European-style (MM-DD-YYYY) -> (DD-MM-YYYY)

import os, re, shutil

def change_dates(path):
  # Create list of the file pathway
  dirs = os.listdir(path)
  # Create New folder pathway for the euro dates
  euro_path = path+"\\"+"Eurodates"
  if not os.path.exists(euro_path):
    os.makedirs(euro_path)

  #Create Regex for American-Style dates passing re.VERBOSE for comment space

  pattern = re.compile(""" 
              ([1-9]|[0][0-9]|[1][0-2])\-            # Month int as 1-9 or 2 digit starting with 0 or 1 
                                          
              ([0-9]{1}|[3][0-1]|[0-2][0-9])             # Day identifier with day 31 limit
                                          
              (\-(19|20)\d\d|\-[0-9]{2})          # Years only in the 20th a 21st century 
              """,re.VERBOSE)

  # Loop through the files and begin to search
  for files in dirs:
    print(files)
    matches = pattern.finditer(files)

    for match in matches:
       # Split the match array and rearrange for european style date
      match_split = match[0].split('-')
      match_final = match_split[1]+'-'+match_split[0]+'-'+match_split[2]
      euro_date = files.replace(match[0],match_final)
      # Set the file pathways for the Source and the Destination
    
      original_location = os.path.join(path,files)
       # Create path for eurofolder
      destination = os.path.join(euro_path,euro_date)
      print(original_location)
      print(destination)
     
      # Move the file to their new location with corrected title
      shutil.move(original_location, destination)

if __name__ == "__main__":
  change_dates("PATH")