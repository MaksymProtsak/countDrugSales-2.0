from app.getListFromJson import getListFromJson


def createNormalDataListVenta(list):
    normalDataList = []
    regionListVenta = getListFromJson('region_list_venta')

    for listObjectDataVenta in list:
        for listObjectInRegionVenta in regionListVenta:
            drug = listObjectDataVenta["Товар"]
            region = listObjectInRegionVenta
            sum = listObjectDataVenta[listObjectInRegionVenta]
            #print(drug, region, sum)
            if sum == '0':
                pass
            else:
                normalDataList.append(
                    {"Товар": drug, "Область": region, "Сума": sum})
    return normalDataList
