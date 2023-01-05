# Eligibility Script

This repo is for the scripts needed to run and create the eligibility CSVs for
progress reports and report card grades.

## Pre-Reqs

Things you will need to have installed:

* Python3.8+
* Pandas (python package | use pip to install)

## Steps

Before running the scripts, you will need to go to [Blackbaud](stpiusx.myschoolapp.com) and download the reports, of which there are 2.

They are both reports under the **Academic** tab.
The first is a variation of the following name: *Eligibility (Q1)/(Q2)/(Q3)*

Once you locate it, ensure the school year is correct and save the file in the same folder as the scripts, and use the name "grades.csv".

The second script is called *students/parents*. Again, ensure that the year is correct, and save the file in the same folder as the scripts and name it "emails.csv".

## Running

Once you have the files saved, simply run the **main.py** script in the command line as such:

```bash
python3 main.py
```

Assuming no errors, you will see the 2 CSV files in the current directory. This means that you are done and can email them to the appropriate parties.

