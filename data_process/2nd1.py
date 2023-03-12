import json

path = r"C:\Users\Akash\Documents\automatad\data\total2.json"
path1 = r"C:\Users\Akash\Documents\automatad\data\com_text2.json"
with open(path, 'r', encoding="utf8") as f:
    a = json.load(f)

m = 0
ar = []
for i in range(1, len(a) + 1):
    l = str(i)
    
    k = a[i - 1][l]
    text = k.split(" ")
    if len(text) > 900:
        for j in range(0, len(text), 900):
            c = text[j:j+900]
            if len(c) > 200:
                m = m + 1
                e = " ".join(c)
                ar.append({str(m): e})
            elif len(c) < 100:
                ar[-1][str(m)] += " " + " ".join(c)
    else:
        m = m + 1
        k = " ".join(text)
        ar.append({str(m): k})

with open(path1, 'w') as f:
    json.dump(ar, f)
