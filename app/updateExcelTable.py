from tkinter import Tk
from app.convertExcelToCSV import convertExcelToCSV
from app.getCreatedDate import getCreatedDate
from app.getExcelFileNameByBaseAndMonth import getExcelFileNameByBaseAndMonth
from app.updateTableFile import updateTableFile


def updateExcelTable(numMonth, base, window, funAfterDestroy, tableInDataList, fileName):
    print("updateExcelTable: START")
    window.destroy()
    fileToUpdate = getExcelFileNameByBaseAndMonth(numMonth, base)

    updateTableFile(fileToUpdate["name"], fileToUpdate["extension"], window)
    # Convert file after copy

    if base == "БаДМ":
        print("updateExcelTable: START to convert BADM")

        convertExcelToCSV(f'badm{numMonth}', 'xlsx', 0, [1, 3, 7], "Товар")
        print("updateExcelTable: FINISH to convert BADM")

    elif base == "Оптіма":
        # print("updateExcelTable: START TO CONVERT OPTIMA")
        convertExcelToCSV(f'optima{numMonth}', 'xlsx',
                          0, [0, 8, 11], "Область")

    elif base == "Вента":
        # print("updateExcelTable: START TO CONVERT VENTA")

        list = [num for num in range(1, 27)]
        convertExcelToCSV(f'venta{numMonth}', 'xls', 0, list, "Вінницька")

    elif base == "Конекс":
        # print("updateExcelTable: START TO CONVERT KONEKS")
        convertExcelToCSV(f'koneks{numMonth}', 'xls', 5, [
                          1, 4, 16, 17], "Всього, уп")

    getCreatedDate()

    window.destroy()
    funAfterDestroy(window, tableInDataList, fileName)
    print("updateExcelTable: START")
