import datetime
import json
import os


def getCreatedDate():
    print("getCreatedDate: START")
    path = "data\\csv\\"
    filesInFolder = os.listdir(path)
    # print(filesInFolder)

    filesDate = {}
    # Create keys file-> created data
    for fileName in filesInFolder:
        m_time = os.path.getmtime(f"{path}{fileName}")
        dt_m = datetime.datetime.fromtimestamp(m_time)
        date = dt_m.strftime("%d.%m.%Y %H:%M")
        filesDate[fileName] = date

    with open(f"data\\json\\excel_file_created_date.json", "w", encoding='utf8') as outfile:
        json.dump(filesDate, outfile, ensure_ascii=False, indent=4)

    print("getCreatedDate: FINISH")
