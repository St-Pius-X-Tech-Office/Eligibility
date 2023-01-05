"""
Make a dictionary of the students and their parents emails
"""
import pandas as pd

# Get the CSV File
email = pd.read_csv("emails.csv")

# Initialize an empty dictionary for data storage
email_Dict = {}


# Main function to loop through the data and create the dictionary
def main():

    for i in range(len(email)):
        # Use the student ID as a key
        current_Student = email.loc[i, "Student ID"]

        student_email = str(email.loc[i, "Email"])
        parents_email = str(email.loc[i, "Parents' Email"])

        # Combine the student and parent emails into one value
        # This is okay because in the end we don't care we send
        # to all emails and don't separate them based on role
        value = student_email + " ," + parents_email

        # Add the values to the dictionary
        email_Dict[current_Student] = value

    # Return the dictionary for use in the main file
    return email_Dict
