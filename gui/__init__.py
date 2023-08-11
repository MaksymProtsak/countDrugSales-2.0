import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser
from app.createListFor_use_table_in_data import createListFor_use_table_in_data
from app.exportExcelFile import exportExcelFile
from app.exportPdfFile import exportPdfFile
from app.generateEmailOutlook import generateEmailOutlook
from app.getCreatedDate import getCreatedDate
from app.updateDefoltRowDataFileJson import updateDefoltRowDataFileJson
from app.updateExcelTable import updateExcelTable
from app.writeFileJson import writeFileJson

from clases.CheckButton import CheckButton
from clases.CheckButtonWinStatus import CheckButtonWinStatus
from clases.Data import Data
from clases.ComboRegionList import ComboRegionList
from clases.ExportFiles import ExportFiles
from clases.GuiRow import GuiRow
from clases.GuiSumRow import GuiSumRow
from clases.GuiTotalSumRow import GuiTotalSumRow

from app.getExportStatus import getExportStatus
from app.getListFromJson import getListFromJson
from clases.UseTableInData import UseTableInData


comboRegionListObject = []

checkButtonVarList = []

blocksIndexForGuiTable = getListFromJson("blocks_index_for_gui_table")

rowGUIObjectsList = []

rowGUISumList = []
rowGUITotalSumList = []

buttonList = []

windowList = []
statusRegionObjectList = []  # Objects for regions checkbutton status

data = Data()
root_tk = tk.Tk()


def mainSettings():
    screen_width = root_tk.winfo_screenwidth()
    screen_height = root_tk.winfo_screenheight()
    sizeWindowW = 1440
    sizeWindowH = 630

    marginWindowLeft = int(screen_width/2-sizeWindowW/2)
    marginWindowTOP = int(screen_height/2-sizeWindowH/2)
    root_tk.config(bg='#EBEBEB')
    root_tk.title(
        'Підрахунок продажів')
    root_tk.geometry(
        f'{sizeWindowW}x{sizeWindowH}+{marginWindowLeft}+40')
    root_tk.resizable(False, False)


def createRegionComboFrame(window, funcToUpdate):
    w = LabelFrame(window, text='Області:', padx=5, pady=1, bg="#EBEBEB")
    w.place(x=260-255, y=605, width=250)

    for i in range(4):
        comboRegionListObject.append(
            ComboRegionList(w, ttk, tk, data.regionList, i, funcToUpdate))


def createExportFrame(window):
    w = LabelFrame(window, text='Експорт:', padx=5, pady=1, bg="#EBEBEB")
    w.place(x=5, y=5, width=250)

    exportFilesListObject = []
    exportFilesListObject.append(ExportFiles(w, tk, 0, 'PDF'))
    exportFilesListObject.append(ExportFiles(w, tk, 1, 'Excel'))
    exportFilesListObject.append(ExportFiles(w, tk, 2, 'Outlook'))

    for object in exportFilesListObject:
        object.createGuiObject()

    Button(w, text='Експорт', command=lambda: getExportStatus(exportFilesListObject),
           width=7, cursor="hand2",).grid(column=3, row=0, padx=2)


