# [x] TODO-1: Prepare a simple dataset that contains 2 columns : Fur Color & Count
# [x] TODO-2: Count number of squirrels as per unique colors

import pandas as pd

data = pd.read_csv(
    "./day25_CSVData_Pandas/Central_Park_Squirrel_Census_-_Squirrel_Data.csv",
)

final_df = pd.DataFrame()

final_df["Fur Color"] = data["Primary Fur Color"].unique()

final_df.dropna(inplace=True)

for index, row in final_df.iterrows():
    final_df.at[index, "Count"] = len(
        data[data["Primary Fur Color"] == row["Fur Color"]]
    )


print(final_df)
