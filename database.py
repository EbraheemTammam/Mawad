import os
import sqlite3
from pathlib import Path
from os.path import join
import sys

class Db:

    DB_URL = join(Path(__file__).resolve().parent, "db.sqlite3")
    # DB_URL = os.path.join(os.path.dirname(sys.executable), "db.sqlite3")

    @staticmethod
    def init_db():
        connection = sqlite3.connect(Db.DB_URL)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workdays (
                id TEXT PRIMARY KEY,
                date TEXT,
                start_time TEXT,
                end_time TEXT,
                break_hours REAL,
                work_hours REAL,
                driver_name TEXT,
                notes TEXT
            )
        ''')
        connection.commit()
        connection.close()

    @staticmethod
    def execute_query(query: str, params: list):
        connection = sqlite3.connect(Db.DB_URL)
        cursor = connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        connection.close()
        return rows

    @staticmethod
    def execute_command(query: str, params: list):
        connection = sqlite3.connect(Db.DB_URL)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()
