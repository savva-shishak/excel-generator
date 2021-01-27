from openpyxl import load_workbook
from openpyxl.cell.cell import MergedCell
from model import MCell

wb = load_workbook(filename = 'sample.xlsx')
sheet_ranges = wb['Шаблон']

cell = MCell()
print(cell)
