from shutil import copy2
from tkinter import filedialog
from datetime import datetime
import tkinter

from app.createExcelFile import createExcelFile


def exportExcelFile(window, funToUpdateJsonFiles, rowGuiObjectList, nameJsonFileDefoltGuiRowData):
    print("exportExcelFile: START")
    # Destroy option window
    window.destroy()

    # Get cuttend date
    currentDate = datetime.today()
    stringCarrentDate = currentDate.strftime("%d-%m-%Y")

    # Get address for save a file
    fileNameForSave = f"Підрахунок продажів {stringCarrentDate}"

    fileAddress = filedialog.asksaveasfilename(
        filetypes=[("Excel файл", ".xlsx")],
        defaultextension=".xlsx",
        initialfile=fileNameForSave)

    # If address "" end function
    if fileAddress == "":
        return

    # Create excel file from GUI
    createExcelFile(funToUpdateJsonFiles, rowGuiObjectList,
                    nameJsonFileDefoltGuiRowData)

    copy2(f'temp\\excel.xlsx', fileAddress)

    tkinter.messagebox.showinfo(
        "Зберегти EXCEL файл",  f'Файл збережено за адресою: "{fileAddress}"')

    print("exportExcelFile: FINISH")
