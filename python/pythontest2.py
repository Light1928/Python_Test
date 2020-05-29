# hoge = [1,2,3,2,1]
#index(要素)要素のあるindex番号を返す
# print(hoge.index(3))

# def trip(d,s):
#     """ dとsからtを求める.
#         関数の処理の詳細を記述する
#         〜〜〜〜〜〜
#         記述する際は以下のことを守る
#         　三重のダブルクォートをつかう
#         　１行目に概要説明を書く　末尾にはピリオドをつける
#         　２行目は空行にする
#         　３行目以降に詳細説明を書く
#     """
#     t = d / s
#     return t
# #trip関数を呼び出す
# print(trip(10,2))

#メソッドを定義する前にメソッドを呼び出すとエラー　（プログラムは上から読まれるため）
# print(trip(10,2))

# def trip(d,s):
#     t = d / s
#     return t

#関数の説明を読むことができる
# コメント("""~~""")が表示される
# help(trip)
#__doc__を使うとコメント部分のみ表示できる
# help(trip.__doc__)

# def hoge(a=1,b=2,c=3):
#     print(a)
#     print(b)
#     print(c)

# hoge(c=999)

# print(list(map(lambda x:x*x,[1,2,3])))

# def cat():
#     global pet
#     pet = 'cat'
   
# pet = 'dog'
# cat()
# print(pet)

#小テスト

# def bmi(hei,wei):
#     return wei/hei/hei*10000

# print(bmi(wei=70,hei=175)) #キーワード引数


# def hoge(x=1,y=2,z=3):
#     print('x = ' + str(x))
#     print('y = ' + str(y))
#     print('z = ' + str(z))

# hoge(10,z=10)

# hoge = list(range(3,6))
# print(hoge)


# hoge = list(map(lambda x: 9*x, range(1,10)))
# print(hoge)

# def hoge():
#     global a
#     a = 'さようなら'
#     print(a)
# a = 'おはよう' #グローバル変数
# hoge()

def hoge():
    def moge():
       # nonlocal a  #nonlocalを使うと外側（hoge)のローカル変数に代入することができる
        global a     #関数の外に定義しているグローバル変数を使用
        a = '111'   #moge内のローカル変数
        print(a)

    a = '222'       # hoge内のローカル変数
    moge()
    print(a)

a = '333' #グローバル変数
hoge()
print(a)