def createWindowOpt(mainWidow,
                    tk,
                    ttk,
                    funUpdateExcell,
                    updateDataAndUpdateGuiInfo,
                    updateDefoltRowDataFileJson,
                    rowGuiObjectList,
                    nameJsonFileDefoltGuiRowData):

    # Create window
    winOpt = tk.Toplevel(mainWidow)
    # Window settings
    winOpt.title('Опції:')
    screen_width = winOpt.winfo_screenwidth()
    screen_height = winOpt.winfo_screenheight()
    sizeWindowW = 288
    sizeWindowH = 455

    marginWindowLeft = int(screen_width/2-sizeWindowW/2)
    marginWindowTOP = int(screen_height/2-sizeWindowH/2)
    winOpt.config(bg='#EBEBEB')
    winOpt.geometry(
        f'{sizeWindowW}x{sizeWindowH}+{marginWindowLeft}+{75}')
    winOpt.resizable(False, False)
    winOpt.grab_set()

    # Excel files create date
    tableInDataList = []
    fileDate = tk.LabelFrame(winOpt, text='Завантажені таблиці:')
    fileDate.place(x=5, y=0, width=280, height=275)
    fileDateJson = getListFromJson("use_table_in_data")
    for i, object in enumerate(fileDateJson):
        tableInDataList.append(UseTableInData(tk,
                                              ttk,
                                              object["fileName"],
                                              object["dateCreated"],
                                              object["status"],
                                              i,
                                              fileDate))
        tableInDataList[i].createRow()

    # Update frame
    comboFrame = tk.LabelFrame(winOpt, text="Оновити таблицю:")
    comboFrame.place(x=5, y=280, width=280, height=70)

    tk.Label(comboFrame, text="Місяць").grid(row=0, column=0)
    tk.Label(comboFrame, text="Постачальник").grid(row=0, column=1)
    numMonthVar = tk.StringVar()
    numMonthVar.set(1)
    monthCombo = ttk.Combobox(comboFrame,
                              values=[1, 2, 3],
                              width=5,
                              cursor="hand2",
                              textvariable=numMonthVar)
    monthCombo['state'] = 'readonly'
    monthCombo.grid(row=1, column=0, padx=9)

    baseVar = tk.StringVar()
    base = ttk.Combobox(comboFrame,
                        values=["Оптіма", "Вента", "БаДМ", "Конекс"],
                        width=10,
                        cursor="hand2",
                        textvariable=baseVar)
    base['state'] = 'readonly'
    base.grid(row=1, column=1, padx=9)
    base.set("Оптіма")

    updateFile = ttk.Button(comboFrame,
                            text='Оновити файл',
                            cursor="hand2",
                            command=lambda: funUpdateExcell(numMonthVar.get(),
                                                            baseVar.get(),
                                                            winOpt,
                                                            updateDataAndUpdateGuiInfo,
                                                            tableInDataList,
                                                            "use_table_in_data"))
    updateFile.grid(row=1, column=2, padx=9)

    # Export frame
    exportFrame = tk.LabelFrame(winOpt, text="Експорт:", width=280, height=95)
    exportFrame.place(x=5, y=355)

    # Button export pdf
    pdf = tk.PhotoImage(file="img\\pdf\\pdg_black_medium.png")
    btnPdf = tk.Button(exportFrame,
                       border=0,
                       cursor="hand2",
                       command=lambda: exportPdfFile(winOpt,
                                                     updateDefoltRowDataFileJson,
                                                     rowGuiObjectList,
                                                     nameJsonFileDefoltGuiRowData),
                       image=pdf)
    btnPdf.image = pdf
    btnPdf.place(x=15, y=3)

    outlook = tk.PhotoImage(
        file="img\\outlook\\OutlookLogo.contrast-white_scale-140.png")
    btnOutlook = tk.Button(exportFrame,
                           border=0,
                           image=outlook,
                           cursor="hand2",
                           command=lambda: generateEmailOutlook(winOpt,
                                                                rowGUISumList,
                                                                statusRegionObjectList,
                                                                rowGUITotalSumList,
                                                                updateGuiInfo))
    outlook.image = outlook
    btnOutlook.place(x=97, y=2, height=70, width=70)

    excell = tk.PhotoImage(
        file="img\\excell\\ExcelLogoSmall.contrast-white_scale-180.png")
    btnExcell = tk.Button(exportFrame,
                          border=0,
                          cursor="hand2",
                          command=lambda: exportExcelFile(winOpt,
                                                          updateDefoltRowDataFileJson,
                                                          rowGuiObjectList,
                                                          nameJsonFileDefoltGuiRowData),

                          image=excell)
    excell.image = excell
    btnExcell.place(x=192, y=4, height=70, width=75)
    winOpt.protocol("WM_DELETE_WINDOW",
                    lambda: updateDataAndUpdateGuiInfo(winOpt,
                                                       tableInDataList,
                                                       "use_table_in_data"))


