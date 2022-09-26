""" 
# Part1:
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Retrieving value from Key:
# print(programming_dictionary)

# Adding/Editing new iterms to dictionary:
# programming_dictionary["Loop"] = "The action of doing something over and over again!"
# print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

"""

# ***************************************************************************************************

""" 

# Part2:
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    val = student_scores[key]
    if val > 90 and val <= 100:
        student_grades[key] = "Outstanding"
    elif val > 80 and val <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif val > 70 and val <= 80:
        student_grades[key] = "Acceptable"
    elif val <= 70:
        student_grades[key] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades) 

"""
# ***************************************************************************************************

""" # Part3

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
] """

# ***************************************************************************************************
from itertools import count


travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new_dict = {}
    new_dict["country"] = country
    new_dict["visits"] = visits
    new_dict["cities"] = cities
    travel_log.append(new_dict)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
