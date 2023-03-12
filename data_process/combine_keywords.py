import os
import json

# Initialize variables
data = []
id_counter = 1

# Loop through all JSON files in the current directory
for file in os.listdir():
    if file.endswith(".json"):
        # Read the file and append its data to the list
        with open(file, "r") as f:
            file_data = json.load(f)
            for item in file_data:
                # Update the id key to be consecutive
                item["id"] = id_counter
                id_counter += 1
            data += file_data

# Write the combined data to a new JSON file
with open("combined_data.json", "w") as f:
    json.dump(data, f, indent=4)
