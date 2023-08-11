from app.convertExcelToCSV import convertExcelToCSV
from app.openCSV import openCSV


def getDataFromOptima(num):
    # convertExcelToCSV(f'optima{num}', 'xlsx', 0, [0, 8, 11])
    listFromCSV = openCSV(f'optima{num}')
    return listFromCSV
