import pandas as pd

data = {
    "ID": [1,2,3,4,5],
    "Name": ["Ali","Sara","John","Ayesha","Michael"],
    "Age": [25,30,45,28,35],
    "Dept": ["IT","HR","Finance","IT","Marketing"],
    "Salary": [60000,50000,80000,55000,70000]
}

df = pd.DataFrame(data)
print(df)





import json

# Load JSON file
with open(r"c:\Ali\py\one\Pandas\save\US_STATE_recipes.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame.from_dict(data, orient='index')

print(df.head(3))        # First 3 rows
print(df.info())         # Column types and counts
print(df.describe())     # Basic stats for numeric columns
print(df.shape)          # (rows, columns)
