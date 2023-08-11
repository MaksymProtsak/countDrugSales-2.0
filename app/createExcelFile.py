from datetime import datetime
import json
import xlsxwriter


def createExcelFile(funToUpdateJsonFiles, rowGuiObjectList, nameJsonFileDefoltGuiRowData):
    print("createExcelFile: START")

    # Refresh defolt GUI JSON file
    funToUpdateJsonFiles(rowGuiObjectList, nameJsonFileDefoltGuiRowData)

    # Get cuttend date
    currentDate = datetime.today()
    stringCarrentDate = currentDate.strftime("%d-%m-%Y")

    # print("Current Time =", stringCarrentDate)

    fileNameForSave = f"Підрахунок продажів {stringCarrentDate}"
    # Get address for save a file

    rowIndex = []
    rowSumIndex = []
    with open(f'data\\json\\blocks_index_for_gui_table.json', 'rb') as f:
        blocksGuiTable = json.load(f)

    with open(f'data\\json\\defolt_gui_row_data.json', 'rb') as f:
        defoltGuiRowData = json.load(f)

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook("temp\\excel.xlsx")
    worksheet = workbook.add_worksheet()

    merge_format_bold = workbook.add_format(
        {'align': 'center',
         'valign':   'vcenter',
         'bold':     True,
         'border':   1})

    merge_format = workbook.add_format(
        {'align': 'center',
         'valign':   'vcenter',
         'fg_color': '#87CEFA',
         'border':   1})

    center_format = workbook.add_format(
        {'align': 'center',
         'valign':   'vcenter',
         'border':   1})
    block_format = workbook.add_format(
        {'align': 'right',
         'valign':   'vcenter',
         'border':   1,
         'bold': True,
         'fg_color': '#E8E8E8'})
    text_sum_in_block_format = workbook.add_format(
        {'align': 'center',
         'valign':   'vcenter',
         'border':   1,
         'bold': False,
         'fg_color': '#E8E8E8',
         'num_format': '#0'})
    text_sum_in_block_bold_format = workbook.add_format(
        {'align': 'center',
         'num_format': '#.#0.0',
         'valign':   'vcenter',
         'border':   1,
         'bold': True,
         'fg_color': '#E0E0E0',
         'num_format': '#.#'})

    total_sum_format = workbook.add_format(
        {'align': 'right',
         'valign':   'vcenter',
         'border':   1,
         'bold': True,
         'fg_color': '#D3D3D3'})

    total_sum_number_format = workbook.add_format(
        {'align': 'center',
         'num_format': '#0',
         'valign':   'vcenter',
         'border':   1,
         'bold': False,
         'fg_color': '#D3D3D3'})

    border1_format = workbook.add_format({'border':   1})

    number_format = workbook.add_format({
        'num_format': '#,##0.00',
        'border':   1,
        'align': 'center',
        'valign':   'vcenter'})
    number_format_round0 = workbook.add_format({
        'num_format': '#0',
        'border':   1,
        'align': 'center',
        'valign':   'vcenter'})
    number_format_round1 = workbook.add_format({
        'num_format': '#,#0.0',
        'border':   1,
        'align': 'center',
        'valign':   'vcenter'})
    number_format_round1_bold = workbook.add_format({
        'num_format': '#,#0.0',
        'border':   1,
        'align': 'center',
        'valign':   'vcenter',
        "bold": True})

    number_format_total_sum_round1_bold = workbook.add_format({
        'num_format': '#,#0.0',
        'border':   1,
        'align': 'center',
        'valign':   'vcenter',
        "bold": True,
        'fg_color': '#D0D0D0'})

    def createTableHeadPatern(col, name):
        worksheet.merge_range(
            0, 1+col, 0, 6+col, name, merge_format_bold)
        worksheet.merge_range(1, 1+col, 1, 3+col, "План", merge_format)
        worksheet.merge_range(1, 4+col, 1, 5+col, "Факт", merge_format)
        worksheet.write(2, 1+col, 'Ціна уп.', center_format)
        worksheet.write(2, 2+col, 'Гроші', center_format)
        worksheet.write(2, 3+col, 'Упак.', center_format)
        worksheet.write(2, 4+col, 'Гроші', center_format)
        worksheet.write(2, 5+col, 'Упак', center_format)
        worksheet.merge_range(1, 6+col, 2, 6+col, "%", center_format)
        worksheet.set_column(6+col, 6+col, 5)

    def createTableHead():
        worksheet.set_column(0, 0, 33)
        worksheet.merge_range(0, 0, 2, 0, "Препарати", merge_format_bold)
        createTableHeadPatern(0, "Квартальний план команди")
        createTableHeadPatern(6, "Місяць 1")
        createTableHeadPatern(12, "Місяць 2")
        createTableHeadPatern(18, "Місяць 3")

    def createDrugBlocks():
        for blockKay in blocksGuiTable:
            rowNum = blocksGuiTable[blockKay]["Рядок з сумою"]
            rowValue = blocksGuiTable[blockKay]["Назва рядка"]
            worksheet.write(3+rowNum, 0, rowValue, block_format)
            worksheet.set_row(3+rowNum, 20)

    def getRowIndexFromBlocks():
        for key in blocksGuiTable:
            list = blocksGuiTable[key]['Рядок з даними']
            for num in list:
                rowIndex.append(num)
            rowSumIndex.append(blocksGuiTable[key]["Рядок з сумою"]+4)

    def fillTableFromDefoltGuiRowData():
        for i, index in enumerate(rowIndex):
            # Month main
            rowName = defoltGuiRowData[i]['Препарат']
            mainDrugPrice = float(
                defoltGuiRowData[i]['План команди']['Ціна уп.'])
            mainDrugMoney = int(defoltGuiRowData[i]['План команди']['Гроші'])

            # Month 1
            month1DrugPrice = float(
                defoltGuiRowData[i]['Місяць № 1']['Ціна уп.'])
            month1DrugMoney = int(defoltGuiRowData[i]['Місяць № 1']['Гроші'])
            month1Packs = int(defoltGuiRowData[i]["Місяць № 1"]["Факт Упак"])
            # Month 2
            month2DrugPrice = float(
                defoltGuiRowData[i]['Місяць № 2']['Ціна уп.'])
            month2DrugMoney = int(defoltGuiRowData[i]['Місяць № 2']['Гроші'])
            month2Packs = int(defoltGuiRowData[i]["Місяць № 2"]["Факт Упак"])

            # Month 3
            month3DrugPrice = float(
                defoltGuiRowData[i]['Місяць № 3']['Ціна уп.'])
            month3DrugMoney = int(defoltGuiRowData[i]['Місяць № 3']['Гроші'])
            month3Packs = int(defoltGuiRowData[i]["Місяць № 3"]["Факт Упак"])

            # Month 1
            worksheet.write(3+index, 7, month1DrugPrice, number_format)
            worksheet.write(3+index, 8, month1DrugMoney, number_format_round0)
            worksheet.write(
                3+index, 9, f"=I{4+index}/H{4+index}", number_format_round0)
            worksheet.write(
                3+index, 10, f"=L{4+index}*H{4+index}", number_format_round0)
            worksheet.write(3+index, 11, month1Packs, number_format_round0)
            worksheet.write(
                3+index, 12, f"=K{4+index}*100/I{4+index}", number_format_round1)
            # Month 2
            worksheet.write(3+index, 13, month2DrugPrice, number_format)
            worksheet.write(3+index, 14, month2DrugMoney, number_format_round0)
            worksheet.write(
                3+index, 15, f"=O{4+index}/N{4+index}", number_format_round0)
            worksheet.write(
                3+index, 16, f"=R{4+index}*N{4+index}", number_format_round0)
            worksheet.write(3+index, 17, month2Packs, number_format_round0)
            worksheet.write(
                3+index, 18, f"=Q{4+index}*100/O{4+index}", number_format_round1)
            # Month 3
            worksheet.write(3+index, 19, month3DrugPrice, number_format)
            worksheet.write(3+index, 20, month3DrugMoney, number_format_round0)
            worksheet.write(
                3+index, 21, f"=U{4+index}/T{4+index}", number_format_round0)
            worksheet.write(
                3+index, 22, f"=X{4+index}*T{4+index}", number_format_round0)
            worksheet.write(3+index, 23, month3Packs, number_format_round0)
            worksheet.write(
                3+index, 24, f"=W{4+index}*100/U{4+index}", number_format_round1)
            # Month main
            worksheet.write(3+index, 0, rowName, border1_format)
            worksheet.write(3+index, 1, mainDrugPrice, number_format)
            worksheet.write(3+index, 2, mainDrugMoney, number_format_round0)
            worksheet.write(
                3+index, 3, f"=C{4+index}/B{4+index}", number_format_round0)
            worksheet.write(
                3+index, 4, f"=(K{4+index}+Q{4+index}+W{4+index})", number_format_round0)
            worksheet.write(
                3+index, 5, f"=L{4+index}+R{4+index}+X{4+index}", number_format_round0)
            worksheet.write(
                3+index, 6, f"=E{4+index}*100/C{4+index}", number_format_round1)

    def fillTableSubBlocks():
        for i, key in enumerate(blocksGuiTable):
            listWithSumIndex = blocksGuiTable[key]["Рядок з даними"]
            indexRowWrite = rowSumIndex[i]-1
            indexMin = min(listWithSumIndex)+4
            indexMax = max(listWithSumIndex)+4

            listForFillTable = ["C", 2], ["D", 3], ["E", 4], ["F", 5], [
                "I", 8], ["J", 9], ["K", 10], ["L", 11], [
                "O", 14], ["P", 15], ["Q", 16], ["R", 17], [
                "U", 20], ["V", 21], ["W", 22], ["X", 23]

            for letter, num in listForFillTable:
                worksheet.write(indexRowWrite, num,
                                F"=sum({letter}{indexMin}:{letter}{indexMax})", text_sum_in_block_format)

            for letterOne, LetterTwo, num in ["E", "C", 6], ["K", "I", 12], ["Q", "O", 18], ["W", "U", 24]:
                worksheet.write(indexRowWrite, num,
                                F"={letterOne}{indexRowWrite+1}*100/{LetterTwo}{indexRowWrite+1}", text_sum_in_block_bold_format)

    def fillTableTotalSumRow():
        indexRowForWrite = max(rowSumIndex)
        worksheet.set_row(indexRowForWrite, 20)
        worksheet.write(indexRowForWrite, 0, "РАЗОМ", total_sum_format)

        listForWriteTotalSumRow = ["C", 2], ["D", 3], ["E", 4], ["F", 5], [
            "I", 8], ["J", 9], ["K", 10], ["L", 11], [
            "O", 14], ["P", 15], ["Q", 16], ["R", 17], [
            "U", 20], ["V", 21], ["W", 22], ["X", 23]

        for letterOne, num in listForWriteTotalSumRow:
            sumString = "="
            for index in rowSumIndex:
                sumString += f"{letterOne}{index}+"
            worksheet.write(indexRowForWrite,
                            num,
                            f"{sumString}"[:-1], total_sum_number_format)

        for letterOne, letterTwo, num in ["E", "C", 6], ["K", "I", 12], ["Q", "O", 18], ["W", "U", 24]:
            # print(letterOne, letterTwo, num)
            worksheet.write(indexRowForWrite, num,
                            f"={letterOne}{indexRowForWrite+1}*100/{letterTwo}{indexRowForWrite+1}",
                            number_format_total_sum_round1_bold)

    def setBgColourSumRow():
        blankCell = [1, 7, 13, 19]
        indexRowForWrite = max(rowSumIndex)
        for blockKay in blocksGuiTable:
            rowNum = blocksGuiTable[blockKay]["Рядок з сумою"]
            for index in blankCell:
                worksheet.write(3+rowNum,
                                index,
                                "",
                                text_sum_in_block_format)

                worksheet.write(indexRowForWrite,
                                index,
                                "",
                                total_sum_format)

            # print(3+rowNum)

    createTableHead()
    createDrugBlocks()
    getRowIndexFromBlocks()
    fillTableFromDefoltGuiRowData()
    fillTableSubBlocks()
    fillTableTotalSumRow()
    setBgColourSumRow()

    worksheet.write(max(rowSumIndex)+2, 0,
                    fileNameForSave)

    workbook.close()

    print("createExcelFile: FINISH")
