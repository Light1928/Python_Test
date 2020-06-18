# import sys
# #コマンドライン引数なので実行のやり方が違う
# print(sys.argv)     #リストの中全てを出力
# print(sys.argv[0])  #実行されたファイル名が格納されている
# print(sys.argv[1])  #ここから引数が格納されていく
# print(sys.argv[2])
# print(sys.argv[3])

# total = 0
# while total <=300:
#     price =input('値を入力：')
#     total += int(price)
#     print('合計',total,'円')

# from random import randint as ri
# ans = ri(1,10)
# #input関数は文字列として受け取るためintでキャストしなければならない
# while int(input('１から１０までの値を入力：')) != ans :
#     print('不正解！再入力してください')
# print('正解')
#テキストファイルとpyファイルの場所が違う場合テキストファイルのパスを入力する必要がある
# with open('./python/hoge.txt','r',encoding='utf-8') as f:
#     count = 1
#     for line in f:
#         print('{0:03d} {1}'.format(count,line),end='')
#         count += 1


# import sys
# with open(sys.argv[1], 'r', encoding='utf-8') as file:
#     count = 1
#     for line in file:
#         print('{0:03d} {1}'.format(count,line),end='')
#         count += 1
#jsonを利用することで他の環境でも動く
import json
# menu = [
#     {'n':'ハン','p':100,'c':260},
#     {'n':'チー','p':130,'c':310},
#     {'n':'フラ','p':150,'c':420}
# ]


# with open('hoge.txt','w') as file:
#     json.dump(menu,file,indent = 4)

with open('hoge.txt','r') as file:
    hoge = json.load(file)
print(hoge)
print(hoge[0])
print(hoge[1])