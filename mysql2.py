import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='root',
    password='',
    database='restaurante'
)
c = db.cursor()
c.execute("SELECT * FROM menu")
# no hay que olvidar de liberar el cursor para evitar problemas de memoria

c.fetchall()

for restaurante in c:
    print(restaurante)
    pass

c.close()
db.close()