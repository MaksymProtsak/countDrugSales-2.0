class GuiSumRow():
    def __init__(self, frame, tk, row, rowName):
        self.frame = frame
        self.tk = tk
        self.row = row
        self.rowName = rowName

    def createRow(self):
        self.tk.Label(self.frame, text=f"{self.rowName} СУМА:", font="Helvetica 9 bold", bg="#EBEBEB").grid(
            pady=2, row=self.row, column=0, sticky='ne')
        # Manth total
        self.rowMoneyPlanVar = self.tk.IntVar()
        self.tk.Label(self.frame, text='Гроші план', textvariable=self.rowMoneyPlanVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=2, sticky='n')
        self.rowPacksPlanVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Упак. план", textvariable=self.rowPacksPlanVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=3, sticky='n')

        self.rowMoneyFactVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші факт", textvariable=self.rowMoneyFactVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=4, sticky='n')

        self.rowPacksFactVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Упак. факт", textvariable=self.rowPacksFactVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=5, sticky='n')

        self.rowTotalPercentVar = self.tk.StringVar()
        self.tk.Label(self.frame, text="Факт %", textvariable=self.rowTotalPercentVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=6, sticky='n')
        # Manth 1
        self.rowManth1MoneyPlanVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші палн місяць 1", textvariable=self.rowManth1MoneyPlanVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=8, sticky='n')

        self.rowManth1PacksPlanVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Упак. план місяць 1", textvariable=self.rowManth1PacksPlanVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=9, sticky='n')

        self.rowManth1MoneyFactVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші факт місяць 1", textvariable=self.rowManth1MoneyFactVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=10, sticky='n')

        self.rowManth1PacksFactVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Упак. факт місяць 1", textvariable=self.rowManth1PacksFactVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=11, sticky='n')

        self.rowManth1PercentVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 1 %", textvariable=self.rowManth1PercentVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=12, sticky='n')
        # Manth 2
        self.rowManth2MoneyPlanVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші палн місяць 2", textvariable=self.rowManth2MoneyPlanVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=14, sticky='n')

        self.rowManth2PacksPlanVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Упак. план місяць 2", textvariable=self.rowManth2PacksPlanVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=15, sticky='n')

        self.rowManth2MoneyFactVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші факт місяць 2", textvariable=self.rowManth2MoneyFactVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=16, sticky='n')

        self.rowManth2PacksFactVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Упак. факт місяць 2", textvariable=self.rowManth2PacksFactVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=17, sticky='n')

        self.rowManth2PercentVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 2 %", textvariable=self.rowManth2PercentVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=18, sticky='n')
        # Manth 3
        self.rowManth3MoneyPlanVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші палн місяць 3", textvariable=self.rowManth3MoneyPlanVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=20, sticky='n')

        self.rowManth3PacksPlanVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Упак. план місяць 3", textvariable=self.rowManth3PacksPlanVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=21, sticky='n')

        self.rowManth3MoneyFactVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші факт місяць 3", textvariable=self.rowManth3MoneyFactVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=22, sticky='n')

        self.rowManth3PacksFactVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Упак. факт місяць 3", textvariable=self.rowManth3PacksFactVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=23, sticky='n')

        self.rowManth3PercentVar = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 3 %", textvariable=self.rowManth3PercentVar,
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(row=self.row, column=24, sticky='n')

    def setDataMoneyPlan(self, data):
        self.rowMoneyPlanVar.set(data)

    def setDataPacksPlan(self, data):
        self.rowPacksPlanVar.set(int(data))

    def setDataMoneyFact(self, data):
        self.rowMoneyFactVar.set(int(data))

    def setDataPacksFact(self, data):
        self.rowPacksFactVar.set(int(data))

    def countPercent(self):
        percent = (self.rowMoneyFactVar.get()*100)/self.rowMoneyPlanVar.get()
        percent = round(percent, 1)
        self.rowTotalPercentVar.set(percent)

    # Month 1
    def setManth1MoneyPlan(self, data):
        self.rowManth1MoneyPlanVar.set(data)

    def setManth1PacksPlan(self, data):
        self.rowManth1PacksPlanVar.set(data)

    def setManth1MoneyFact(self, data):
        self.rowManth1MoneyFactVar.set(data)

    def setManth1PacksyFact(self, data):
        self.rowManth1PacksFactVar.set(data)

    def countPercentManth1(self):
        percent = (self.rowManth1MoneyFactVar.get()*100) / \
            self.rowManth1MoneyPlanVar.get()
        percent = round(percent, 1)
        self.rowManth1PercentVar.set(percent)
    # Month2

    def setManth2MoneyPlan(self, data):
        self.rowManth2MoneyPlanVar.set(data)

    def setManth2PacksPlan(self, data):
        self.rowManth2PacksPlanVar.set(data)

    def setManth2MoneyFact(self, data):
        self.rowManth2MoneyFactVar.set(data)

    def setManth2PacksyFact(self, data):
        self.rowManth2PacksFactVar.set(data)

    def countPercentManth2(self):
        percent = (self.rowManth2MoneyFactVar.get()*100) / \
            self.rowManth2MoneyPlanVar.get()
        percent = round(percent, 1)
        self.rowManth2PercentVar.set(percent)

    # Month3

    def setManth3MoneyPlan(self, data):
        self.rowManth3MoneyPlanVar.set(data)

    def setManth3PacksPlan(self, data):
        self.rowManth3PacksPlanVar.set(data)

    def setManth3MoneyFact(self, data):
        self.rowManth3MoneyFactVar.set(data)

    def setManth3PacksyFact(self, data):
        self.rowManth3PacksFactVar.set(data)

    def countPercentManth3(self):
        percent = (self.rowManth3MoneyFactVar.get()*100) / \
            self.rowManth3MoneyPlanVar.get()
        percent = round(percent, 1)
        self.rowManth3PercentVar.set(percent)
