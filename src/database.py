import sqlite3
from sqlite3 import Error

DB_PATH = "database.db"


def db_create():
    sql_create_user = """CREATE TABLE IF NOT EXISTS users 
    (
        id integer PRIMARY KEY,
        prefix text NOT NULL,
        class text
    ); """
    db_exec(sql_create_user)


def db_adduser(userid):
    sql = f'''INSERT INTO users (id,prefix, class) VALUES (?, ?, ?)'''
    args = (userid, '?', None)

    db_exec(sql, args)


def db_exists(userid):
    sql = f'''SELECT * FROM users ORDER BY id'''
    db = db_exec(sql)

    for row in db:
        if userid == row[0]:
            return row

    return None


def db_exec(sql, args=None):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    if args:
        res = cur.execute(sql, args).fetchall()
    else:
        res = cur.execute(sql).fetchall()

    conn.commit()
    if conn:
        conn.close()

    return res
