#! python3
# this code reads the content of the excel fine and returns the area and perimeter of the lands in it in a dictionary form
import openpyxl, pprint

def areaPerimeter(excelFile):
    output = {}
    wb = openpyxl.load_workbook(excelFile)
    sheet = wb['Sheet1']
    for row in range(1, sheet.max_row +1):
        landName = sheet['A' + str(row)].value
        landLength = sheet['B' + str(row)].value
        landBreath = sheet['C' + str(row)].value

        area = landLength * landBreath
        perimeter = 2*(landBreath + landLength)

        output.setdefault(landName, {})
        output[landName].setdefault('area', area)
        output[landName].setdefault('perimeter', perimeter)

    pprint.pprint(output)

areaPerimeter('lands.xlsx')