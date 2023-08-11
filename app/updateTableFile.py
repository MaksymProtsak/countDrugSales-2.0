import os
from shutil import copy2
from tkinter import filedialog


def updateTableFile(fileName, typeType, window):
    # print("updateTableFile: START")
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    source = filedialog.askopenfilename(
        initialdir=desktop,
        title=f'Оновити таблицю "{fileName}.{typeType}"',
        filetypes=(("Таблиця Excel", f"{typeType}"),
                   ("all files", "*.*")))

    copy2(source, f'data\\excel\{fileName}.{typeType}')

    # print('updateTableFile: FINISH')
