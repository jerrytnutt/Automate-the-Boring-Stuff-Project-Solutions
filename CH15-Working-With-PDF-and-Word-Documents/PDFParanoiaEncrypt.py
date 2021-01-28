# Use os.walk() to find every PDF in a folder and encrypt the PDFs using a password provided on the command line.
# Save each encrypted PDF with a '_encrypted.pdf' suffix. 
# Before deleting the original file, attempt to read and decrypt the file to ensure that it was encrypted

import PyPDF2 
import sys
import os

def encrypt_PDFs():
  if len(sys.argv) == 2:
    path = os.getcwd()
    encrypt_password = sys.argv[1]
    
    for folderName, subfolders, filenames in os.walk(path):
      for subfolder in subfolders:
        pass
      for filename in filenames:
        if filename.endswith('.pdf'):
          absolute_path = folderName+"\\"+filename
          removable_path = absolute_path
          # Open each pdf to append the pages and encrypt to the new file
          with open(absolute_path,'rb') as pdf_file:
            pdfReader = PyPDF2.PdfFileReader(pdf_file)
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfWriter.appendPagesFromReader(pdfReader)
            pdfWriter.encrypt(encrypt_password)
            
            absolute_path = absolute_path[:-4]+"_encrypted.pdf"
            with open(absolute_path,"wb") as encrypted_file:
              pdfWriter.write(encrypted_file)
              
            # Open newly created pdf and check if it was properly encrypted
            with open(absolute_path,"rb") as encrypted_file:
              pdfReader = PyPDF2.PdfFileReader(encrypted_file)
            
              if pdfReader.decrypt(encrypt_password) == 1:
                pass
              else:
                removable_path = 'none'
                print('Sorry, The file was not properly encrypted')
          if removable_path != 'none':
            os.remove(removable_path)
                   
  else:
    print('Please supply a password')

if __name__ == "__main__":
  encrypt_PDFs()






  

    
