import tkinter as tk
import sqlite3

def create_database():
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS names (
                    id INTEGER PRIMARY KEY,
                    name TEXT
              )""")
    conn.commit()
    conn.close()

def on_submit(entry):
    name = entry.get()
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("INSERT INTO names (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def update_listbox(listbox):
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("SELECT * FROM names")
    rows = c.fetchall()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row[1])

    conn.close()

def main():
    # Create a database storing inputs (if none exists)
    create_database()

    # Initialise an application with GUI
    app = tk.Tk()
    app.title("Python Desktop App")
    app.geometry("400x300")

    # Add app label
    label = tk.Label(app, text="Enter your name:")
    label.pack()

    # Entry text box
    entry = tk.Entry(app)
    entry.pack()

    # Submit button
    submit_button = tk.Button(app, text="Submit", command=lambda: on_submit(entry))
    submit_button.pack()

    # Exit button
    exit_button = tk.Button(app, text="Exit", command=app.destroy)
    exit_button.pack()

    # Listbox for displaying all available entries
    listbox = tk.Listbox(app)
    listbox.pack()

    # Main loop
    while True:
        update_listbox(listbox)
        app.update_idletasks()
        app.update()

if __name__ == '__main__':
    main()