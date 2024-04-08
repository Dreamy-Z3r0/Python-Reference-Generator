import tkinter as tk
import sqlite3


class MainInterface:
    def __init__(self, title="Reference Generator", geometry="1024x768"):
        self.database = "References.db"

        # Create a database storing reference inputs (if none exists)
        MainInterface.create_database(self.database)
    
    @staticmethod
    def create_database(databaseName):
        conn = sqlite3.connect(databaseName)
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS References (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                 )""")
        conn.commit()
        conn.close()

    @classmethod
    def clear_field(cls, display_field):
        display_field.delete(0, tk.END)