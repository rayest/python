import re
import xlwt


def readDataToXls(path):
    data_table = xlwt.Workbook(encoding='utf-8', style_compression=0)
    new_sheet = data_table.add_sheet('student', cell_overwrite_ok=True)
    num = 0
    with open(path, 'r') as f:
        text = f.read()
        info = re.compile(r'"(\d+)":\["(.*?)",(\d+),(\d+),(\d+)]')
        for x in info.findall(text):
            for i in range(len(x)):
                new_sheet.write(num, i, x[i])
            num += 1
        data_table.save('result.xls')
    pass


if __name__ == '__main__':
    readDataToXls('student.txt')
