from app.convertExcelToCSV import convertExcelToCSV
from app.openCSV import openCSV
from app.replaceDrugName import replaceDrugName
from app.replaceRegionName import replaceRegionName


def getDataFromBaDM(num):
    listFromCSV = openCSV(f'badm{num}')
    replacedDataBaDM = replaceDrugName(listFromCSV, 'Товар')
    replacedDataBaDM = replaceRegionName(replacedDataBaDM, 'Область')
    # print(listFromCSV)
    return replacedDataBaDM
