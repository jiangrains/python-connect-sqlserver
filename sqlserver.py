# --*-- coding:utf-8 -*-
import pymssql


#conn = pymssql.connect(host='localhost:1433',user='JDC-WIN7\tplink',database='HondaSafetyTechTransTable')
conn = pymssql.connect(server="localhost", port="1433", user="sa", password="309jiang", database="HondaSafetyTechTransTable",charset="UTF-8")
cur = conn.cursor()
cur.execute('select * from InterActionTransTable')

#print cur.fetchall()

for row in cur:
	print row[0], row[1], row[2], row["Qrcode"]

cur.close()
conn.close()
