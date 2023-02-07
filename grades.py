import pandas as pd

grade_List = pd.read_csv("grades.csv")

student_list = {}

course2 = []
grade2 = []
course3 = []
grade3 = []
course4 = []
grade4 = []
course5 = []
grade5 = []
course6 = []
grade6 = []
course7 = []
grade7 = []


def main():
    for i in range(len(grade_List)):
        student_id = grade_List.loc[i, "Student ID"]
        course = grade_List.loc[i, "Course title"]
        grade = grade_List.loc[i, "Numeric grade"]

        if student_id not in student_list:
            student_list[student_id] = []
            student_list[student_id].append(course)
            student_list[student_id].append(round(grade))
        else:
            student_list[student_id].append(course)
            student_list[student_id].append(round(grade))

    return student_list


main()

for id in student_list:
    try:
        course2.append(student_list[id][2])
    except IndexError:
        course2.append("")
for id in student_list:
    try:
        grade2.append(student_list[id][3])
    except IndexError:
        grade2.append("")
for id in student_list:
    try:
        course3.append(student_list[id][4])
    except IndexError:
        course3.append("")
for id in student_list:
    try:
        grade3.append(student_list[id][5])
    except IndexError:
        grade3.append("")
for id in student_list:
    try:
        course4.append(student_list[id][6])
    except IndexError:
        course4.append("")
for id in student_list:
    try:
        grade4.append(student_list[id][7])
    except IndexError:
        grade4.append("")
for id in student_list:
    try:
        course5.append(student_list[id][8])
    except IndexError:
        course5.append("")
for id in student_list:
    try:
        grade5.append(student_list[id][9])
    except IndexError:
        grade5.append("")
for id in student_list:
    try:
        course6.append(student_list[id][10])
    except IndexError:
        course6.append("")
for id in student_list:
    try:
        grade6.append(student_list[id][11])
    except IndexError:
        grade6.append("")
for id in student_list:
    try:
        course7.append(student_list[id][12])
    except IndexError:
        course7.append("")
for id in student_list:
    try:
        grade7.append(student_list[id][13])
    except IndexError:
        grade7.append("")
