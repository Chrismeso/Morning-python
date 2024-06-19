import sqlite3

conn = sqlite3.connect('data.db')
print("successfully connected to database")

conn.execute("UPDATE Employee set SAlARY= 500000.0 WHERE ID=4")
conn.commit()

data = conn.execute("SELECT * FROM Employee")
for employee in data:
    print("ID: ", employee[0])
    print("FIRSTNAME: ", employee[1])
    print("LASTNAME: ", employee[2])
    print("AGE: ", employee[3])
    print("POSITION: ", employee[4])
    print("SALARY: ", employee[5])