def updateDataAndUpdateGuiInfo(window, tableInDataList, fileName):
    # print("updateDataAndUpdateGuiInfo: START")
    listToUpdate = createListFor_use_table_in_data(tableInDataList)
    writeFileJson(listToUpdate, fileName)
    window.destroy()
    data.refresh()
    updateGuiInfo()
    # print("updateDataAndUpdateGuiInfo: FINISH")


def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label


def columnHead(window, x, label):
    padY = 3
    make_label(window, 256+x, 5-padY, 25, 293,
               text=label, background='#ffffff')
    make_label(window, 256+x, 49, 20, 48,
               text='Ціна уп.', background='#ffffff')
    make_label(window, 305+x-49, 31-padY, 20, 104+49,
               text='План', background='#87CEFA')
    make_label(window, 410+x, 31-padY, 20, 97,
               text='Факт', background='#87CEFA')
    make_label(window, 305+x, 52-padY, 20, 57,
               text='Гроші', background='#ffffff')
    make_label(window, 363+x, 52-padY, 20, 45,
               text='Упак.', background='#ffffff')
    make_label(window, 409+x, 52-padY, 20, 55,
               text='Гроші', background='#ffffff')
    make_label(window, 465+x, 52-padY, 20, 42,
               text='Упак.', background='#ffffff')
    make_label(window, 508 + x, 31-padY, 41, 41,
               text='%', background='#ffffff')


def createCheckButtonStatusObjects(list, fileName):
    checkButtonStatus = getListFromJson(fileName)
    for i, key in enumerate(checkButtonStatus):
        list.append(CheckButtonWinStatus(ttk, tk, key))
        list[i].var.set(checkButtonStatus[key])


def actionWinRegionsClose(window, mainCheckbuttonObjectList, tempCheckbuttobObjectList, funToUpdate):
    for i in range(len(mainCheckbuttonObjectList)):
        mainCheckbuttonObjectList[i].var.set(
            tempCheckbuttobObjectList[i].var.get())
    window.destroy()
    funToUpdate()


def createWinRegions(tk, checkButtonStatusObjectList, funToUpdate):
    tempCheckbuttonObjectList = []
    moreOptWin = tk.Toplevel()
    moreOptWin.title('Області:')

    screen_width = moreOptWin.winfo_screenwidth()
    screen_height = moreOptWin.winfo_screenheight()
    sizeWindowW = 220
    sizeWindowH = 530

    marginWindowLeft = int(screen_width/2-sizeWindowW/2)
    marginWindowTOP = int(screen_height/2-sizeWindowH/2)
    moreOptWin.config(bg='#EBEBEB')
    moreOptWin.geometry(
        f'{sizeWindowW}x{sizeWindowH}+{marginWindowLeft}+60')
    moreOptWin.resizable(False, False)
    moreOptWin.grab_set()
    for i, listObject in enumerate(checkButtonStatusObjectList):
        tempCheckbuttonObjectList.append(
            CheckButtonWinStatus(ttk, tk, listObject.name))
        tempCheckbuttonObjectList[i].var.set(listObject.var.get())
        tempCheckbuttonObjectList[i].createCheckbutton(
            moreOptWin, i)

    moreOptWin.protocol("WM_DELETE_WINDOW",
                        lambda: actionWinRegionsClose(moreOptWin, checkButtonStatusObjectList, tempCheckbuttonObjectList, funToUpdate))


def createTableHead(window):
    make_label(window, 5, 2, 67, 250, text='Препарат',
               background='#ffffff')
    columnHead(window, 1, 'Квартальний план команди')
    columnHead(window, 296, '')
    columnHead(window, 591, '')
    columnHead(window, 886, '')


def openAuthorLink():
    webbrowser.open_new("https://tangerine-youtiao-a51230.netlify.app/")


