import pdfplumber
import xlsxwriter
import os
import pathlib

# get filelist
files = os.listdir(pathlib.Path("pdftotext/source"))
# files = os.listdir(f'{os.getcwd()}\\source')

for file in files:
    pdf = pdfplumber.open(pathlib.Path(f'pdftotext/source/{file}'))
    # pdf = pdfplumber.open(f'{os.getcwd()}\\source\\{file}')

    p0 = pdf.pages[0]

    table = p0.extract_tables()

    natOfOperation = table[1][2][0].split('\n')[1]
    corporateName = table[2][0][0].split('\n')[1]
    dateOfIssuance = table[2][0][6].split('\n')[1]
    fatura = p0.crop([15, 254, 575, 360]).extract_text()
    nfValue = table[3][1][9].split('\n')[1]

    codes = []
    qty = []
    vlUnit = []
    aiIpi = []
    for page in pdf.pages:
        codes.extend(page.extract_table()[1][0].split('\n'))
        qty.extend(page.extract_table()[1][6].split('\n'))
        vlUnit.extend(page.extract_table()[1][7].split('\n'))
        aiIpi.extend(page.extract_table()[1][13].split('\n'))

    wb = xlsxwriter.Workbook(pathlib.Path(f'pdftotext/{file}.xlsx'))
    # wb = xlsxwriter.Workbook(f'{os.getcwd()}\\{file}.xlsx')
    sheet1 = wb.add_worksheet()

    #NATUREZA DA OPERAÇÃO
    sheet1.write("A1", "NATUREZA DA OPERAÇÃO")
    sheet1.write("B1", natOfOperation)

    #NOME/RAZÃO SOCIAL
    sheet1.write("A2", "NOME/RAZÃO SOCIAL")
    sheet1.write("B2", corporateName)

    #DATA DA EMISSÃO
    sheet1.write("A3", "DATA DA EMISSÃO")
    sheet1.write("B3", dateOfIssuance)

    #FATURA
    sheet1.write("A4", "FATURA")
    sheet1.write("B4", fatura)

    #VALOR TOTAL DA NF
    sheet1.write("A5", "VALOR TOTAL DA NF")
    sheet1.write("B5", nfValue)

    sheet1.write("A7", "CÓD. PROD.")
    sheet1.write("B7", "QTDE.")
    sheet1.write("C7", "VL. UNIT.")
    sheet1.write("D7", "Al. IPI")

    x = 8
    y = 0
    for code in codes:
        idx = str(x)
        sheet1.write("A"+idx, code)
        sheet1.write("B"+idx, qty[y])
        sheet1.write("C"+idx, vlUnit[y])
        sheet1.write("D"+idx, aiIpi[y])
        x += 1
        y += 1

    wb.close()

print('end')