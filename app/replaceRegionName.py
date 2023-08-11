from app.getListFromJson import getListFromJson


def replaceRegionName(list, region):
    keysDrugList = getListFromJson('keys_region_list')
    for listObject in list:
        listObject[region] = keysDrugList[listObject[region]]
    return list
