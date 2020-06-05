import mysql.connector as mydb

  # コネクションの作成
conn = mydb.connect(
      host='localhost',
      port='3306',
      user='root',
      password='password',
      database='python_test'
)

  # コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

  # 接続できているかどうか確認
print(conn.is_connected())

#DB操作用のカーソル作成
cur = conn.cursor()
cur.execute("SELECT * FROM user")
rows = cur.fetchall()
for row in rows:
    print(row)
# DB操作が終わったらカーソルとコネクションを閉じる
cur.close()
conn.close()