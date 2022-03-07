import psycopg2

def initConection():
    con = psycopg2.connect(database="users", user="postgres", password="C2m3s0m598", host="192.168.1.73", port="5432")
    return con
