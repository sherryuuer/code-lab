import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open('Formulas, Fonts, and Fills')

ws = spreadsheet.worksheet('Ratings')

rng = 'B2:E11'

data = ws.get(rng)

# modify data part
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

formulas = [['Average Rating']]

# modify formula part
for i in range(len(data)):
    current_row = str(i + 2)

    formula_cell = 'F' + current_row

    formula = '=AVERAGE(B' + current_row + ':E' + current_row + ')'

    formulas.append([formula])

formula_range = 'F1:F' + str(len(formulas))

ws.update(formulas, formula_range, raw=False)
