import psycopg2

def initConectionBuro():
    con = psycopg2.connect(database="burocredito", user="postgres", password="C2m3s0m598", host="192.168.1.73", port="5432")
    return con

def initConectionUsers():
    con = psycopg2.connect(database="users", user="postgres", password="C2m3s0m598", host="192.168.1.73", port="5432")
    return con
