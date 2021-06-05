#!/usr/bin/env python
# coding: utf-8
# この二つは必ず冒頭！
# =======================================================================
# ■POST送信されたものを受け取る処理
import cgi
import cgitb

cgitb.enable()

# HTMLを記述するためのヘッダ
print("Content-Type: text/html")
print()

# インスタンス化、フォームデータを取得する
form = cgi.FieldStorage()
first_num = form.getvalue("first_num")
last_num = form.getvalue("last_num")

print("Success! Open the data.csv file in folder")
print("</br>")
print("<a href='/'><button type='submit'>Back</button></a>")

# =======================================================================
# ■取得した変数の型変換（念のため）

first_num=int(first_num)
last_num=int(last_num)


# =======================================================================
# ■実装

import csv
from bs4 import BeautifulSoup
import urllib.request as req 
# ■関数の定義

def single_get(i):
    # HTMLを解析する --- (※3)
    url = "https://poke-m.com/producers?category=%E9%87%8E%E8%8F%9C&page_no=" + str(i)
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    # =======================================================================
    # 住所を取得する

    lists=soup.find_all(class_="address")
    Address_lists =[]
    for a in lists:
        lists = Address_lists.append(a.get_text().replace("\u3000", "").replace("\'", ""))

    # =======================================================================
    # 名前を取得する
    lists=soup.find_all(class_="name")

    Name_lists =[]
    for a in lists:
        lists = Name_lists.append(a.get_text().replace("\u3000", "").replace("\'", ""))

    # =======================================================================
    # 詳細を取得する
    lists=soup.find_all(class_="types")

    Detail_lists =[]
    for a in lists:
        lists = Detail_lists.append(a.get_text().replace("\u3000", "").replace("\'", ""))

    # =======================================================================
    # 全ての配列を結合する
    data=list(zip(Address_lists,Name_lists,Detail_lists))

    return data
# =======================================================================
# ■関数の実行と保存
all_data=[]
for i in range(first_num,last_num+1): 
    s = single_get(i)
    all_data.extend(s)

# エクセルへ出力する関数
with open('data.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(all_data)

# =======================================================================
# ■おまけの部品
# import sys
# if "first_num" not in form:
#     print("Error! Back & Type Number")
#     print("<a href='/'><button type='submit'>Back</button></a>")
#     sys.exit()
# =======================================================================
# ■ローカルでの使い方

# ※権限を755にする
#     chmod 755 cgi-bin/double.py

# ※pythonのCGIモジュールを使ってサーバーを立ち上げる
#     python -m http.server --cgi 8000

# ※ローカルホストを立ち上げる
# http://localhost:8000/

# ※取得したいURLを検索窓にいれる 

# 以上
# =======================================================================



