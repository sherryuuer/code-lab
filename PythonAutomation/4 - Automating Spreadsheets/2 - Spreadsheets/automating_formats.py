import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open('Formulas, Fonts, and Fills')

ws = spreadsheet.worksheet('Ratings')

rng = ws.range('B2:E11')

bad_rating_style = {
    "textFormat": {
        "foregroundColor": {
            "red": 1.0,
            "green": 0.0,
            "blue": 0.0
        },
        "fontSize": 12,
        "italic": True
    }
}

good_rating_style = {
    "textFormat": {
        "foregroundColor": {
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
        },
        "fontSize": 12,
        "bold": True
    },
    "backgroundColor": {
        "red": 0.0,
        "green": 0.0,
        "blue": 1.0
    }
}

for cell in rng:
    addr = cell.address

    if cell.value == '':
        pass
    elif int(cell.value) < 5:
        ws.format(addr, bad_rating_style)
    elif int(cell.value) == 10:
        ws.format(addr, good_rating_style)