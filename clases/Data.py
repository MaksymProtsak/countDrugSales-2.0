from app.getDataFromBaDM import getDataFromBaDM
from app.getDataFromKoneks import getDataFromKoneks
from app.getDataFromVenta import getDataFromVenta
from app.getListFromJson import getListFromJson
from app.getDataFromOptima import getDataFromOptima


class Data():
    def __init__(self):
        self.refresh()

    def refresh(self):
        self.regionList = getListFromJson('region_list')
        self.drugList = getListFromJson('drug_list')
        self.fileStatus = getListFromJson("use_table_in_data")
        self.dataBaDM1 = []
        self.dataBaDM2 = []
        self.dataBaDM3 = []
        self.dataKoneks1 = []
        self.dataKoneks2 = []
        self.dataKoneks3 = []
        self.dataVenta1 = []
        self.dataVenta2 = []
        self.dataVenta3 = []
        self.dataOptima1 = []
        self.dataOptima2 = []
        self.dataOptima3 = []

        for listObject in self.fileStatus:

            if listObject["fileName"] == "badm1.csv" and listObject["status"] == True:
                self.dataBaDM1 = getDataFromBaDM(1)
            elif listObject["fileName"] == "badm2.csv" and listObject["status"] == True:
                self.dataBaDM2 = getDataFromBaDM(2)
            elif listObject["fileName"] == "badm3.csv" and listObject["status"] == True:
                self.dataBaDM3 = getDataFromBaDM(3)

            if listObject["fileName"] == "koneks1.csv" and listObject["status"] == True:
                self.dataKoneks1 = getDataFromKoneks(1)
            elif listObject["fileName"] == "koneks2.csv" and listObject["status"] == True:
                self.dataKoneks2 = getDataFromKoneks(2)
            elif listObject["fileName"] == "koneks3.csv" and listObject["status"] == True:
                self.dataKoneks3 = getDataFromKoneks(3)

            if listObject["fileName"] == "venta1.csv" and listObject["status"] == True:
                self.dataVenta1 = getDataFromVenta(1)
            elif listObject["fileName"] == "venta2.csv" and listObject["status"] == True:
                self.dataVenta2 = getDataFromVenta(2)
            elif listObject["fileName"] == "venta3.csv" and listObject["status"] == True:
                self.dataVenta3 = getDataFromVenta(3)

            if listObject["fileName"] == "optima1.csv" and listObject["status"] == True:
                self.dataOptima1 = getDataFromOptima(1)
            elif listObject["fileName"] == "optima2.csv" and listObject["status"] == True:
                self.dataOptima2 = getDataFromOptima(2)
            elif listObject["fileName"] == "optima3.csv" and listObject["status"] == True:
                self.dataOptima3 = getDataFromOptima(3)

        # self.dataBaDM1 = getDataFromBaDM(1)
        # self.dataBaDM2 = getDataFromBaDM(2)
        # self.dataBaDM3 = getDataFromBaDM(3)
        # self.dataKoneks1 = getDataFromKoneks(1)
        # self.dataKoneks2 = getDataFromKoneks(2)
        # self.dataKoneks3 = getDataFromKoneks(3)
        # self.dataVenta1 = getDataFromVenta(1)
        # self.dataVenta2 = getDataFromVenta(2)
        # self.dataVenta3 = getDataFromVenta(3)
        # self.dataOptima1 = getDataFromOptima(1)
        # self.dataOptima2 = getDataFromOptima(2)
        # self.dataOptima3 = getDataFromOptima(3)
