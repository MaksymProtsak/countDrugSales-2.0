from app.findCityInAddressKoneks import findCityInAddressKoneks


def findNullRegionInKoneks(list):
    # print("findNullRegionInKoneks: START")

    for listObject in list:
        if listObject['Область України'] == '':
            listObject['Область України'] = findCityInAddressKoneks(
                listObject['Адреса клієнта-одержувача'])
            # if listObject['Область України'] == '':
            #     print("listObject: ", listObject['Адреса клієнта-одержувача'])
    # print("findNullRegionInKoneks: FINISH")

    return list
