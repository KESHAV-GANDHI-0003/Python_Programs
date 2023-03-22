# Importing the required modules
import mysql.connector

# Creating a MySQL connection
db = mysql.connector.connect(
  host="localhost",
  user="teacher",
  password="myclass"
)

# Creating a database cursor
dbcrsr = db.cursor()

# Opening the database named "CLASS"
dbcrsr.execute("USE CLASS")
