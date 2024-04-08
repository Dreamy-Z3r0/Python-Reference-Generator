import tkinter as tk


class InputInterface:
    def __init__(self, title="Reference input", geometry=None):
        # Input categories
        self.inputCategories = [
            'Type of source',
            'Author(s)',
            'Title',
            'Year',
            'City',
            'State/Province',
            'Country/Region',
            'Publisher',
            'Editor(s)',
            'Volume',
            'Number of volumes',
            'Translator(s)',
            'Short title',
            'Standard number',
            'Pages',
            'Edition',
            'Comments',
            'Medium',
            'Year accessed',
            'Month accessed',
            'Day accessed',
            'URL',
            'DOI',
            'ISSN'
        ]

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

        self.entries = []

        for index, label in enumerate(self.inputCategories):
            fieldLabel = tk.Label(self.inputTable, text=label)
            fieldLabel.grid(row=index, column=0, sticky='E')

            self.entries.append(tk.Entry(self.inputTable))
            self.entries[-1].grid(row=index, column=1, sticky='W')


    def create_button_field(self):
        self.buttons = tk.Frame(self.app)
        self.buttons.pack()

        # Submit button
        self.submit_button = tk.Button(self.buttons, text='Submit', command=self.on_submit)
        self.submit_button.pack(side=tk.LEFT)

        # Exit button
        self.exit_button = tk.Button(self.buttons, text="Cancel", command=self.app.destroy)
        self.exit_button.pack(side=tk.LEFT)
    

    def on_submit(self):
        self.inputData = [entry.get() for entry in self.entries]
        for index, input in enumerate(self.inputData):
            print(f'{self.inputCategories[index]}: {input}')


if __name__ == '__main__':
    testApp = InputInterface()