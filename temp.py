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
header={"Name of test Case":"","User Name":"","Host Name":"","Time Started":"","Time Ended":"","Pass Count":"","Fail Count":""}

def listDir(dir):
    fileNames = os.listdir(dir)
    temp = []
    for fileName in fileNames:
        temp.append(fileName)
    return temp


if __name__ == "__main__":
    fileNameList = listDir(Folder_Path)
    sheetRow = 0
    sheetCol = 0
    for key in header:
        sheet1.write(sheetRow,sheetCol,key)
        sheetCol+=1
    for roots, dirs, files in os.walk(
        r"C:\\Users\\USER\\Documents\\Ifastools\\", topdown=False
    ):
        for name in files:
            if os.path.splitext(name)[0]!="Summary" and os.path.splitext(name)[1] == ".html":
                fullPath = roots + "\\" + name
                filepath = fullPath
                sheetRow = sheetRow + 1
                sheetCol = 0
                sheet1.write(sheetRow, sheetCol, json.dumps(name))
                sheetCol = sheetCol + 1
                f = open(filepath, encoding="utf8")
                soup = BeautifulSoup(f, "lxml")
                rows = soup.findAll("tr")
                print("FilePath is ", filepath)
                failCase=0
                passCase=0
                for row in rows:
                    data = row.find_all("td")
                    for cells in data:
                        ctr=0
                        for cell in cells:
                            ctr+=1
                            print(type(cell))
                            if(ctr==2):
                                sheet1.write(sheetRow,sheetCol,cell.strip())
                                sheetCol+=1
                                print(cell)
                            if(ctr==8):
                                sheet1.write(sheetRow,sheetCol,cell.strip())
                                sheetCol+=1
                                print(cell)
                        if(cells.get('class')):
                            if(cells.get('class')[0] == 'status' ):
                                if(cells.get('class')[1] == 'fail'):
                                    failCase+=1
                                else:
                                    passCase+=1
                            if(cells.get('class')[0]=='step-details'):
                                endTime=cells.text.strip()
                        cell = cells.text.strip()
                        jsonCell = json.dumps(cell)
                        # print(jsonCell)
                sheet1.write(sheetRow,sheetCol,endTime)
                sheetCol+=1
                sheet1.write(sheetRow,sheetCol,passCase)
                sheetCol+=1
                sheet1.write(sheetRow,sheetCol,failCase)
                sheetCol+=1
    wb.save(r"C:\\Users\\USER\\Desktop\\Book1.xls")
