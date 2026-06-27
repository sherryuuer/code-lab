import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open('Employee Ratings')

ws = spreadsheet.worksheet('Ratings')

rng = 'B2:E11'

data = ws.get(rng)  # 取得的结果是一个二元嵌套列表

for i, row in enumerate(data):
    for j, val in enumerate(row):
        if not val.isnumeric():
            data[i][j] = ''
        elif int(val) < 0:
            data[i][j] = 0
        elif int(val) > 10:
            data[i][j] = 10
        else:
            data[i][j] = int(val)

ws.update(data, rng)
