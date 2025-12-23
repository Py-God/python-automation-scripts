import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):  # create some data in column A
    sheet['A' + str(i)] = i

refObj = openpyxl.chart.Reference(sheet, min_row=1, min_col=1, max_col=1, max_row=10)
seriesObj = openpyxl.chart.Series(refObj, title='First series')
chartObj = openpyxl.chart.BarChart()

chartObj.append(seriesObj)
chartObj.height = 10
chartObj.width = 20
sheet.add_chart(chartObj)
wb.save('C:\\Users\\user\\Desktop\\PYTHON\\sampleChart.xlsx')
