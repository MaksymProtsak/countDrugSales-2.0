class GuiRow():
    def __init__(self, frame, ttk, tk, drugList, regionCheckbuttonList, data, row, month1Status, month2Status, month3Status, bindFunToUpdate):
        self.variableOfRegion = tk.StringVar()
        self.frame = frame
        self.ttk = ttk
        self.tk = tk
        self.drugList = drugList
        self.regionCheckbuttonList = regionCheckbuttonList
        self.data = data
        self.row = row
        self.month1Status = month1Status
        self.month2Status = month2Status
        self.month3Status = month3Status
        self.bindFutToUpdate = bindFunToUpdate

    def createRow(self):
        comboRegion = self.ttk.Combobox(
            self.frame, textvariable=self.variableOfRegion, value=self.drugList, width=38)
        comboRegion['state'] = 'readonly'
        comboRegion.current(0)
        comboRegion.grid(row=self.row, column=0)

        # MAIN COLUMN
        self.mainDrugPriceVar = self.tk.StringVar()
        mainDrugPrice = self.ttk.Entry(
            self.frame, width=7,  textvariable=self.mainDrugPriceVar, justify='center')
        mainDrugPrice.grid(padx=2, row=self.row, column=1)

        self.mainMoneyPlanVar = self.tk.StringVar()
        mainMoney = self.ttk.Entry(self.frame, width=8,
                                   textvariable=self.mainMoneyPlanVar, justify='center')
        mainMoney.grid(padx=0, row=self.row, column=2)

        self.mainPlanPackVar = self.tk.StringVar()
        mainPlanPack = self.tk.Label(self.frame, width=5, bg="#EBEBEB", text='Упак',
                                     textvariable=self.mainPlanPackVar)  # "#EBEBEB"
        mainPlanPack.grid(padx=3, row=self.row, column=3)

        self.mainMoneyFactVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=7, text='ГРОШІ',
                      bg="#EBEBEB", textvariable=self.mainMoneyFactVar).grid(row=self.row, column=4)

        self.mainPacksFactVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='УПАК', bg="#EBEBEB",
                      textvariable=self.mainPacksFactVar).grid(padx=2, row=self.row, column=5)

        self.mainPercentVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='%', bg="#EBEBEB",
                      textvariable=self.mainPercentVar).grid(row=self.row, column=6)
        # MONTH 1
        self.Month1DrugPriceVar = self.tk.StringVar()
        month1DrugPrice = self.ttk.Entry(self.frame, width=7, text='*ЦІНА*',
                                         textvariable=self.Month1DrugPriceVar, justify='center')
        month1DrugPrice.grid(padx=2, row=self.row, column=7, sticky="e")

        self.Month1MoneyPalnVar = self.tk.StringVar()
        month1MoneyPlan = self.ttk.Entry(self.frame, width=8, text='*ГРОШІ*',
                                         textvariable=self.Month1MoneyPalnVar, justify='center')
        month1MoneyPlan.grid(padx=1, row=self.row, column=8)

        self.Month1PacksPlanVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='*УПАК*',
                      bg="#EBEBEB", textvariable=self.Month1PacksPlanVar).grid(padx=3, row=self.row, column=9)

        self.Month1MoneyFactVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=7, text='ГРОШІ',
                      textvariable=self.Month1MoneyFactVar, bg="#EBEBEB").grid(padx=1, row=self.row, column=10)

        self.Month1PacksVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='УПАК',
                      textvariable=self.Month1PacksVar, bg="#EBEBEB").grid(row=self.row, column=11)

        self.Month1PercentVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='%', bg="#EBEBEB",
                      textvariable=self.Month1PercentVar).grid(padx=2, row=self.row, column=12)

        # MONTH 2
        self.Month2DrugPriceVar = self.tk.StringVar()
        month2DrugPrice = self.ttk.Entry(self.frame, width=7, text='*ЦІНА*',
                                         textvariable=self.Month2DrugPriceVar, justify='center')
        month2DrugPrice.grid(padx=0, row=self.row, column=13, sticky="e")

        self.Month2MoneyPalnVar = self.tk.StringVar()
        month2MoneyPlan = self.ttk.Entry(self.frame, width=8, text='*ГРОШІ*',
                                         textvariable=self.Month2MoneyPalnVar, justify='center')
        month2MoneyPlan.grid(padx=2, row=self.row, column=14)

        self.Month2PacksPlanVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='*УПАК*',
                      bg="#EBEBEB", textvariable=self.Month2PacksPlanVar).grid(padx=1, row=self.row, column=15)

        self.Month2MoneyFactVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=7, text='ГРОШІ',
                      textvariable=self.Month2MoneyFactVar, bg="#EBEBEB").grid(padx=2, row=self.row, column=16)

        self.Month2PacksVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='УПАК',
                      textvariable=self.Month2PacksVar, bg="#EBEBEB").grid(padx=0, row=self.row, column=17)

        self.Month2PercentVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='%', bg="#EBEBEB",
                      textvariable=self.Month2PercentVar).grid(padx=2, row=self.row, column=18)

        # MONTH 3
        self.Month3DrugPriceVar = self.tk.StringVar()
        month3DrugPrice = self.ttk.Entry(self.frame, width=7, text='*ЦІНА*',
                                         textvariable=self.Month3DrugPriceVar, justify='center')
        month3DrugPrice.grid(padx=1, row=self.row, column=19, sticky="e")

        self.Month3MoneyPalnVar = self.tk.StringVar()
        month3MoneyPlan = self.ttk.Entry(self.frame, width=8, text='*ГРОШІ*',
                                         textvariable=self.Month3MoneyPalnVar, justify='center')
        month3MoneyPlan.grid(padx=1, row=self.row, column=20)

        self.Month3PacksPlanVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='*УПАК*',
                      bg="#EBEBEB", textvariable=self.Month3PacksPlanVar).grid(padx=2, row=self.row, column=21)

        self.Month3MoneyFactVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=7, text='ГРОШІ',
                      textvariable=self.Month3MoneyFactVar, bg="#EBEBEB").grid(padx=1, row=self.row, column=22)

        self.Month3PacksVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='УПАК',
                      textvariable=self.Month3PacksVar, bg="#EBEBEB").grid(padx=1, row=self.row, column=23)

        self.Month3PercentVar = self.tk.StringVar()
        self.tk.Label(self.frame, width=5, text='%', bg="#EBEBEB",
                      textvariable=self.Month3PercentVar).grid(padx=1, row=self.row, column=24)

        comboRegion.bind("<<ComboboxSelected>>",
                         lambda x: self.bindFutToUpdate())
        mainDrugPrice.bind("<Return>", lambda x: self.updateInfoGui())
        mainMoney.bind("<Return>", lambda x: self.bindFutToUpdate())
        month1DrugPrice.bind("<Return>", lambda x: self.updateInfoGui())
        month1MoneyPlan.bind("<Return>", lambda x: self.bindFutToUpdate())
        month2DrugPrice.bind("<Return>", lambda x: self.updateInfoGui())
        month2MoneyPlan.bind("<Return>", lambda x: self.bindFutToUpdate())
        month3DrugPrice.bind("<Return>", lambda x: self.updateInfoGui())
        month3MoneyPlan.bind("<Return>", lambda x: self.bindFutToUpdate())

    def updateInfoGui(self):
        # print("class GuiRow, fun updateInfoGui: START")
        self.countMainPlanPack()
        self.countMonthPlanPack(self.Month1DrugPriceVar.get(),
                                self.Month1MoneyPalnVar.get(),
                                self.Month1PacksPlanVar)

        self.countMonthPlanPack(self.Month2DrugPriceVar.get(),
                                self.Month2MoneyPalnVar.get(),
                                self.Month2PacksPlanVar)
        self.countMonthPlanPack(self.Month3DrugPriceVar.get(),
                                self.Month3MoneyPalnVar.get(),
                                self.Month3PacksPlanVar)

        self.getSumByDrugAndRegions(self.data.dataBaDM1,
                                    self.data.dataKoneks1,
                                    self.data.dataVenta1,
                                    self.data.dataOptima1,
                                    self.Month1PacksVar,
                                    self.Month1MoneyFactVar,
                                    self.month1Status)

        self.getSumByDrugAndRegions(self.data.dataBaDM2,
                                    self.data.dataKoneks2,
                                    self.data.dataVenta2,
                                    self.data.dataOptima2,
                                    self.Month2PacksVar,
                                    self.Month2MoneyFactVar,
                                    self.month2Status)

        self.getSumByDrugAndRegions(self.data.dataBaDM3,
                                    self.data.dataKoneks3,
                                    self.data.dataVenta3,
                                    self.data.dataOptima3,
                                    self.Month3PacksVar,
                                    self.Month3MoneyFactVar,
                                    self.month3Status)

        self.countPercentMonth(self.Month1MoneyPalnVar,
                               self.Month1MoneyFactVar,
                               self.Month1PercentVar)

        self.countPercentMonth(self.Month2MoneyPalnVar,
                               self.Month2MoneyFactVar,
                               self.Month2PercentVar)

        self.countPercentMonth(self.Month3MoneyPalnVar,
                               self.Month3MoneyFactVar,
                               self.Month3PercentVar)

        self.countPercentMonth(self.Month3MoneyPalnVar,
                               self.Month3MoneyFactVar,
                               self.Month3PercentVar)

        self.countTotalFactMoney(self.Month1MoneyFactVar,
                                 self.Month2MoneyFactVar,
                                 self.Month3MoneyFactVar,
                                 self.mainMoneyFactVar)

        self.countTotalFactPacks(self.Month1PacksVar,
                                 self.Month2PacksVar,
                                 self.Month3PacksVar,
                                 self.mainPacksFactVar)
        # TOTAL PERCENTE
        self.countPercentMonth(self.mainMoneyPlanVar,
                               self.mainMoneyFactVar,
                               self.mainPercentVar)

    def replaceDotForComma(self, string):
        newString = ''
        if ',' in string or "," in string:
            newString = string.replace(",", ".")
            return newString
        else:
            return string

    def getRegionsFromCheckbuttons(self):
        regionSetList = []
        for listObject in self.regionCheckbuttonList:
            if listObject.var.get() == True:
                regionSetList.append(listObject.name)
        return regionSetList

    def countMainPlanPack(self):
        if self.mainDrugPriceVar.get() == '' or self.mainMoneyPlanVar.get() == '':
            pass
        else:
            mainDrugPrice = self.replaceDotForComma(
                self.mainDrugPriceVar.get())
            mainDrugPrice = float(mainDrugPrice)
            mainMoneyVar = self.replaceDotForComma(self.mainMoneyPlanVar.get())
            mainMoneyVar = float(mainMoneyVar)
            mainPlanPack = round((mainMoneyVar/mainDrugPrice), 0)
            mainPlanPack = int(mainPlanPack)
            self.mainPlanPackVar.set(mainPlanPack)

    def countMonthPlanPack(self, monthDrugPriceVar, monthMoneyVar, monthPacksPlanVar):

        if monthDrugPriceVar == '' or monthMoneyVar == '':
            pass
        else:
            monthDrugPrice = self.replaceDotForComma(monthDrugPriceVar)
            monthDrugPrice = float(monthDrugPrice)
            monthMoneyVar = self.replaceDotForComma(monthMoneyVar)
            monthMoneyVar = float(monthMoneyVar)
            monthPlanPack = round((monthMoneyVar/monthDrugPrice), 0)
            monthPlanPack = int(monthPlanPack)
            monthPacksPlanVar.set(monthPlanPack)

    def countPercentMonth(self, MonthMoneyPalnVar, MonthMoneyFactVar, MonthPercentVar):
        # print("countPercentMonth: START")

        month1MoneyPlanVar = self.replaceDotForComma(
            MonthMoneyPalnVar.get())
        month1MoneyFactVar = self.replaceDotForComma(
            MonthMoneyFactVar.get())

        # print(month1MoneyPlanVar, month1MoneyFactVar)

        monthPercent = float((float(month1MoneyFactVar)*100) /
                             float(month1MoneyPlanVar))
        monthPercent = round(monthPercent, 1)

        MonthPercentVar.set((monthPercent))

    def countTotalFactMoney(self, Month1MoneyFactVar, Month2MoneyFactVar, Month3MoneyFactVar, TotalMoneyFactVar):
        Month1MoneyFactVar = int(
            self.replaceDotForComma(Month1MoneyFactVar.get()))
        Month2MoneyFactVar = int(
            self.replaceDotForComma(Month2MoneyFactVar.get()))
        Month3MoneyFactVar = int(
            self.replaceDotForComma(Month3MoneyFactVar.get()))
        TotalMoneyFactVar.set(Month1MoneyFactVar +
                              Month2MoneyFactVar +
                              Month3MoneyFactVar)

    def countTotalFactPacks(self, Month1FactPacksVar, Month2FactPacksVar, Month3FactPacksVar, MonthTotalFactPacksVar):
        Month1FactPacksVar = int(Month1FactPacksVar.get())
        Month2FactPacksVar = int(Month2FactPacksVar.get())
        Month3FactPacksVar = int(Month3FactPacksVar.get())
        MonthTotalFactPacksVar.set(Month1FactPacksVar +
                                   Month2FactPacksVar +
                                   Month3FactPacksVar)

    def getSumByDrugAndRegions(self, BaDM, Koneks, Venta, Optima, MonthPacksVar, MonthMoneyFactVar, monthStatus):
        listOfCombosDrugs = self.getRegionsFromCheckbuttons()
        currentDrug = self.variableOfRegion.get()

        sumSalesBaDM1 = 0
        sumSalesKoneks1 = 0
        sumSalesDataVenta1 = 0
        sumSalesDataOptima1 = 0

        for i in range(len(listOfCombosDrugs)):
            for list in BaDM:
                # print(list['Область'], list['Товар'], list['Количество'])
                if listOfCombosDrugs[i] == list['Область'] and list['Товар'] == currentDrug and monthStatus.get() == True:
                    sumSalesBaDM1 += int(list['Количество'])

        for i in range(len(listOfCombosDrugs)):
            for list in Koneks:
                if listOfCombosDrugs[i] == list['Область України'] and list['Назва продукту'] == currentDrug and monthStatus.get() == True:
                    sumSalesKoneks1 += float(list['Всього, уп'])

        for i in range(len(listOfCombosDrugs)):
            for list in Venta:
                if listOfCombosDrugs[i] == list['Область'] and list['Товар'] == currentDrug and monthStatus.get() == True:
                    sumSalesDataVenta1 += float(list['Сума'])

        for i in range(len(listOfCombosDrugs)):
            for list in Optima:
                if listOfCombosDrugs[i] == list['Область'] and list['Товар'] == currentDrug and monthStatus.get() == True:
                    sumSalesDataOptima1 += float(list['Продажи шт'])

        totalSum1 = int(sumSalesBaDM1+sumSalesKoneks1 +
                        sumSalesDataVenta1+sumSalesDataOptima1)

        MonthPacksVar.set(totalSum1)

        mainDrugPriceVar = self.replaceDotForComma(self.mainDrugPriceVar.get())
        month1Money = int(float(mainDrugPriceVar)*float(totalSum1))
        MonthMoneyFactVar.set(month1Money)

    def setDefoltData(self, i):
        from app.getListFromJson import getListFromJson
        defoltGuiData = getListFromJson("defolt_gui_row_data")
        rowData = defoltGuiData[i]
        # print(rowData)
        drugName = rowData['Препарат']
        planComandPrice = rowData['План команди']['Ціна уп.']
        planComandMoney = rowData['План команди']['Гроші']
        month1Price = rowData['Місяць № 1']['Ціна уп.']
        month1Money = rowData['Місяць № 1']['Гроші']
        month2Price = rowData['Місяць № 2']['Ціна уп.']
        month2Money = rowData['Місяць № 2']['Гроші']
        month3Price = rowData['Місяць № 3']['Ціна уп.']
        month3Money = rowData['Місяць № 3']['Гроші']

        self.variableOfRegion.set(drugName)
        self.mainDrugPriceVar.set(planComandPrice)
        self.mainMoneyPlanVar.set(planComandMoney)
        self.Month1DrugPriceVar.set(month1Price)
        self.Month1MoneyPalnVar.set(month1Money)
        self.Month2DrugPriceVar.set(month2Price)
        self.Month2MoneyPalnVar.set(month2Money)
        self.Month3DrugPriceVar.set(month3Price)
        self.Month3MoneyPalnVar.set(month3Money)

    def returnCurrenRowScreenData(self, listToUpdate):
        listToUpdate["Рядок"].append(int(self.row))
        listToUpdate["Назва препарату"].append(self.variableOfRegion.get())
        listToUpdate["Гроші план"].append(int(self.mainMoneyPlanVar.get()))
        listToUpdate["Упак. план"].append(float(self.mainPlanPackVar.get()))
        listToUpdate["Гроші факт"].append(int(self.mainMoneyFactVar.get()))
        listToUpdate["Упак. факт"].append(int(self.mainPacksFactVar.get()))

        listToUpdate["Гроші палн місяць 1"].append(
            int(self.Month1MoneyPalnVar.get()))
        listToUpdate["Упак. план місяць 1"].append(
            int(self.Month1PacksPlanVar.get()))
        listToUpdate["Гроші факт місяць 1"].append(
            int(self.Month1MoneyFactVar.get()))
        listToUpdate["Упак. факт місяць 1"].append(
            int(self.Month1PacksVar.get()))

        listToUpdate["Гроші палн місяць 2"].append(
            int(self.Month2MoneyPalnVar.get()))
        listToUpdate["Упак. план місяць 2"].append(
            int(self.Month2PacksPlanVar.get()))
        listToUpdate["Гроші факт місяць 2"].append(
            int(self.Month2MoneyFactVar.get()))
        listToUpdate["Упак. факт місяць 2"].append(
            int(self.Month2PacksVar.get()))

        listToUpdate["Гроші палн місяць 3"].append(
            int(self.Month3MoneyPalnVar.get()))
        listToUpdate["Упак. план місяць 3"].append(
            int(self.Month3PacksPlanVar.get()))
        listToUpdate["Гроші факт місяць 3"].append(
            int(self.Month3MoneyFactVar.get()))
        listToUpdate["Упак. факт місяць 3"].append(
            int(self.Month3PacksVar.get()))

        return listToUpdate
