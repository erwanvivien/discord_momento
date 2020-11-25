import sqlite3
from commands import DEFAULT_PREFIX
from sqlite3 import Error

DB_PATH = "database.db"


def create():
    sql_create_user = """CREATE TABLE IF NOT EXISTS users 
    (
        id integer PRIMARY KEY,
        prefix text NOT NULL,
        class text
    ); """
    exec(sql_create_user)


def adduser(userid):
    sql = f'''INSERT INTO users (id, prefix, class) VALUES (?, ?, ?)'''
    args = (userid, DEFAULT_PREFIX, None)

    exec(sql, args)


def clear_all(userid):
    sql = f"DELETE FROM users WHERE id = {userid}"
    exec(sql)


def get_group(userid):
    sql = f'SELECT class FROM users WHERE id={userid}'
    return exec(sql)[0][0]


def set_group(userid, group):
    sql = f"UPDATE users SET class = '{group}' WHERE id = {userid}"
    exec(sql)


def set_prefix(userid, prefix):
    sql = f"UPDATE users SET prefix = '{prefix}' WHERE id = {userid}"
    exec(sql)


def get_settings(userid):
    sql = f"SELECT * FROM users WHERE id = {userid}"
    return exec(sql)[0]


def get_prefix(userid):
    sql = f'SELECT prefix FROM users WHERE id={userid}'
    return exec(sql)[0][0]


def user_exists(userid):
    sql = f'''SELECT * FROM users ORDER BY id'''
    db = exec(sql)

    for row in db:
        if userid == row[0]:
            return row

    return None


def exec(sql, args=None):
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