def createAuthorLink():
    authorLink = Label(
        root_tk, text='maksym.protsak@gmail.com', fg="blue", cursor="hand2", bg="#EBEBEB")
    authorLink.place(x=1274, y=607)  # 1162 ,607
    authorLink.bind(
        "<Button-1>", lambda x: openAuthorLink())


def updateGuiInfo():
    for i in range(len(rowGUIObjectsList)):
        rowGUIObjectsList[i].updateInfoGui()

    for i in range(len(rowGUISumList)):
        updateSumRowForBlock(rowGUIObjectsList, f"Блок {i}",
                             blocksIndexForGuiTable, rowGUISumList)

    updateTotalSumRow(rowGUITotalSumList, rowGUISumList)


def createButton(tk, text, x, y, width, command):
    tk.Button(text=text, command=command,
              cursor="hand2", width=width).place(x=x, y=y)


def createCheckbuttonVar(list, tk, window, commandFun):
    # print("createCheckbuttonVar: START")
    list.append(CheckButton(ttk, tk, window, "Місяць 1", commandFun, 665))
    list.append(CheckButton(ttk, tk, window, "Місяць 2", commandFun, 958))
    list.append(CheckButton(ttk, tk, window, "Місяць 3", commandFun, 1255))
    for listObject in list:
        listObject.createCheckbutton()
    # print(list)
    # print("createCheckbuttonVar: FINISH")
    return list


def createListGuiRowObjects(list, blockList, window, ttk, tk, dataDrugList, checkbuttonListObject, data, month1CheckboxVar, month2CheckboxVar, month3CheckboxVar):
    # Create rowObject
    for row in blockList:
        list.append(GuiRow(window, ttk, tk, dataDrugList,
                    checkbuttonListObject, data, row, month1CheckboxVar, month2CheckboxVar, month3CheckboxVar, updateGuiInfo))
    # Create row
    for listObject in list:
        listObject.createRow()


def setDefoltGuiRowData(list):
    for i in range(len(list)):
        list[i].setDefoltData(i)


def setDefoltGuiRegion(listObjects):
    for i in range(len(listObjects)):
        listObjects[i].setGuiDefotlGegion(i)


def setDefoltGuiCheckbuttons(list, jsonFile):
    fileWithData = getListFromJson(jsonFile)
    for i in range(len(list)):
        list[i].checkVar.set(fileWithData[f"Місяць {i+1}"])


def createGUISumRows(row, rowFrame,  tk, rowName):
    rowGUISumList.append(GuiSumRow(rowFrame, tk,  row, rowName))
    for listObject in rowGUISumList:
        listObject.createRow()


def getInfoFromGuiRowObject(guiRowObjectsList):
    # print("getInfoFromGuiRowObject: START")
    infoList = getListFromJson("infoList_for_returnCurrenRowScreenData")
    for listObject in guiRowObjectsList:
        listObject.returnCurrenRowScreenData(infoList)

    # print("getInfoFromGuiRowObject: FINISH")
    return infoList


