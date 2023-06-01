# 引入 sqlite3 模組
import sqlite3

# 建立資料庫連接，如果資料庫不存在則會被創建
conn = sqlite3.connect('example.db')

# 建立游標物件
c = conn.cursor()

# 定義一個資料列表
data = [
    ('2023-05-31', 'BUY', 'AI', 100, 35.2),
    ('2023-05-31', 'BUY', 'TSLA', 50, 700),
    ('2023-05-31', 'SELL', 'AAPL', 150, 130),
    ('2023-05-31', 'BUY', 'MSFT', 200, 200)
]

# 使用游標物件執行 SQL 語句，插入多筆資料
c.executemany("INSERT INTO stocks VALUES (?, ?, ?, ?, ?)", data)

# 要記得提交事務，不然插入的資料不會被實際寫入資料庫
conn.commit()

# 顯示變更總數
print(conn.total_changes) 

# 使用游標物件執行 SQL 語句，查詢資料
c.execute("SELECT * FROM stocks WHERE symbol = 'AI'")

# 使用 fetchall 函數取得查詢結果
print(c.fetchall())

# 在完成所有資料庫操作後，關閉連接
conn.close()


