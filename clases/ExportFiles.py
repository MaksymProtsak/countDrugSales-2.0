class ExportFiles():
    def __init__(self, frame, tk, i, name):
        self.name = name
        self.frame = frame
        self.tk = tk
        self.i = i
        self.var = tk.BooleanVar()

    def createGuiObject(self):
        self.tk.Checkbutton(self.frame, text=self.name, variable=self.var,  cursor="hand2").grid(
            column=self.i, row=0)

    def returnName(self):
        return self.name, self.var.get()
