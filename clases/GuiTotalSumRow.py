class GuiTotalSumRow():
    def __init__(self, frame, tk, row):
        self.frame = frame
        self.tk = tk
        self.row = row

    def createRow(self):
        self.tk.Label(self.frame, text="РАЗОМ:",
                      font="Helvetica 9 bold", bg="#EBEBEB").grid(pady=1, row=self.row, column=0, sticky='e')

        self.mainMoneyPlan = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.mainMoneyPlan).grid(row=self.row, column=2)

        self.mainPacksPlan = self.tk.IntVar()
        self.tk.Label(self.frame, text="План уп.",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.mainPacksPlan).grid(row=self.row, column=3)

        self.mainMoneyFact = self.tk.IntVar()
        self.tk.Label(self.frame, text="Гроші факт",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.mainMoneyFact).grid(row=self.row, column=4)

        self.mainPacksFact = self.tk.IntVar()
        self.tk.Label(self.frame, text="Уп. факт",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.mainPacksFact).grid(row=self.row, column=5)

        self.mainPercent = self.tk.StringVar()
        self.tk.Label(self.frame, text="%",
                      font="Helvetica 9 bold", bg="#EBEBEB", textvariable=self.mainPercent).grid(row=self.row, column=6)
        # Manth 1
        self.manth1MoneyPlan = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 1 гроші план",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth1MoneyPlan).grid(row=self.row, column=8)

        self.manth1PacksPlan = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 1 уп. план",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth1PacksPlan).grid(row=self.row, column=9)

        self.manth1MoneyFact = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 1 гроші факт",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth1MoneyFact).grid(row=self.row, column=10)

        self.manth1PacksFact = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 1 уп. факт",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth1PacksFact).grid(row=self.row, column=11)

        self.manth1Percent = self.tk.IntVar()
        self.tk.Label(self.frame, text="%",
                      font="Helvetica 9 bold", bg="#EBEBEB", textvariable=self.manth1Percent).grid(row=self.row, column=12)

        # Manth 2
        self.manth2MoneyPlan = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 2 гроші план",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth2MoneyPlan).grid(row=self.row, column=14)

        self.manth2PacksPlan = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 2 уп. план",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth2PacksPlan).grid(row=self.row, column=15)

        self.manth2MoneyFact = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 2 гроші факт",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth2MoneyFact).grid(row=self.row, column=16)

        self.manth2PacksFact = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 2 уп. факт",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth2PacksFact).grid(row=self.row, column=17)

        self.manth2Percent = self.tk.IntVar()
        self.tk.Label(self.frame, text="%",
                      font="Helvetica 9 bold", bg="#EBEBEB", textvariable=self.manth2Percent).grid(row=self.row, column=18)
        # Manth 3
        self.manth3MoneyPlan = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 3 гроші план",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth3MoneyPlan).grid(row=self.row, column=20)

        self.manth3PacksPlan = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 3 уп. план",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth3PacksPlan).grid(row=self.row, column=21)

        self.manth3MoneyFact = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 3 гроші факт",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth3MoneyFact).grid(row=self.row, column=22)

        self.manth3PacksFact = self.tk.IntVar()
        self.tk.Label(self.frame, text="Місяць 3 уп. факт",
                      font="Helvetica 9", bg="#EBEBEB", textvariable=self.manth3PacksFact).grid(row=self.row, column=23)

        self.manth3Percent = self.tk.IntVar()
        self.tk.Label(self.frame, text="%",
                      font="Helvetica 9 bold", bg="#EBEBEB", textvariable=self.manth3Percent).grid(row=self.row, column=24)

    def setData(self,
                sumTotalMoneyPlan,
                sumMainPacksPlan,
                sumMainMoneyFact,
                sumMainPacksFact,

                sumManth1MoneyPlan,
                sumManth1PacksPlan,
                sumManth1MoneyFact,
                sumManth1PacksFact,

                sumManth2MoneyPlan,
                sumManth2PacksPlan,
                sumManth2MoneyFact,
                sumManth2PacksFact,

                sumManth3MoneyPlan,
                sumManth3PacksPlan,
                sumManth3MoneyFact,
                sumManth3PacksFact):

        self.mainMoneyPlan.set(sumTotalMoneyPlan)
        self.mainPacksPlan.set(sumMainPacksPlan)
        self.mainMoneyFact.set(sumMainMoneyFact)
        self.mainPacksFact.set(sumMainPacksFact)
        percent = (sumMainMoneyFact*100)/sumTotalMoneyPlan
        self.mainPercent.set(round(percent, 1))

        self.manth1MoneyPlan.set(sumManth1MoneyPlan)
        self.manth1PacksPlan.set(sumManth1PacksPlan)
        self.manth1MoneyFact.set(sumManth1MoneyFact)
        self.manth1PacksFact.set(sumManth1PacksFact)
        percentManth1 = (sumManth1MoneyFact*100)/sumManth1MoneyPlan
        self.manth1Percent.set(round(percentManth1, 1))

        self.manth2MoneyPlan.set(sumManth2MoneyPlan)
        self.manth2PacksPlan.set(sumManth2PacksPlan)
        self.manth2MoneyFact.set(sumManth2MoneyFact)
        self.manth2PacksFact.set(sumManth2PacksFact)
        percentManth2 = (sumManth2MoneyFact*100)/sumManth2MoneyPlan
        self.manth2Percent.set(round(percentManth2, 1))

        self.manth3MoneyPlan.set(sumManth3MoneyPlan)
        self.manth3PacksPlan.set(sumManth3PacksPlan)
        self.manth3MoneyFact.set(sumManth3MoneyFact)
        self.manth3PacksFact.set(sumManth3PacksFact)
        percentManth3 = (sumManth3MoneyFact*100)/sumManth3MoneyPlan
        self.manth3Percent.set(round(percentManth3, 1))
