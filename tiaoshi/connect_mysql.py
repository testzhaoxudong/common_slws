import csv

import pymysql
import os

class ConnectMysql():
    def get_mysql_config(sfle,sql):
        db_data = os.path.join(os.path.dirname(__file__),"config","db.csv")
        with open(db_data,"r",encoding="utf-8") as data:
            file_data = csv.reader(data)
            # for file in file_data:
            #     print(file)
            db_info = dict(file_data)
            print(db_info)
        # return dict_file
        conn = pymysql.connect(host=db_info["Host"], user=db_info["Username"], password=db_info["Passwd"],
                               database=db_info["dbName"], port=int(db_info["Port"]), charset='utf8')
        print(conn)
        youbiao = conn.cursor()
        youbiao.execute(sql)
        conn.commit()
        result = youbiao.fetchall()
        youbiao.close()
        conn.close()
        return result

if __name__ == '__main__':
    sql = "SELECT * FROM blade_notice"
    db_info = ConnectMysql().get_mysql_config(sql)
    print(db_info)



