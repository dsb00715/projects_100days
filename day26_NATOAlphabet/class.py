# list comprehension : Coding room exercises
# dictionary comprehension: Coding room exercises & below
""" import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {name: random.randint(50, 90) for name in names}
print(student_scores)

passed_students = {key: value for key, value in student_scores.items() if value >= 60}

print(passed_students)
 """

import pandas as pd

student_dict = {"student": ["Alex", "Beth", "Caroline"], "score": [56, 78, 98]}
student_df = pd.DataFrame(student_dict)
# print(student_df)

""" 
# dictionary like loop
for key, value in student_df.items():
    print(key)
    print(value) """

for index, row in student_df.iterrows():
    print(row.score)
