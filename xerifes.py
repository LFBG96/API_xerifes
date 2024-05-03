import pandas as pd



def jsonXerifes():
    xerifes = pd.read_excel('/home/apenas/mysite/xerifes.xlsx')
    xerifes['Data'] = xerifes['Data'].dt.strftime('%d/%m/%Y')
    return xerifes.to_json(orient='records' ,date_format='iso')


