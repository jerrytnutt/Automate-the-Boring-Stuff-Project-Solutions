# Rename Files with American-Style Dates to European-Style Dates
# Search all the filenames in the current working directory for American-style dates.
# Renames the file with date swapped to European-style (MM-DD-YYYY) -> (DD-MM-YYYY)

import os, sys, re
import shutil

# Create path for current working directory
path = os.getcwd()
# Create list of the file pathway
dirs = os.listdir(path)
# Create New folder pathway for the euro dates
euroPath = path+"\\"+"Eurodates"

#Create Regex for American-Style dates passing re.VERBOSE for comment space

pattern = re.compile(""" 
            ([1-9]|[0][0-9]|[1][0-2])\-            # Month int as 1-9 or 2 digit starting with 0 or 1 
                                          
            ([0-9]{1}|[3][0-1]|[0-2][0-9])             # Day identifier with day 31 limit
                                          
            (\-(19|20)\d\d|\-[0-9]{2})          # Years only in the 20th a 21st century 
            """,re.VERBOSE)

# Loop through the files and begin to search
for files in dirs:
   matches = pattern.finditer(files)
   # loop through files that matches regex
   for match in matches:
     # Split the match array and rearrange for european style date
     matchSplit = match[0].split('-')
     matchFinal = matchSplit[1]+'-'+matchSplit[0]+'-'+matchSplit[2]
     euroDate = files.replace(match[0],matchFinal)
     # Set the file pathways for the Source and the Destination
     sourceP = path+"\\"+files
     # Create path for eurofolder
     destinationP = euroPath+"\\"+euroDate
     
     # Move the file to their new location with corrected title
     shutil.move(set1, set2)


     
     

  