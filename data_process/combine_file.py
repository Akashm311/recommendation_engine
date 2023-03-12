import json
import os

# Define the path where the JSON files are located
path = r"C:\Users\Akash\Documents\automatad\data\text"
path2=r"C:\Users\Akash\Documents\automatad\data\combined_fi.json"

# Initialize an empty dictionary to store the combined JSON data
combined_data = []

# Define a counter variable to keep track of the ID keys
counter = 1

# Loop through each file in the directory
for file in os.listdir(path):
    # Check whether file is in JSON format
    if file.endswith(".json"):
        # Open the file and load the JSON data into a dictionary
        with open(os.path.join(path, file), "r") as f:
            data = json.load(f)
        
        # Loop through each dictionary in the JSON data
        for item in data:
            
            # Update the ID key with a consecutive number string
            combined_data.append({str(counter):item[list(item.keys())[0]]})
            counter += 1

# Write the combined JSON data to a new file
with open(path2, "w") as f:
    json.dump(combined_data, f, indent=4)
