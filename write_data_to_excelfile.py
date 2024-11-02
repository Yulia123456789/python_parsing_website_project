import xlsxwriter

from parsing_website1 import array

def writer(parametr):

    workbook = xlsxwriter.Workbook("/home/yu/Рабочий стол/data_python_project/data.xlsx")
    sheet = workbook.add_worksheet('данные_о_товарах')

    sheet.set_column('A:A', 20)
    sheet.set_column('B:B', 20)
    sheet.set_column('C:C', 50)
    sheet.set_column('D:D', 50)

    row = 0
    column = 0
    for item in parametr:
        sheet.write(row, column, item[0])
        sheet.write(row, column + 1, item[1])
        sheet.write(row, column + 2, item[2])
        sheet.write(row, column + 3, item[3])
        row += 1


    workbook.close()

writer(array())

