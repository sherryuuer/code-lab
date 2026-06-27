import gspread

# 需要从 GCP 取得 google drive 的 API，enable google drive 和 google spread 的 API
# 创建 client object
gc = gspread.service_account('service_account_credentials.json')

# open and edit
spreadsheet = gc.open('gspread 101')
ws = spreadsheet.sheet1

# 用 ss 的 key 打开，ss 名可以变化，但是 key 不会变
# spreadsheet = gc.open_by_key('1bqccoz6XTmQGKMfwvHggPzmnyT9Hi2Emwjx2yFqDLKs')


# ws.update('A1', 'Hello Google Sheets!')  (update 弃用了)
ws.update_acell('A1', 'Hello Google Sheets!')
ws.update([["Hello", "world"]], "A1:B1")  # 注意两个参数的位置和单一更新不一样，（更新内容，更新位置）

# create and share to person account
new_spreadsheet = gc.create('gspread 201')
new_spreadsheet.share('tlcuzick@gmail.com', perm_type='user', role='writer')
