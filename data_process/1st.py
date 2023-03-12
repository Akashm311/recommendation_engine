import os
import re
import json
  
# Folder Path
path = r"C:\Users\Akash\Documents\automatad\total"
path1=r"C:\Users\Akash\Documents\automatad\data\total2.json"
  
# Change the directory
os.chdir(path)
  
# Read text File
  
  
def read_text_file(file_path,j):
    with open(file_path, 'r',encoding="utf8") as f:
        a=f.read()
        #result = re.sub("[^\w']", ' ',a)
        #result = re.sub("[^A-Za-z0-9.,!?'’\-]+", ' ', a)
        a = a.replace('\n', ' ')
        # remove tabs
        a = a.replace('\t', ' ')

        
        # remove \u characters
        a = a.encode('ascii', 'ignore').decode('utf-8')
        
        i=str(j)
        r=a.strip()
        #b=r.split(" ")
        
        c={i:r}
        return c
    

  

# iterate through all file
def call():
    i=0
    h=[]
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{path}\{file}"
            i=i+1
      
            # call read text file function
            l=read_text_file(file_path,i)
            h.append(l)
    return h
s=call()
with open(path1,'a',encoding="utf8") as g:
        g.write(json.dumps(s)+"\n")
