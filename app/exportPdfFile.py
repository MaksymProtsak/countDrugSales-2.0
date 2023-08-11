import tkinter
from app.convertExcelFileToPDF import convertExcelFileToPDF
from app.createExcelFile import createExcelFile
from datetime import datetime
from tkinter import filedialog
from shutil import copy2


def exportPdfFile(window, updateDefoltRowDataFileJson, rowGuiObjectList, nameJsonFileDefoltGuiRowData):
    print("exportPdfFile: START")
    # Destroy option window
    window.destroy()

    # Get cuttend date
    currentDate = datetime.today()
    stringCarrentDate = currentDate.strftime("%d-%m-%Y")

    # Get address for save a file
    fileNameForSave = f"Підрахунок продажів {stringCarrentDate}"

    fileAddress = filedialog.asksaveasfilename(
        filetypes=[("PDF файл", ".pdf")],
        defaultextension=".pdf",
        initialfile=fileNameForSave)

    # If address "" end function
    if fileAddress == "":
        return

    # Create excel file
    createExcelFile(updateDefoltRowDataFileJson,
                    rowGuiObjectList, nameJsonFileDefoltGuiRowData)

    # Convert excel file to pdf
    convertExcelFileToPDF(fileAddress)
    #

    # Copy pdf file from temp to fileAddress
    copy2(f'temp\\pdf.pdf', fileAddress)

    tkinter.messagebox.showinfo(
        "Зберегти PDF файл",  f'Файл збережено за адресою: "{fileAddress}"')

    print("exportExcelFile: FINISH")
    print("exportPdfFile: FINISH")
