# Program to update a job to jobs database

import sqlite3
import sys

con = sqlite3.connect(r"C:\Python\hr.db")
cur = con.cursor()

try:
    id = input("Enter The ID : ")
    cur.execute("select title from jobs where id = (?)", (id,))
    job = cur.fetchone()
    if job is None:
        print("Sorry!Job ID Not Found")
        sys.exit(1)
    print(f"Job Title : {job[0]}")
    title = input("Enter The New Job Title : ")
    cur.execute("update jobs set title = ? where id = ?", (title, id))
    con.commit()
    print("Updated Successfully!")
except Exception as ex:
    print(f"Error : {ex}")
finally:
    print("Closing Resources!")
    cur.close()
    con.close()
