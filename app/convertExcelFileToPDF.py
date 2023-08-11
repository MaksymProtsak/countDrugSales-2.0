import os
import win32com.client as win32


def convertExcelFileToPDF(fileAddress):
    print("convertExcelFileToPDF: START")

    fullPathExcelFile = os.path.abspath("temp\\excel.xlsx")

    excel_file = fullPathExcelFile
    pdf_file = os.path.abspath("temp\\pdf.pdf")

    # Open Excel application
    excel = win32.gencache.EnsureDispatch('Excel.Application')

    # Open workbook
    workbook = excel.Workbooks.Open(excel_file)

    # Set print settings
    worksheet = workbook.ActiveSheet
    worksheet.PageSetup.FitToPagesWide = 1
    worksheet.PageSetup.Orientation = 2
    worksheet.PageSetup.TopMargin = 20
    worksheet.PageSetup.LeftMargin = 7
    worksheet.PageSetup.RightMargin = 7
    worksheet.PageSetup.FitToPagesTall = False
    worksheet.PageSetup.Zoom = False
    worksheet.PageSetup.PrintArea = None

    # Export worksheet as PDF
    worksheet.ExportAsFixedFormat(0, pdf_file)

    # Close workbook and Excel application
    workbook.Close(SaveChanges=False)
    excel.Quit()
    print("convertExcelFileToPDF: FINISH")
