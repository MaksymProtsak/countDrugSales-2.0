import tkinter
import pandas as pd


def convertExcelToCSV(fileName, format, skiprows, usecols, checkKey):
    print("convertExcelToCSV: START")
    read_fileExcel = pd.read_excel(
        f'data\\excel\\{fileName}.{format}',
        skiprows=int(skiprows),
        usecols=usecols)
    for i, object in enumerate(read_fileExcel):
        if i == 1 and object == checkKey:
            print(object, " == ", checkKey)
            read_fileExcel.to_csv(
                f'data\\csv\\{fileName}.csv', index=None, header=True)
            print(
                f"convertExcelToCSV: {fileName}, {format}, {skiprows}, {usecols}")
            tkinter.messagebox.showinfo(
                "Оновити таблицю",  f'Файл {fileName}.{format} оновлено!')
            print("convertExcelToCSV: FINISH")

            return
        elif i == 1 and object != checkKey:
            print(object, " != ", checkKey)
            tkinter.messagebox.showerror(
                f"Оновити таблицю", f"Невірний файл!")
            return
        elif i > 2:
            return
