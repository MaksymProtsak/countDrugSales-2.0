def popNullDrugInVenta(list):
    for i in range(len(list)):
        if list[i]['Товар'] == '':
            list.pop(i)
    return list