def updateSumRowForBlock(guiObjectsList, blockName, indexTable, rowGuiSumList):
    # print("updateSumRowForBlock: START")
    # print(blockName)
    # print(indexTable)

    infoFromCurrentGui = getInfoFromGuiRowObject(guiObjectsList)
    # print(infoFromCurrentGui)
    indexForRowSum = indexTable[blockName]['Рядок з даними']
    moneyPlan = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Гроші план')
    packsPlan = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Упак. план')
    moneyFact = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Гроші факт')
    packsFact = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Упак. факт')
    # Manth 1
    moneyManth1Plan = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Гроші палн місяць 1')
    moneyManth1PacksPlan = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Упак. план місяць 1')
    moneyManth1Fact = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Гроші факт місяць 1')
    moneyManth1PacksFact = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Упак. факт місяць 1')
    # print(packsPlan)

    # Manth 2
    moneyManth2Plan = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Гроші палн місяць 2')
    moneyManth2PacksPlan = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Упак. план місяць 2')
    moneyManth2Fact = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Гроші факт місяць 2')
    moneyManth2PacksFact = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Упак. факт місяць 2')

    # Manth 3
    moneyManth3Plan = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Гроші палн місяць 3')
    moneyManth3PacksPlan = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Упак. план місяць 3')
    moneyManth3Fact = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Гроші факт місяць 3')
    moneyManth3PacksFact = getDataByIndex(
        indexForRowSum, infoFromCurrentGui, 'Упак. факт місяць 3')

    setDataMoneyPlan(indexTable, blockName, moneyPlan, rowGuiSumList)
    setDataPacksPlan(indexTable, blockName, packsPlan, rowGuiSumList)
    setDataMoneyFact(indexTable, blockName, moneyFact, rowGuiSumList)
    setDataPacksFact(indexTable, blockName, packsFact, rowGuiSumList)
    setDataPercent(indexTable, blockName, rowGuiSumList)
    # Manth 1
    setManth1MoneyPlan(indexTable, blockName, moneyManth1Plan, rowGuiSumList)
    setManth1PacksPlan(indexTable, blockName,
                       moneyManth1PacksPlan, rowGuiSumList)
    setManth1MoneyFact(indexTable, blockName, moneyManth1Fact, rowGuiSumList)
    setManth1PacksFact(indexTable, blockName,
                       moneyManth1PacksFact, rowGuiSumList)
    setDataMonth1Percent(indexTable, blockName, rowGuiSumList)

    # Manth 2
    setManth2MoneyPlan(indexTable, blockName, moneyManth2Plan, rowGuiSumList)
    setManth2PacksPlan(indexTable, blockName,
                       moneyManth2PacksPlan, rowGuiSumList)
    setManth2MoneyFact(indexTable, blockName, moneyManth2Fact, rowGuiSumList)
    setManth2PacksFact(indexTable, blockName,
                       moneyManth2PacksFact, rowGuiSumList)
    setDataMonth2Percent(indexTable, blockName, rowGuiSumList)
    # Manth 3
    setManth3MoneyPlan(indexTable, blockName, moneyManth3Plan, rowGuiSumList)
    setManth3PacksPlan(indexTable, blockName,
                       moneyManth3PacksPlan, rowGuiSumList)
    setManth3MoneyFact(indexTable, blockName, moneyManth3Fact, rowGuiSumList)
    setManth3PacksFact(indexTable, blockName,
                       moneyManth3PacksFact, rowGuiSumList)
    setDataMonth3Percent(indexTable, blockName, rowGuiSumList)


def getDataByIndex(indexForRowSum, infoFromCurrentGui, key):
    sum = 0
    for listObject in indexForRowSum:
        indexForSum = infoFromCurrentGui['Рядок'].index(listObject)
        # print(indexForSum)
        get = infoFromCurrentGui[key][indexForSum]
        # print(get)
        sum += get
        # print(sum)
    return sum


