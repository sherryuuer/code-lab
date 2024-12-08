import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open('gspread 101')

# rename a new sheet
ws = spreadsheet.worksheet('Sheet2')
ws.update_title('Second Sheet')

# add a sheet
spreadsheet.add_worksheet(title='a new worksheet', rows=100, cols=100)

# delete a sheet
ws = spreadsheet.worksheet('Second Sheet')
spreadsheet.del_worksheet(ws)
