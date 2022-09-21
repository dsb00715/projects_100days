""" import json
import pandas as pd

df = pd.read_json("DeviceTechnicalSettings.json")

with open("DeviceTechnicalSettings.json", "r") as f:
    data = json.load(f)
df.to_excel("output.xlsx")

print(df.head())
 """

# ********************************************************************

""" import json
import pandas as pd
import numpy as np

df = pd.read_excel("Dolice_codes.xlsx")
df.update('"' + df["OPC NAME"].astype(str) + '"')
df.update('"' + df["USERCODE"].astype(str) + '"')
merged_df = df["OPC NAME"] + ": " + df["USERCODE"] + ","


try:
    np.savetxt(r"final_codes.txt", merged_df.values, fmt="%s")
    print("file saved!! please check")
except:
    print("there is an error while saving file. Try again!") """


# ****************************************************************
