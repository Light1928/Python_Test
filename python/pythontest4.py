# ジャンケンゲーム（対戦記録あり)


import random


def validata(hand):
    if 0 <= hand <= 3:
        return True
    else:
        return False


def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は「' + hands[hand] + '」を出しました\n')


def judge(player, computer):
    if player == computer:
        return '引き分け'
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        return '勝ち'
    else:
        return '負け'


player_win = 0
computer_win = 0
draw = 0

print('じゃんけんをはじめます')

player_name = input('● 名前を入力してください\n'+'　※ゲストを使用する場合はそのままEnter\n'+':')

while True:

    print('--------------------------------------------------------------')
    print('● 何を出しますか？（0: ゲーム終了, 1: グー, 2: チョキ, 3: パー）')

    player_hand = int(input('● 数字で入力してください：'))

    print('')

    if 1 <= player_hand <= 3:
        if validata(player_hand):

            computer_hand = random.randint(0, 2)

            if player_name == '':
                print_hand(int(player_hand-1))
            else:
                print_hand(int(player_hand-1), player_name)

            print_hand(computer_hand, 'コンピューター')
            result = judge(int(player_hand), computer_hand)
            print('結果は 「' + result + '」　でした\n')

            if result == '勝ち':
                player_win += 1
            elif result == '負け':
                computer_win += 1
            else:
                draw += 1

            print(str(player_win) + '勝　' + str(computer_win) +
                  '負　' + str(draw) + '引き分け　です')

        else:
            print('● 正しい数値を再入力してください')

    else:
        print('ゲームを終了します')
        break
