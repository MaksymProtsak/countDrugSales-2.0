class CheckButton():
    def __init__(self, ttk, tk, window, text, commandFun, xPlace):
        self.ttk = ttk
        self.tk = tk
        self.window = window
        self.text = text
        self.commandFun = commandFun
        self.xPlace = xPlace
        self.checkVar = self.tk.BooleanVar()

    def createCheckbutton(self):
        s = self.ttk.Style()
        s.configure('Red.TCheckbutton', background='#ffffff')
        self.ttk.Checkbutton(self.window, text=self.text, style='Red.TCheckbutton',
                             variable=self.checkVar, cursor="hand2", command=self.commandFun).place(x=self.xPlace, y=5)
