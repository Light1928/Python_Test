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

# name = '情報花子'
# if name == '子':
#     print('有')
# else:
#     print('無')

# moji = 'P'
# while moji <= 'PPPP':
#     moji = 'P' + moji
# print(moji)

#別解
# moji = 'P'
# while moji < 'PPPPP':
#     moji = 'P' + moji
# print(moji)

# temp = 35.5
# while temp <= 38.0:
#     print('平熱です')
#     temp += 0.5
#     if temp == 37.0:
#         break
# print('微熱です')

# hoge = ['12','1234','123']
# for h in hoge:
#     if len(h) >= 4:
#         continue
#         print(h)
#     while len(h) < 4:
#         h = '0' + h #左からつめる
#     print(h)
