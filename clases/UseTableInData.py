class UseTableInData():
    def __init__(self, tk, ttk, rowName, dateCreated, status, numRow, window):
        self.tk = tk
        self.ttk = ttk
        self.rowName = rowName
        self.dateCreated = dateCreated
        self.status = status
        self.numRow = numRow
        self.window = window
        self.var = tk.BooleanVar()

    def createRow(self):
        self.fileName = self.tk.Label(self.window,
                                      text=self.rowName)
        self.fileName.grid(row=self.numRow, column=0)

        self.fileDateCreated = self.tk.Label(self.window,
                                             text=self.dateCreated)
        self.fileDateCreated.grid(row=self.numRow, column=1)

        checkButton = self.ttk.Checkbutton(self.window,
                                           text='Опрацьовувати',
                                           variable=self.var,
                                           onvalue=1,
                                           offvalue=0,
                                           cursor="hand2",
                                           command=self.setStatus)

        checkButton.grid(row=self.numRow, column=2, padx=3)

        self.var.set(self.status)
        self.setStatus()

    def setStatus(self):
        status = self.var.get()
        if status == True:
            self.fileName.config(state='active')
            self.fileDateCreated.config(state='active')
        else:
            self.fileName.config(state='disabled')
            self.fileDateCreated.config(state='disabled')
