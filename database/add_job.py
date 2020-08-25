# Program to add a job to jobs database

import sqlite3

con = sqlite3.connect(r"C:\Python\hr.db")
cur = con.cursor()

try:
    title = input("Enter The Job Title : ")
    minsal = input("Enter The Min Salary : ")
    maxsal = input("Enter The Max Salary : ")
    cur.execute("insert into jobs (title,minsal,maxsal) values (?,?,?)",
                (title, minsal, maxsal))
    con.commit()
    print("Added Successfully!")
except Exception as ex:
    print(f"Error : {ex}")
finally:
    print("Closing Resources!")
    cur.close()
    con.close()