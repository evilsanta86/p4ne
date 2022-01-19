from matplotlib import pyplot
from openpyxl import load_workbook

rawdata = load_workbook('data_analysis_lab.xlsx')
sheet = rawdata['Data']
sheet['A'][1:]


def getvalue(x):
    return x.value

#map(getvalue, sheet['A'][1:])

years = list(map(getvalue, sheet['A'][1:]))
temperature = list(map(getvalue, sheet['C'][1:]))
activity = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(years, temperature, label='Данные')
pyplot.show()
