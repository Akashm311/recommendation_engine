import json

path=r"C:\Users\Akash\Documents\automatad\data\text.json"
path1 = r"C:\Users\Akash\Documents\automatad\data\pro_text.json"
with open(path, 'r',encoding="utf8") as f:
        a=json.load(f)


count=0
m=0
ar=[]
for i in range(1,len(a)+1):
    l=str(i)
    m=m+1
    k=a[i-1][l]
    text=k.split(" ")
    ar.append({str(m):text})

with open(path1, 'w') as f:
    json.dump(ar, f) 
