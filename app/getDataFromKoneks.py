from app.findNullRegionInKoneks import findNullRegionInKoneks
from app.openCSV import openCSV
from app.replaceDrugName import replaceDrugName
from app.replaceRegionName import replaceRegionName


def getDataFromKoneks(num):
    # print("getDataFromKoneks: START")

    listFromCSV = openCSV(f'koneks{num}')

    replacedDataKoneks = replaceDrugName(listFromCSV, "Назва продукту")

    replacedDataKoneks = findNullRegionInKoneks(replacedDataKoneks)

    replacedDataKoneks = replaceRegionName(
        replacedDataKoneks, 'Область України')
    # print("getDataFromKoneks: FINISH")
    return replacedDataKoneks
