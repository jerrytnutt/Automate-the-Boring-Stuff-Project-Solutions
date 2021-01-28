# Write a program that will decrypt the PDF by trying every possible English word until it finds one that works. 
# Try both uppercase and lowercase forms of each word.
# Loop over each word in this list, passing it to the decrypt() method. 

import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader 

def brute_force_password():
  num = 0; 
  with open("encrypted.pdf","rb") as ch:
    pdfReader = PyPDF2.PdfFileReader(ch)
    with open('dictionary.txt') as f:
      lines = f.readlines()
      length_lines = len(lines)
      while num < length_lines:
        # Attempt to decrypt with both lower and uppercase version of word
        pass_upper = lines[num].strip()
        pass_lower = lines[num].lower().strip()
        if pdfReader.decrypt(pass_upper) == 1:
          print("The corect password is {}".format(pass_upper))
          break
        elif pdfReader.decrypt(pass_lower) == 1:
          print("The corect password is {}".format(pass_lower))
          break
        else:
          pass
        num += 1

if __name__ == "__main__":
  brute_force_password()
