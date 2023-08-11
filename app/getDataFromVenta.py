from app.convertExcelToCSV import convertExcelToCSV
from app.createNormalDataListVenta import createNormalDataListVenta
from app.openCSV import openCSV
from app.popNullDrugInVenta import popNullDrugInVenta
from app.replaceDrugName import replaceDrugName
from app.replaceRegionName import replaceRegionName


def getDataFromVenta(num):
    # list = [num for num in range(1, 27)]
    # convertExcelToCSV(f'venta{num}', 'xls', 0, list)
    listFromCSV = openCSV(f'venta{num}')
    listFromCSV = popNullDrugInVenta(listFromCSV)
    replacedDataVenta = replaceDrugName(listFromCSV, 'Товар')
    normalDataListVenta = createNormalDataListVenta(replacedDataVenta)
    replacedDataVenta = replaceRegionName(normalDataListVenta, 'Область')

    return replacedDataVenta
