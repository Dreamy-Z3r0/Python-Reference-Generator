import tkinter as tk


class InputInterface:
    def __init__(self, title="Reference input", geometry=None):
        # Input categories
        self.inputFields = {
            'Type of source': None,
            'Author(s)': None,
            'Title': None,
            'Year': None,
            'City': None,
            'State/Province': None,
            'Country/Region': None,
            'Publisher': None,
            'Editor(s)': None,
            'Volume': None,
            'Number of volumes': None,
            'Translator(s)': None,
            'Short title': None,
            'Standard number': None,
            'Pages': None,
            'Edition': None,
            'Comments': None,
            'Medium': None,
            'Year accessed': None,
            'Month accessed': None,
            'Day accessed': None,
            'URL': None,
            'DOI': None,
            'ISSN': None
        }

        # Initialise input application with GUI
        self.app = tk.Tk()
        self.app.title(title)

        # Set geometry
        if geometry is not None:
            self.app.geometry(geometry)

        # Put on top
        self.app.lift()
        self.app.attributes('-topmost', True)
        self.app.after_idle(self.app.attributes, '-topmost', False)

        # Input table
        self.create_input_field()

        # Buttons
        self.create_button_field()

        # Main loop
        self.app.mainloop()        


    def create_input_field(self):
        self.inputTable = tk.Frame(self.app)
        self.inputTable.pack()

        for index, label in enumerate(list(self.inputFields.keys())):
            fieldLabel = tk.Label(self.inputTable, text=label)
            fieldLabel.grid(row=index, column=0, sticky='E')

            self.inputFields[label] = [tk.Entry(self.inputTable), None]
            self.inputFields[label][0].grid(row=index, column=1, sticky='W')


    def create_button_field(self):
        self.buttons = tk.Frame(self.app)
        self.buttons.pack()

        # Clear button
        self.clear_all = tk.Button(self.buttons, text='Clear', command=self.clear_fields)
        self.clear_all.pack(side=tk.LEFT)

        # Submit button
        self.submit_button = tk.Button(self.buttons, text='Submit', command=self.on_submit)
        self.submit_button.pack(side=tk.LEFT)

        # Exit button
        self.exit_button = tk.Button(self.buttons, text="Cancel", command=self.app.destroy)
        self.exit_button.pack(side=tk.LEFT)
    

    def clear_fields(self):
        for label in list(self.inputFields.keys()):
            self.inputFields[label][0].delete(0, tk.END)


    def on_submit(self):
        for label in list(self.inputFields.keys()):
            self.inputFields[label][1] = self.inputFields[label][0].get()
            self.inputFields[label][0].delete(0, tk.END)

            print(f'{label}: {self.inputFields[label][1]}')



if __name__ == '__main__':
    testApp = InputInterface()