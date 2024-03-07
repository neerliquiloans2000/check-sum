import mysql.connector
conn = mysql.connector.connect(
    host="ll-staging-rds-cluster.cluster-cgyu6lttldv9.ap-south-1.rds.amazonaws.com",
    user="pareshkanjani",
    password="JNbYiQbw",
    database="liquiloans"
)

cursor = conn.cursor()
cursor.execute("SELECT id FROM los_application order by id desc limit 5")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()