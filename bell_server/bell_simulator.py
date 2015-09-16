import sqlite3
import os
import time


con = sqlite3.connect("bell.db")
cursor = con.cursor()


bell_id = input("Which bell would you want?")


while True:
    time.sleep(2);
    os.system('clear')
    cursor.execute("SELECT open_status FROM bell WHERE id = ?",[bell_id])
    open_status = cursor.fetchone()
    if open_status[0] == 1: #opend
        print("+-----------------------------------------------+")
        print("|                                               |")
        print("|  +-----------------------------------------+  |")
        print("|  |XXXXX  mmm     mmmm    mmmm   m   m XXXXX|  |")
        print("|  |XX    m   m    m   m   m      mm  m    XXl  |")
        print("|  |XXX   m   m    mmmm    mmmm   m m m   XXX|  |")
        print("|  |XX    m   m    m       m      m  mm    XX|  |")
        print("|  |XXXXX  mmm     m       mmmm   m   m XXXXX|  |")
        print("|  +-----------------------------------------+  |")
        print("|                                               |")
        print("|                    +++++++                    |")
        print("|     -------------------------------------     |")
        print("|                  +++++++++++                  |")
        print("|     -------------------------------------     |")
        print("|                  +++++++++++                  |")
        print("|     -------------------------------------     |")
        print("|                    +++++++                    |")
        print("|                                               |")
        print("|                                               |")
        print("|                   +-------+                   |")
        print("|                   |mmmmmmm|                   |")
        print("|                   |mmmmmmm|                   |")
        print("|                   |mmmmmmm|                   |")
        print("|                   +-------+                   |")
        print("|                                               |")
        print("+-----------------------------------------------+")
    else:
        print("+-----------------------------------------------+")
        print("|                                               |")
        print("|  +-----------------------------------------+  |")
        print("|  |   mmm  m      mmm    mmm   mmmm  mmmm   |  |")
        print("|  |  m     m     m   m  m      m     m   m  |  |")
        print("|  |  m     m     m   m   mmm   mmmm  m   m  |  |")
        print("|  |  m     m     m   m      m  m     m   m  |  |")
        print("|  |   mmm  mmmm   mmm    mmm   mmmm  mmmm   |  |")
        print("|  +-----------------------------------------+  |")
        print("|                                               |")
        print("|                    +++++++                    |")
        print("|     -------------------------------------     |")
        print("|                  +++++++++++                  |")
        print("|     -------------------------------------     |")
        print("|                  +++++++++++                  |")
        print("|     -------------------------------------     |")
        print("|                    +++++++                    |")
        print("|                                               |")
        print("|                                               |")
        print("|                   +-------+                   |")
        print("|                   |mmmmmmm|                   |")
        print("|                   |mmmmmmm|                   |")
        print("|                   |mmmmmmm|                   |")
        print("|                   +-------+                   |")
        print("|                                               |")
        print("+-----------------------------------------------+")

