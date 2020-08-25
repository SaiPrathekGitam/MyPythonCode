# Program to delete a job to jobs database

import sqlite3

con = sqlite3.connect(r"C:\Python\hr.db")
cur = con.cursor()

try:
    id = input("Enter The ID : ")
    cur.execute("delete from jobs where id = (?)", (id,))
    if cur.rowcount == 1:
        con.commit()
        print("Deleted Successfully!")
    else:
        print("ID Not Found!")
except Exception as ex:
    print(f"Error : {ex}")
finally:
    print("Closing Resources!")
    cur.close()
    con.close()
