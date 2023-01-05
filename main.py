import pandas as pd
import emails

One_Fail_Columns = [
    "Student Name",
    "Parent Name",
    "Course",
    "Grade",
    "Emails",
]

Two_Fail_Columns = [
    "Student Name",
    "Parent Name",
    "Course",
    "Grade",
    "Emails",
]

one_df = pd.DataFrame(columns=One_Fail_Columns)
two_df = pd.DataFrame(columns=Two_Fail_Columns)

masterList = pd.read_csv("grades.csv")

count = {}

# Run a for loop to count how many times a student appears in the list
# This will allow us to split student who have > 1 failing grade.
for i in range(len(masterList)):
    id = masterList.loc[i, "Student ID"]

    if id not in count:
        count[id] = 1
    else:
        count[id] += 1


def main():

    for i in range(len(masterList)):
        id = masterList.loc[i, "Student ID"]

        # Write to the one list if the student only is listed once
        if count[id] == 1:
            one_df.loc[-1] = [
                masterList.loc[i, "Student name"],
                masterList.loc[i, "Parents/Guardians"],
                masterList.loc[i, "Section ID"],
                masterList.loc[i, "Cumulative gradebook grade"],
                emails.email_Dict[id],
            ]
            one_df.index += 1
            one_df.sort_index()
        else:
            two_df.loc[-1] = [
                masterList.loc[i, "Student name"],
                masterList.loc[i, "Parents/Guardians"],
                masterList.loc[i, "Section ID"],
                masterList.loc[i, "Cumulative gradebook grade"],
                emails.email_Dict[id],
            ]
            two_df.index += 1
            two_df.sort_index()


# Run the email script
emails.main()
# Run the main script above
main()

# Write the dataframes to our CSV files
one_df.to_csv("Test 1 fail.csv", index=False)
two_df.to_csv("Test 2 fail.csv", index=False)

# For me :)
print("You did it ya big lug...")
