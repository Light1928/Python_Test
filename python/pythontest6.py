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
