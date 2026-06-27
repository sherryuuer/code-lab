import gspread
import re

gc = gspread.service_account('service_account_credentials.json')
spreadsheet = gc.open_by_key('1bqccoz6XTmQGKMfwvHggPzmnyT9Hi2Emwjx2yFqDLKs')

# loop and add worksheets
products = ['UltraZoom Camera', 'HydroClean Vacuum', 'TasteBud Blender', 'VeloSwift Bicycle', 'SonicBeat Headphones',
            'MobiMax Smartphone', 'LumaBright Lamp', 'HomeEase Air Conditioner', 'MegaFit Treadmill', 'AquaPure Water Filter']

for product in products:
    spreadsheet.add_worksheet(title=product, rows=100, cols=100)


# loop and delete worksheets
pattern = r'^Sheet\d+$'
all_ws = spreadsheet.worksheets()

for ws in all_ws:
    if re.search(pattern, ws.title) is not None:
        spreadsheet.del_worksheet(ws)
