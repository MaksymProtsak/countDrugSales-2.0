import json
import os
import sys

os.chdir(sys.path[0])


def getListFromJson(name):
    with open(f'data\\json\\{name}.json', 'rb') as f:
        jsonList = json.load(f)

    return jsonList
