from app.getListFromJson import getListFromJson


def replaceDrugName(list, key):
    keysDrugList = getListFromJson('keys_drug_list')
    for listObject in list:
        listObject[key] = keysDrugList[listObject[key]]
    return list
