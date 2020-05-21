# hoge = [10,20,30]
# for h in hoge:
#     print(h)

# hoge = [10,20,30]
# for h in range(1,3):
#     print(hoge[h])

# age = 64
# if age < 20:
#     print('未成年')
# elif 19 < age < 65:
#     print('現役世代')
# else:
#     print('高齢')

#文字列検索する場合＝＝は使わずにinを使う true falseが返ってくる
# name = '情報花子'
# if '子' in name:
#     print('有')
# else:
#     print('無')

# moji = 'P'
#inを使わなくてもmoji < 'pppp'とかでも動く
# while moji in 'PPPP':  
#     moji = 'P' + moji
# print(moji)

#別解
# moji = 'P'
# while moji in 'PPPPP':
#     moji = 'P' + moji
# print(moji)


#str(変数)　数値を文字列に変換
# temp = 35.5
# while temp <= 38.0:
#     print(str(temp) + 'は平熱です')
#     temp += 0.5
#     if temp == 37.0:
#         break
# このprintはwhileを抜けた後
# print(str(temp) + 'は微熱です')

# hoge = ['12','1234','123']
# for h in hoge:
#     if len(h) >= 4:
#         continue
# 実行されないため必要なし(print(h))
#     while len(h) < 4:
#         h = '0' + h #文字列は左からつめる　数値は右からつめる
#     print(h)

# hoge = ['12','1234','123']
# for h in hoge:
#     if len(h) >= 4:
#         break
#     while len(h) < 4:
#         h = '0' + h
#     print(h)
# else: for文でのelseは、for文が正常処理できた場合のみ処理される
#     print('OK')