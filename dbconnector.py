import pymysql

def connection():
    con=pymysql.connect(host='localhost', user='root', password='', db='usersystem', port=3306)
    cur=con.cursor()
    return con,cur
