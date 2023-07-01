import random

numbers = [1,2,3]

#Instead of using for loop and append, use a list comprehension
new_list = [n + 1 for n in numbers]
print(new_list)

#Can also use strings

name = "Daniel"
new_list = [letter for letter in name]
print(new_list)

#Challenge

r = range(1,5)
new_list = [n * 2 for n in r]
print(new_list)


#Can add a test statement (The if command)
names = ["Daniel", "Cody", "Zach", "Isaiah", "Austin"]
new_list = [name.upper() for name in names if len(name) > 4]
print(new_list)


#################################################

#Dictionary Comprehensions

#For list
#new_dict = {new_key:new_value for item in list}

#For existing dictionary
#new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ["Daniel", "Cody", "Zach", "Isaiah", "Austin"]

students_scores = {student:random.randint(50,100) for student in names}
print(students_scores)

#passed_students = {student:"Passed" for student in students_scores if students_scores[student] > 70}
#or
passed_students = {student:score for (student, score) in students_scores.items() if score >= 70} #THE .items() is of the UTMOST importance!!!
print(passed_students)




#################################################

#Pandas Comprehensions
import pandas
student_dict = {"names": ["Daniel", "Cody", "Zach", "Isaiah", "Austin"], 
                "scores" : [99, 12, 84, 36, 42] }
print()
#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

#DataFrame

student_df = pandas.DataFrame(student_dict)
print(student_df)

# for (key, value) in student_df.items():
#     print(value)

#PANDAS HAS OWN LOOP METHOD
for(index, row) in student_df.iterrows():
    print(row.names)

#Can do row.names or row.score
