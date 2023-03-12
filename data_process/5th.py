import json
import jsonlines

path_out = r"C:\Users\Akash\Documents\automatad\data\output.jsonl"

path=r"C:\Users\Akash\Documents\automatad\data\pro_text.json"
path1 = r"C:\Users\Akash\Documents\automatad\data\clean.json"
with open(path, 'r',encoding="utf8") as f:
        a=json.load(f)


with open(path1, 'r',encoding="utf8") as g:
        b=json.load(g)



with jsonlines.open(path_out, mode='w') as writer:
    for i in range(1, len(a) + 1):
        l = str(i)
        k = a[i - 1][l]
        m = b[i-1]["keyphrases"]
        writer.write({"document": k, "extractive_keyphrases": m})
