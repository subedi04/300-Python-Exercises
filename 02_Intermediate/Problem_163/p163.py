'''
Write a Python Program to Create a excel 
file using python using xlswriter library 
'''
import xlsxwriter

wb = xlsxwriter.Workbook("xlswriter_wb.xlsx")
wb_sheet = wb.add_worksheet()
wb_sheet.write('A1',"Faisal Zamir")
wb_sheet.write('B1',"Python")

wb.close()