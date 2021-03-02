import os
import filetype
import re
import json
import time
import xlwt
from xlwt import Workbook
from bs4 import BeautifulSoup

wb = Workbook()
sheet1 = wb.add_sheet("Sheet 1")

Folder_Path = r"C:\\Users\\USER\\Documents\\Ifastools"


def listDir(dir):
    fileNames = os.listdir(dir)
    temp = []
    for fileName in fileNames:
        temp.append(fileName)
    return temp


if __name__ == "__main__":
    fileNameList = listDir(Folder_Path)
    sheetRow = 0
    sheetCol = -1
    for roots, dirs, files in os.walk(
        r"C:\\Users\\USER\\Documents\\Ifastools\\", topdown=False
    ):
        for name in files:
            if os.path.splitext(name)[0]!="Summary" and os.path.splitext(name)[1] == ".html":
                # root = re.escape(roots) + "\\"
                fullPath = roots + "\\" + name
                filepath = fullPath
                sheetCol = sheetCol + 1
                sheetRow = 0
                sheet1.write(sheetRow, sheetCol, json.dumps(name))
                sheetRow = sheetRow + 1
                f = open(filepath, encoding="utf8")
                soup = BeautifulSoup(f, "lxml")
                rows = soup.findAll("tr")
                print("FilePath is ", filepath)
                for row in rows:
                    data = row.find_all("td")
                    for cells in data:
                        cell = cells.text.strip()
                        jsonCell = json.dumps(cell)
                        sheet1.write(sheetRow, sheetCol, jsonCell)
                        sheetRow = sheetRow + 1
    wb.save(r"C:\\Users\\USER\\Desktop\\Book1.xls")
