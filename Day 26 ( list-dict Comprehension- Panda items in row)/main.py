# List Comprehension
import random
import pandas

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
# print(new_numbers)
name = "Angela"
letter_list = [letter for letter in name]
# print(letter_list)
new_mult = [number * 2 for number in range(1, 5)]
# print(new_mult)
name_people = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_name_people = [name.upper() for name in name_people if len(name) > 5]
# print(new_name_people)
# Dict Comprehension
student_score = {name: random.randint(50, 100) for name in name_people}
# print(student_score)
passed_students = {name: score for (name, score) in student_score.items() if score > 80}
# print(passed_students)
# Pandas Frame
student_dict = {
    "students": name_people,
    "Score": [random.randint(50, 100) for number in range(1, len(name_people) + 1)]

}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# Loop through a data frame NOT USEFUL
for (key, Value) in student_data_frame.items():
    print(Value)
# Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
# Loop through rows of data frame getting single ready items
for (index, row) in student_data_frame.iterrows():
    print(row.students)
# Loop through rows of data frame getting search ready
for (index, row) in student_data_frame.iterrows():
    if row.students == "Alex":
        print(row.Score)

