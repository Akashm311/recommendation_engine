import json
import os

path = r"C:\Users\Akash\Documents\automatad\data\com_text2.json"
path1 = r"C:\Users\Akash\Documents\automatad\data\text"

with open(path, 'r', encoding="utf8") as f:
    a = json.load(f)

batch_size = 300
num_batches = (len(a) // batch_size) + (1 if len(a) % batch_size != 0 else 0)

for batch_num in range(num_batches):
    start_index = batch_num * batch_size
    end_index = min(start_index + batch_size, len(a))
    
    batch_data = []
    for i in range(start_index, end_index):
        l = str(i+1)
        k = a[i][l]
        batch_data.append({str(i+1-start_index): k})
    
    batch_filename = f"batch_{batch_num+1}.json"
    with open(os.path.join(path1, batch_filename), 'w') as f:
        json.dump(batch_data, f,indent=4)
