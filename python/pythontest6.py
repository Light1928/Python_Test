# hoge = [10,20] #リスト
# print(hoge)
# print(hoge[0])

# moge = (10,20) #タプル
# print(moge)
# print(moge[0])


# hoge = 10,20,30 #パック、パッキング
# print(hoge)

# h1,h2,h3 = hoge #アンパック、アンパッキング
# print(h1)
# print(h2)
# print(h3)

# hoge = [(10,20),(30,40),(50,60)]
# print(hoge[0][0])

# hoge = 10
# moge = 20
# poge = 30
# print(hoge,moge,poge)

# hoge = [10,20,30]
# for h1,h2 in enumerate(hoge,1): #開始値と要素をそれぞれの変数に代入　デフォルトは０
#     print(h1,h2)

# def test(*x): #０以上の変数の個数　タプルになる
#     print(x)
# test(1,2)
# test()

# def sum(*number):
#     s = 0
#     for n in number:
#         s += n
#     print(s)

# sum(1,2)

# 集合
# hoge = {10,20,30,20,10} #重複は１つにまとめられる
# print(hoge)
# print(hoge[0]) #添字の概念がない

# hoge = [10,20,30,20,10]
# print(hoge)
# print(type(hoge)) #type　型が分かる

# moge = set(hoge) #set 集合に変わる
# print(moge) #また、集合(set)は重複を持たない
# print(type(moge))

# hoge = {10,20,30,20,10}
# print(hoge)

# print(30 in hoge) #trueが返る hogeに30が入っているか

# print(20 not in hoge)#falseが返る

# hoge = {10, 20, 30}
# hoge |= {40, 50}  # バラバラに挿入される
# print(hoge)

# hoge = {10, 20, 30}
# hoge -= {20}
# print(20)


# hoge = {10,20,30}
# moge = {10,30,50}
# print(hoge & moge)#積集合　互いにあるデータのみ抽出
# print(hoge | moge)#和集合　全て抽出
# print(hoge - moge)#差集合　左側のみのデータを抽出
# print(hoge ^ moge)#対象差　どちらか一方のみのデータを抽出

#1801の左側がキー　キーは重複不可　右側が値
# hoge = {1801:'本寺',1802:'高井'}
# moge = ['本寺','高井']
# # print(hoge)
# # print(type(hoge))

# # print(hoge[1801]) #辞書はキー
# # print(moge[0]) #リストはインデックス

# # for k1,k2 in hoge.items():
# #     print(k1,k2)

# hoge[1803] = '森実' #辞書に要素の追加
# print(hoge)

# hoge[1803] = '澤野井' #上書き
# print(hoge)
# del hoge[1803]
# print(hoge)

def test(*x,**y): #可変長引数のため引数は０以上の個数　(**y)キーワード引数の場合辞書、(*x)位置引数の場合タプル
    print(x)
    print(y)

test(a=4,b=5) #キーワード引数の場合
test(1,2,3) #　位置引数の場合タプルとして*xに渡される
test(a=4,b=5,c=6) #キーワード引数の場合**yに渡される
