#-*-coding=utf-8 -*-
import xlrd,xlwt
from xlutils.copy import copy
from xlwt import Style
def rwExcel():
     global table
     data = xlrd.open_workbook('D:\\Documents\\Downloads\\test.xls')
     table = data.sheets()[0]
     # cell00 = table.cell(0,0).value
     # cell01 = table.cell(0,1).value
     cell10 = table.cell(1,0).value
     # cell11 = table.cell(1,1).value
     zhu = str(cell10)
     return zhu
def writeExcel(row,col,str,styl=Style.default_style):
    rb = xlrd.open_workbook('D:\\jietu\\member_tmpl.xls',formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    ws.write(row,col,str,styl)
    wb.save('D:\\jietu\\member_tmpl.xls')
# test = str(rwExcel())
# print test
# assert('TEST1110'==test)

# a = rwExcel()
# print(a)
style = xlwt.easyxf('align:  horiz center')
writeExcel(1, 6,'20199+',style)