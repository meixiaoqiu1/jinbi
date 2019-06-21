import xlrd
class ReadExcelData(object):
    def returnExcelData(self,ExcelName,sheetNme,x,y):
        ExcelName=xlrd.open_workbook('../data_pool/data.xlsx')
        Excelsheet=ExcelName.sheet_by_name(sheetNme)
        TestData=Excelsheet.cell(x,y).value
        return TestData
