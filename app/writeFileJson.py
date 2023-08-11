import json


def writeFileJson(listToWrite, fileName):

    with open(f"data\\json\\{fileName}.json", "w", encoding='utf8') as outfile:
        json.dump(listToWrite, outfile, ensure_ascii=False, indent=4)
