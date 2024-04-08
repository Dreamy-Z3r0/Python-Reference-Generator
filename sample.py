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

def clear_field(display_field):
    display_field.delete(0, tk.END)

def on_submit(entry):
    name = entry.get()
    clear_field(entry)
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

    clear_field(listbox)
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

    # Button field
    buttons = tk.Frame(app)
    buttons.pack()

    # Clear text option for entry text box
    clear_text = tk.Button(buttons, text="Clear", command=lambda: clear_field(entry))
    clear_text.pack(side=tk.LEFT)

    # Submit button
    submit_button = tk.Button(buttons, text="Submit", command=lambda: on_submit(entry))
    submit_button.pack(side=tk.LEFT)

    # Exit button
    exit_button = tk.Button(buttons, text="Exit", command=app.destroy)
    exit_button.pack(side=tk.LEFT)

    # Listbox for displaying all available entries, with a scrollbar
    listbox_frame = tk.Frame(app)       # Create a frame
    listbox_frame.pack()

    listbox = tk.Listbox(listbox_frame)           # Create the listbox
    listbox.pack(side=tk.LEFT)

    scrollbar_listbox = tk.Scrollbar(listbox_frame)       # Verticle scrollbar for listbox
    scrollbar_listbox.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox.config(yscrollcommand=scrollbar_listbox.set)    # Integrate scrollbar to listbox
    scrollbar_listbox.config(command=listbox.yview)

    # Main loop
    while True:
        update_listbox(listbox)
        app.update_idletasks()
        app.update()

if __name__ == '__main__':
    main()