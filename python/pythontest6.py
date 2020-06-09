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

# def test(*x,**y): #可変長引数のため引数は０以上の個数　(**y)キーワード引数の場合辞書、(*x)位置引数の場合タプル
#     print(x)
#     print(y)

# test(a=4,b=5) #キーワード引数の場合
# test(1,2,3) #　位置引数の場合タプルとして*xに渡される
# test(a=4,b=5,c=6) #キーワード引数の場合**yに渡される


# a=[]
# for x in range(1,10):
#     a.append(x**2)
#print(a)

#上３行を１行にまとめることができる（内包表記）
# a = [x**2 for x in range(1,10)]
# print(a)

#条件もつけることが可能
# a = [x**2 for x in range(1,10) if x % 3 == 0]
# print(a)

#Fizz Buzzゲーム　プログラマ入入社試験問題によく出る
# x = 2
# print('Fizz' if x % 3 == 0 else x)

# x = 3
# print('Fizz' if x % 3 == 0 else x) 

# a= ['Fizz' if x % 3 == 0 else x for x in range(1,10)]
# print(a)

#上のプログラムを崩した場合
# a = []
# for x in range(1,10):
#     if(x % 3 == 0):
#         a.append('Fazz')
#     else:
#         a.append(x)
# print(a)

#end=''で改行なしにできる
#ジェネレータ式
# number = (x for x in range(10))
# for x in number:
#     print(x)

# def do_return():
#     return 1
#     return 2
#     return 'Fizz'
#     return 4
#     return 'Buzz'

# print(do_return())
# print(do_return())
# print(do_return()) #1しか帰ってこない

# def do_yield():
#     yield 1
#     yield 2
#     yield 'Fizz'
#     yield 4
#     yield 'Buzz'

# print(do_yield())
# print(do_yield())
# print(do_yield())

#イテラブルのためfor文と組み合わせることが可能
#イテラブルとは繰り返しアクセエス可能なオブジェクトのこと リスト,タブル,rangeなど
# for i in do_yield():
#     print(i)

#FizzBuzzゲーム
#returnだと一度returnするとおわってしまう
# def fizzbuzz(n):
#     for x in range(1,n):
#         if x % 15 == 0:
#             yield 'FizzBuzz'
#         elif x % 5 == 0:
#             yield 'Buzz'
#         elif x % 3 == 0:
#             yield 'Fizz'
#         else:
#             yield x
# print(list(fizzbuzz(16)))

#hoge = (10,20,30)
# hoge = 10,20,30
# print(hoge)
# 
# hoge = 100,90,80
# for rank,hoge in enumerate(hoge,1):
#     print(str(rank)+'位' + str(hoge)+'点')

# hoge = {10,20,30}
# print(hoge)
# #少数も整数と同じになる
# hoge={10,20,30,20,10.0}
# print(hoge)

# moge = [1,2,3,1,2,3,1,2,3]
# print(set(moge))

#辞書
hoge = {101:'本寺',102:'高井'}
# print(hoge[101])

# #キーを取り出す場合
# for h in hoge:
#     print(h)

#辞書から全てのキーと値のペアを取り出す
for h1,h2 in hoge.items():
    print(str(h1)+'号室は'+h2+'さん')


hoge[103] = '森実'
print(hoge)

hoge[103] = '馬場'
print(hoge)

del hoge[103]
print(hoge)

hoge =[]
for x in range(1,10):
    if x % 3 != 0:
        hoge.append(x)
    else:
        hoge.append('F')
print(hoge)

#１行で表す
print([x for x in range(1,10) if x % 3 != 0])

print('F' if x % 3 == 0 else x for x in range(1,10))