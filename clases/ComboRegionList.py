
class ComboRegionList():
    def __init__(self, frame, ttk, tk, list, i, funcToUpdate):
        self.variableOfRegion = tk.StringVar()

        comboRegion = ttk.Combobox(
            frame, textvariable=self.variableOfRegion, value=list, width=25, background="#EBEBEB", cursor="hand2")
        comboRegion['state'] = 'readonly'

        comboRegion.grid(
            row=i, column='0')
        tk.Button(frame, text='Більше', padx=0, command=self.buttonFunction, cursor="hand2").grid(
            row=i, column='1', padx=10, pady=1)

        comboRegion.bind("<<ComboboxSelected>>", lambda x: funcToUpdate())

    def buttonFunction(self):
        print(self.variableOfRegion.get())

    def getRegion(self):
        return self.variableOfRegion.get()

    def setGuiDefotlGegion(self, i):
        from app.getListFromJson import getListFromJson
        defoltGuiData = getListFromJson("defolt_set_gui_region")
        region = defoltGuiData[f"{i}"]
        self.variableOfRegion.set(region)
