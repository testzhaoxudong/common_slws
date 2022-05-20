import pymysql




conn = pymysql.connect( user = "root",password = "Matrix2021@",host = "122.112.174.71",port = 0,charset = "utf8",database="stfoa" )

cur = conn.cursor()
sql = "SELECT * FROM blade_role_scope"
exe = cur.execute(sql)
print(exe)
# cur.close()

