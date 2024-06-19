import sqlite3

conn = sqlite3.connect('data.db')
print("successfully connected to database")

conn.execute("INSERT INTO Employee VALUES(11, 'Mark', 'Mugo', '45', '1200000.00', 'Manager')")
conn.execute("INSERT INTO Employee VALUES(21, 'Jane', 'Njoroge', '28', '200000.00', 'Admin')")
conn.execute("INSERT INTO Employee VALUES(31, 'Martha', 'Mugo', '34', '800000.00', 'HR')")
conn.execute("INSERT INTO Employee VALUES(41, 'Ann', 'Kirui', '55', '100000.00', 'Receptionist')")
conn.execute("INSERT INTO Employee VALUES(51, 'George', 'Kamua', '45', '1200000.00', 'Marketer')")
conn.execute("INSERT INTO Employee VALUES(61, 'Duke', 'Orodi', '38', '1500000.00', 'consultant')")

conn.commit()
print("Successfully inserted value into Employee table")