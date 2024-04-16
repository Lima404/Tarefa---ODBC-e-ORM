import psycopg2

conn = psycopg2.connect(
    dbname="atividade_db",
    user="postgres",
    password="postgres",
    host="172.18.0.2",
    port="5432"
)

cur = conn.cursor()

sql = "INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (%s, %s, %s, %s)"
val = ("Monitoria - Atividade 2", 2, "2018-06-27", "2018-07-31")
cur.execute(sql, val)

conn.commit()

sql = "UPDATE projeto SET responsavel = %s WHERE codigo = %s"
val = (3, 1)
cur.execute(sql, val)

conn.commit()

cur.execute("SELECT * FROM projeto ORDER BY codigo")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT * FROM atividade ORDER BY codigo")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()