import pandas as pd
import emails
import grades

Main_Columns = [
    "Fail Count Tracker",
    "Student Name",
    "Parent Name",
    "Emails",
    "Course1",
    "Grade1",
]


main_df = pd.DataFrame(columns=Main_Columns)

masterList = pd.read_csv("grades.csv")

seen = []
ids = []


for i in range(len(masterList)):
    student_ID = masterList.loc[i, "Student ID"]

    if student_ID not in ids:
        ids.append(student_ID)


def main():

    count = 0
    for i in range(len(masterList)):
        student_ID = masterList.loc[i, "Student ID"]

        if len(grades.student_list[student_ID]) > 2:
            count = 1
        else:
            count = 0

        if student_ID not in seen:
            main_df.loc[-1] = [
                count,
                masterList.loc[i, "Student name"],
                masterList.loc[i, "Parents/Guardians"],
                emails.email_Dict[student_ID],
                grades.student_list[student_ID][0],
                grades.student_list[student_ID][1],
            ]
            main_df.index += 1
            main_df.sort_index()
            seen.append(student_ID)
        else:
            pass


def addColumns():
    main_df["Course2"] = grades.course2
    main_df["Grade2"] = grades.grade2
    main_df["Course3"] = grades.course3
    main_df["Grade3"] = grades.grade3
    main_df["Course4"] = grades.course4
    main_df["Grade4"] = grades.grade4
    main_df["Course5"] = grades.course5
    main_df["Grade5"] = grades.grade5
    main_df["Course6"] = grades.course6
    main_df["Grade6"] = grades.grade6
    main_df["Course7"] = grades.course7
    main_df["Grade7"] = grades.grade7


# Run the email script
emails.main()

# Run the functions above
main()
addColumns()

# Write the dataframes to our CSV files
main_df.to_csv("Masterlist.csv", index=False)

# Terminal message showing completion
print("Process Completed")
