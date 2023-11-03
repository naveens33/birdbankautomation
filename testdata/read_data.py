import xlrd


def get_data():
    wb = xlrd.open_workbook(r"C:\Users\Me\PycharmProjects\birdbankautomation\testdata\TestData.xls")
    sheet = wb.sheet_by_name("NewBiller")
    print(sheet.nrows)
    print(sheet.ncols)
    data = []
    for i in range(1, sheet.nrows):
        data.append([sheet.cell_value(i, 0), sheet.cell_value(i, 1)])
    return data