def setDataMoneyPlan(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setDataMoneyPlan(sum)


def setDataPacksPlan(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setDataPacksPlan(sum)


def setDataMoneyFact(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setDataMoneyFact(sum)


def setDataPacksFact(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setDataPacksFact(sum)


def setDataPercent(indexTable, blockName, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.countPercent()

# Manth 1


def setManth1MoneyPlan(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth1MoneyPlan(sum)


def setManth1PacksPlan(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth1PacksPlan(sum)


def setManth1MoneyFact(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth1MoneyFact(sum)


def setManth1PacksFact(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth1PacksyFact(sum)


def setDataMonth1Percent(indexTable, blockName, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.countPercentManth1()

# Manth 2


def setManth2MoneyPlan(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth2MoneyPlan(sum)


def setManth2PacksPlan(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth2PacksPlan(sum)


def setManth2MoneyFact(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth2MoneyFact(sum)


def setManth2PacksFact(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth2PacksyFact(sum)


def setDataMonth2Percent(indexTable, blockName, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.countPercentManth2()

# Manth 3


def setManth3MoneyPlan(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth3MoneyPlan(sum)


def setManth3PacksPlan(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth3PacksPlan(sum)


def setManth3MoneyFact(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth3MoneyFact(sum)


def setManth3PacksFact(indexTable, blockName, sum, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.setManth3PacksyFact(sum)


def setDataMonth3Percent(indexTable, blockName, rowGuiSumList):
    indexRowSum = indexTable[blockName]['Рядок з сумою']
    for listObject in rowGuiSumList:
        if listObject.row == indexRowSum:
            # print("listObject.row: ", listObject.row)
            listObject.countPercentManth3()


def createBlockGui(blokIndexList, numBlock):
    indexRowList = blokIndexList[numBlock]['Рядок з даними']
    indexRowSum = blokIndexList[numBlock]['Рядок з сумою']
    rowName = blokIndexList[numBlock]['Назва рядка']

    createListGuiRowObjects(rowGUIObjectsList, indexRowList, rowFrame, ttk, tk, data.drugList,
                            statusRegionObjectList, data, checkButtonVarList[0].checkVar, checkButtonVarList[1].checkVar, checkButtonVarList[2].checkVar)
    createGUISumRows(indexRowSum, rowFrame, tk, rowName)


def createBlocks(rangeRows):
    for i in range(rangeRows):
        createBlockGui(blocksIndexForGuiTable, f"Блок {i}")


def createTotalSumRow(rowGUITotalTubList):
    rowGUITotalTubList.append(GuiTotalSumRow(rowFrame, tk, 23))
    rowGUITotalTubList[0].createRow()
    pass


def updateTotalSumRow(guiTotalSumList, guiSumList):
    # print("updateTotalSumRow: START")
    sumTotalMoneyPlan = 0
    sumMainPacksPlan = 0
    sumMainMoneyPlan = 0
    sumMainPacksFact = 0

    sumManth1MoneyPlan = 0
    sumManth1PacksPlan = 0
    sumManth1MoneyFact = 0
    sumManth1PacksFact = 0

    sumManth2MoneyPlan = 0
    sumManth2PacksPlan = 0
    sumManth2MoneyFact = 0
    sumManth2PacksFact = 0

    sumManth3MoneyPlan = 0
    sumManth3PacksPlan = 0
    sumManth3MoneyFact = 0
    sumManth3PacksFact = 0

    for listObject in guiSumList:
        sumTotalMoneyPlan += listObject.rowMoneyPlanVar.get()
        sumMainPacksPlan += listObject.rowPacksPlanVar.get()
        sumMainMoneyPlan += listObject.rowMoneyFactVar.get()
        sumMainPacksFact += listObject.rowPacksFactVar.get()

        sumManth1MoneyPlan += listObject.rowManth1MoneyPlanVar.get()
        sumManth1PacksPlan += listObject.rowManth1PacksPlanVar.get()
        sumManth1MoneyFact += listObject.rowManth1MoneyFactVar.get()
        sumManth1PacksFact += listObject.rowManth1PacksFactVar.get()

        sumManth2MoneyPlan += listObject.rowManth2MoneyPlanVar.get()
        sumManth2PacksPlan += listObject.rowManth2PacksPlanVar.get()
        sumManth2MoneyFact += listObject.rowManth2MoneyFactVar.get()
        sumManth2PacksFact += listObject.rowManth2PacksFactVar.get()

        sumManth3MoneyPlan += listObject.rowManth3MoneyPlanVar.get()
        sumManth3PacksPlan += listObject.rowManth3PacksPlanVar.get()
        sumManth3MoneyFact += listObject.rowManth3MoneyFactVar.get()
        sumManth3PacksFact += listObject.rowManth3PacksFactVar.get()

    guiTotalSumList[0].setData(
        sumTotalMoneyPlan,
        sumMainPacksPlan,
        sumMainMoneyPlan,
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
        sumManth3PacksFact)


def checkProgramClose(window,
                      rowObjectList,
                      checkButtonsObjectList,
                      checkbuttonListObject,
                      fileToWriteDefoltDrowData,
                      fileToWriteDefoltCheckbuttons,
                      fileToWriteDefoltRegion):
    window.protocol("WM_DELETE_WINDOW",
                    lambda: getInfoFromGui(window,
                                           rowObjectList,
                                           checkButtonsObjectList,
                                           checkbuttonListObject,
                                           fileToWriteDefoltDrowData,
                                           fileToWriteDefoltCheckbuttons,
                                           fileToWriteDefoltRegion))


def getInfoFromGui(window,
                   rowObjectList,
                   checkButtonsObjectList,
                   checkbuttonListObject,
                   fileToWriteDefoltRowData,
                   fileToWriteDefoltCheckbuttons,
                   fileToWriteDefoltRegion):

    from app.getListFromJson import getListFromJson
    from app.writeFileJson import writeFileJson
    fileToEditDefoltCheckbuttons = getListFromJson(
        fileToWriteDefoltCheckbuttons)
    fileToEditDefoltRegions = getListFromJson(fileToWriteDefoltRegion)

    # Write Row status to the file
    updateDefoltRowDataFileJson(rowObjectList, fileToWriteDefoltRowData)

    for i in range(len(checkButtonsObjectList)):

        fileToEditDefoltCheckbuttons[f"Місяць {1+i}"] = checkButtonsObjectList[i].checkVar.get()

    writeFileJson(fileToEditDefoltCheckbuttons, fileToWriteDefoltCheckbuttons)

    # Write checkButton status to the file
    for i, listObject in enumerate(checkbuttonListObject):
        fileToEditDefoltRegions[listObject.name] = checkbuttonListObject[i].var.get(
        )
    writeFileJson(fileToEditDefoltRegions, fileToWriteDefoltRegion)
    window.destroy()


mainSettings()
# createRegionComboFrame(root_tk, updateGuiInfo)
createTableHead(root_tk)

# Create  objects for window More options
createCheckButtonStatusObjects(statusRegionObjectList,
                               "checkbutton_region_status")

rowFrame = Frame(root_tk, bg="#EBEBEB", width=300, height=200)
rowFrame.place(x=5, y=72)

buttonList.append(createButton(ttk,
                               'Області',
                               5,
                               568+15+10,
                               8,
                               lambda: createWinRegions(
                                   tk, statusRegionObjectList, updateGuiInfo)
                               ))  # 5, 568 , '⚙ Більше опцій ⚙'
buttonList.append(createButton(ttk,
                               'Опції',
                               5+50+10+5-2,
                               568+15+10,
                               6,
                               lambda: createWindowOpt(root_tk,
                                                       tk,
                                                       ttk,
                                                       updateExcelTable,
                                                       updateDataAndUpdateGuiInfo,
                                                       updateDefoltRowDataFileJson,
                                                       rowGUIObjectsList,
                                                       "defolt_gui_row_data")))
buttonList.append(createButton(ttk,
                               'По областях',
                               5+120-7,
                               568+15+10,
                               12,
                               lambda: getCreatedDate()))  # 5, 568 , '⚙ Більше опцій ⚙'
createCheckbuttonVar(checkButtonVarList, tk, root_tk, updateGuiInfo)
make_label(root_tk, 5, 580, 1, 1350+80,
           background='#87CEFA')  # x = 137, w = 1210
make_label(root_tk, 207, 605, 1, 1228,
           background='#87CEFA')  # x = 207, w = 1140

createBlocks(7)  # Should be 7
createTotalSumRow(rowGUITotalSumList)
createAuthorLink()

setDefoltGuiRowData(rowGUIObjectsList)
setDefoltGuiCheckbuttons(checkButtonVarList, "defolt_set_gui_checkButtons")
# setDefoltGuiRegion(comboRegionListObject)

updateGuiInfo()

checkProgramClose(root_tk,
                  rowGUIObjectsList,
                  checkButtonVarList,
                  statusRegionObjectList,
                  "defolt_gui_row_data",
                  "defolt_set_gui_checkButtons",
                  "checkbutton_region_status")
# createExportFrame(root_tk)
root_tk.mainloop()
