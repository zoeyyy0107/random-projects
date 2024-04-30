import pandas as pd
import os

def readFileAsDataframe(fileType, filename):
    data = []

    if fileType == 'csv':
        data = pd.read_csv(f'!sec financial data\source\{filename}', index_col=False)
    elif fileType == 'excel':
        data = pd.read_excel(f'!sec financial data\source\{filename}', index_col=False)
    
    return data

files = os.listdir('!sec financial data/source/')

for file in files:
    fname = file
    df = readFileAsDataframe('excel', fname)

    # remove null columns
    df.dropna(how='all', axis=1, inplace=True)

    # replace footnotes
    for i in range(1,50):
        df.columns = df.columns.str.replace(f'\({i}\)', '', regex=True)
        df.replace(f'\({i}\)', '', inplace=True, regex=True)

    # trim columns
    df.columns = df.columns.str.strip()

    # clean these columns
    replaceList = ['$', '€', '£', 'C$', 'CAD', 'DKK', 'EUR', 'GBP', 'NOK', 'SEK', 'AUD']
    for str in replaceList:
        #df['Par / Units'].replace(str, '', inplace=True)
        df['Amortized Cost'].replace(str, '', inplace=True)
        df['Fair Value'].replace(str, '', inplace=True)

    df.to_excel(f"!sec financial data\\{fname.replace(' ', '_')}", index=False)