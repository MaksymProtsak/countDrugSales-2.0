from time import strftime
import pandas as pd

from app.generateHtmlTable import generateHtmlTable


def generateEmailOutlook(windowOpt, sumDrugObjectList, regionObjectList, totalSumDrugObjectList, updateGuiInfo):
    print("generateEmailOutlook: START")
    windowOpt.destroy()

    tableDict = generateHtmlTable(sumDrugObjectList,
                                  regionObjectList,
                                  totalSumDrugObjectList,
                                  updateGuiInfo)
    htmlTable = pd.DataFrame(tableDict)
    htmlTable.style
    # htmlTable.to_html()
    # with open("data\\outlook\\tableTemplate.html", "w") as file:
    #     file.write(htmlTable.to_html(index=False, justify="center"))

    with open('data\\outlook\\mailTo.txt', 'r') as myfile:
        mailTo = myfile.read()
    with open('data\\outlook\\mailCopy.txt', 'r') as myfile:
        mailCC = myfile.read()
    with open('data\\outlook\\mailAuthor.txt', 'r', encoding='utf-8') as myfile:
        mailAuthor = myfile.read()

    subject = f"Виконання плану на {strftime('%d.%m.%Y')}"

    # Destroy temp window

    htmlPage = f"""
    <html>
    <br>Шановні колеги!
    <br>
    <br>У вкладенні файл виконання плану на {strftime('%d.%m.%Y')}
    <br>
    <br>Маємо такі результати:
    <br>
	{htmlTable.to_html(index=False, justify="center")}
    <br>
    <br>Дякую.
    <br>
    <hr>
    <pre style="font-family:'Arial'">
    <font size="12px">
    {mailAuthor}
    </pre>
    </font>
    </html>
    """

    import win32com.client as win32
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = mailTo
    mail.CC = mailCC
    mail.Subject = subject
    mail.HTMLBody = htmlPage
    mail.Display(True)
    print("generateEmailOutlook: FINISH")
