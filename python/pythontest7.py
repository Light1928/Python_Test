class MenuItem:     #MenuItemクラスを定義

 #クラスの中でメソッド（関数）を定義　※(第１引数にはSelfを追加する)
    #__init__メソッドはクラスの中でインスタンスが生成された直後にinitメソッドが呼び出され、その中の処理が実行される
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)  #printをreturnにすることで戻り値を返す
    
    #合計金額を求めるメソッド
    def get_total_price(self, count):
        total_price = self.price * count
        #注文が３つ以上の時は10%割引、
        if count >= 3:
            total_price*=0.9
        return round(total_price)

class Food(MenuItem):
    def __init__(self, name, price, calorie):
        super().__init__(name, price)
        self.calorie = calorie
    
    def info(self):
        return self.name + ': ¥' + str(self.price)

class Drink(MenuItem):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    def info(self):
        return self.name + ': ¥' + str(self.price)



#MenuItemクラスのインスタンスを生成
food1 = Food('サンドイッチ', 500, 330)
food2 = Food('チョコケーキ', 400, 450)
food3 = Food('シュークリーム', 200, 180)

foods = [food1, food2, food3]

drink1 = Drink('コーヒー', 300, 180)
drink2 = Drink('オレンジジュース', 200, 350)
drink3 = Drink('エスプレッソ', 300, 30)

drinks = [drink1, drink2, drink3]

print('-----------------------------'+'\n食べ物メニュー')
for index,food in enumerate(foods):     #enumerateあり
    print(str(index) +'.'+food.info())
    

print('飲み物メニュー')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('-----------------------------')

while True:
    try: #try文は例外処理を行う
        #購入する商品の番号を0~2で入力
        food_order = int(input('食べ物の番号を入力してください: '))
        if food_order <=2: #0~2の場合
            selected_food = foods[food_order]
            print('選択された食べ物: ' + selected_food.name)
            break

        else:   #0~3以外の数字の場合
            selected_food = food_order
            print('\n※ 0~2の食べ物の番号を入力してください ※　\n'+'-----------------------------')
            
    except: #try文の例外処理のexcept
        print('\n※ 0~2の食べ物の番号を入力してください ※　\n'+'-----------------------------')  

while True:
    try:
        drink_order = int(input('飲み物の番号を入力してください: '))
        if drink_order <=2: #0~2の場合
            selected_drink = drinks[drink_order]
            print('選択された飲み物: ' + selected_drink.name)
            break

        else:   #0~3以外の数字の場合
            selected_drink = drink_order
            print('\n※ 0~2の飲み物の番号を入力してください ※　\n'+'-----------------------------')

    except: #try文の例外処理のexcept
        print('\n※ 0~2の飲み物の番号を入力してください ※　\n'+'-----------------------------')  
    
    # 購入個数を入力し、お会計の内訳を表示
count =int(input('\n何セット買いますか？(3つ以上で1割引): '))
if 3 > count:
    print('お会計＝(' + selected_food.info() +' + '+ selected_drink.info() + ')×' +str(count))
        

else:
    print('お会計＝{(' + selected_food.info() +' + '+ selected_drink.info() + ')×' +str(count) + '} × 0.9')

    #結果を出力
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)
print('-----------------------------')
print('       お会計は'+str(result)+'円です\n'+'-----------------------------\n')