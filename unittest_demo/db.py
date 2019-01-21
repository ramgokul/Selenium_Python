import mysql.connector

mydb = mysql.connector.connect(
  host="172.16.204.44",
  user="AutoDBUser",
  passwd="portal123!",
  database="AutomationDB"
)

mycursor = mydb.cursor()
sql = "select InputParams from tblwebdrivertestdata where TestId='AM-4526'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult[0])