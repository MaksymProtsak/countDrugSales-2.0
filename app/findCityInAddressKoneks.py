def findCityInAddressKoneks(string):
    # print("findCityInAddressKoneks: START")
    # print(f"string: {string}")
    string = string.replace(".", " ")
    string = string.replace(",", " ")
    city = ''
    cityList = ['Київ',
                'Киев,',
                'Дніпро',
                'Киів',
                'Слобожанське']
    for i in range(len(cityList)):
        index = string.find(cityList[i])
        if index > 0:
            city = string[index:index+len(cityList[i])]
    if city == 'Киів':
        city = 'Київ'

    if city == "м.Дніпро" or city == "Слобожанське":
        city = "Дніпро"

    # If city anyway '', try second methon to find city
    if city == '':
        # print("findCityInAddressKoneks")
        # print(f'ERROR: "{city}", string: {string}')
        stringInList = string.split(' ')
        # print(stringInList)
        for listObject in stringInList:
            if listObject in cityList:
                city = listObject

    # If city anyway '', try third methon to find city
    if city == '':
        stringInList = string.split(' ')
        for listObject in stringInList:
            if listObject == 'Киев':
                city = "Київ"
    # print("findCityInAddressKoneks: FINISH")

    return city
