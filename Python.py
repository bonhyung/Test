#!python

import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials

#def main(string) :
#    print(string)
#if __name__ == "__main__" :
#    main(sys.argv[1])

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

json_file_name = 'roktest-e1292599e71d.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1cp7Dog-xParbQKDKpok4JEuREbFyaBDZW8aWjloJQlk/edit#gid=0'
# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)

sheet = doc._spreadsheets_get

# 시트 선택하기
wk = doc.worksheet('시트1')

# 특정 cell 가져오가
cell_data = wk.acell('B2').value
print('cell data: ' ,cell_data)

# 행 데이터 가져오기
row_data = wk.row_values(2)
print('rowdata : ', row_data, len(row_data))

# 열 데이터 가져오기
col_data = wk.col_values(2)
print('coldata : ',col_data, len(col_data))

#특정 cell 데이터 쓰기
wk.update_acell('C3','test')
wk.update_acell('D3','bhku')
#행으로 데이터 쓰기
#wk.append_row(['11','22','333','4444'])

# 특정위치에 한행을 추가
#wk.insert_row(['11','22','333','4444'],4)

# 시트 크기 조정
wk.resize(15,10)

wk.format("A2:B2", {
    "backgroundColor": {
      "red": 0.0,
      "green": 0.0,
      "blue": 0.0
    },
    "horizontalAlignment": "CENTER",
    "textFormat": {
      "foregroundColor": {
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      "fontSize": 12,
      "bold": True
    }
})

print('hello world')

