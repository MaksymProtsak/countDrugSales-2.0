from app.getListFromJson import getListFromJson


def getExcelFileNameByBaseAndMonth(numMonth, base):

    fileJson = getListFromJson("key_excell_name_for_update")
    name = fileJson[base]
    extension = fileJson[name]
    fileNameExcell = f"{name}{numMonth}"
    # print(fileNameExcell)
    return {"name": fileNameExcell, "extension": extension}
