import sqlite3
import os
import time


con = sqlite3.connect("bell.db")
cursor = con.cursor()


bell_id = input("Which bell would you want?")


while True:
    time.sleep(3);
    os.system('clear')
    cursor.execute("SELECT open_status FROM bell WHERE id = ?",[bell_id])
    open_status = cursor.fetchone()
    print("--------------------------------")
    result = "Closed";
    if open_status[0] == 1:
        result = "Opened"

    print("| open status : "+ result+"         |")
    print("--------------------------------")

