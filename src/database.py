import sqlite3
from sqlite3 import Error

DB_PATH = "database.db"

create_connection(DB_PATH)


def create_connection():
    try:
        conn = sqlite3.connect('database.db')
        sql_create_user = """ CREATE TABLE IF NOT EXISTS user (
                                                id integer PRIMARY KEY,
                                                prefix text NOT NULL,
                                                group text NOT NULL
                                            ); """
        # sql_create_guilds = """ CREATE TABLE IF NOT EXISTS guilds (
        #                                         id integer PRIMARY KEY,
        #                                         prefix text,
        #                                         group text
        #                                     ); """
        create_table(conn, sql_create_user)
        # create_table(conn, sql_create_guilds)
    except:
        return


def db_exec(sql, args=None):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    if args:
        cur.execute(sql, args)
    else:
        cur.execute(sql)

    close_connection(conn)
