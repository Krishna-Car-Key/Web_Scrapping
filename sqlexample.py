import sqlite3

# Establishing a connection and cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
connection.commit()

# Queering all datas
rows = cursor.execute("SELECT * FROM tours")
rows = rows.fetchall()
print(rows)

# Queering all columns based on conditionals
rows2 = cursor.execute("SELECT * FROM tours WHERE date='2088.5.11'")
rows2 = rows2.fetchall()
print(rows2)

# Queering some columns based on conditionals
rows3 = cursor.execute("SELECT band,city FROM tours WHERE date='2088.5.11'")
rows3 = rows3.fetchall()
print(rows3)

# Inserting some rows in database
data_to_insert = [('Elephants', 'Elephant city', '2088.5.13'),
                  ('Dinosaurs', 'Dinosaur city', '2088.5.13')]
cursor.executemany("INSERT INTO tours VALUES(?,?,?)", data_to_insert)
connection.commit()

# Queering all datas
rows = cursor.execute("SELECT * FROM tours")
rows = rows.fetchall()
print(rows)
connection.close()
