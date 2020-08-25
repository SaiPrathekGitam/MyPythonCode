# Program to list all the data from jobs table

import sqlite3

con = sqlite3.connect(r"C:\Python\hr.db")
cur = con.cursor()

try:
    cur.execute("select * from jobs")

    for job in cur.fetchall():
        # print(f"{job[0]} {job[1]:20} {job[2]:5} {job[3]:7}")
        print(f"{job[0]:3} {job[1]:20} {job[2]:5} {job[3]:7}")
except Exception as ex:
    print(f"Error : {ex}")
finally:
    print("Closing Resources!")
    cur.close()
    con.close()