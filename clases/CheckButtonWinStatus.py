class CheckButtonWinStatus():
    def __init__(self, ttk, tk, name):
        self.ttk = ttk
        self.tk = tk
        self.var = tk.BooleanVar()
        self.name = name

    def createCheckbutton(self, window, i):
        s = self.ttk.Style()
        s.configure('Red.TCheckbutton', background='#ffffff')
        self.ttk.Checkbutton(window, text=self.name, variable=self.var).grid(
            row=i, column=0, sticky='w', padx=4)
