import tkinter as tk

from tkinter import font

"""
button1は'１'、button2は'２'、button3は'＋'、button4は'ー'
printはデバッグ用
config関数で属性を変更
文字を連結させて=が押されたらeval関数を使用して式と評価する

"""

def btn_click(moji):
    global total
    if moji == '1':
        button1.config(state='disable')
        button2.config(state='disable')
        button3.config(state='normal')
        button4.config(state='normal')
        label.config(text=moji)
        total += moji
        print(total)
    elif moji == '2':
        button1.config(state="disable")
        button2.config(state='disable')
        button3.config(state='normal')
        button4.config(state='normal')
        label.config(text=moji)
        total += str(moji)
        print(total)
    elif moji == '+': #strとintを同時に条件に入れることはできない
        button1.config(state="normal")
        button2.config(state="normal")
        button3.config(state="disable")
        button4.config(state='disable')
        total += str(moji) 
        label.config(text=eval(total+'0'))
        print(total) 
    elif moji == '-':
        button1.config(state="normal")
        button2.config(state="normal")
        button3.config(state="disable")
        button4.config(state='disable')
        total += str(moji)
        print(total)        
    elif moji == '=':
        label.config(text=eval(total))
        button1.config(state="normal")
        button2.config(state="normal")
        button3.config(state='normal')
        button4.config(state='normal')
        total = ''
        print(type(total))
        print(total)
    else:
        total = ''
        label.config(text='')


global total
total = ''

base = tk.Tk()
base.title('電 卓')
base.geometry('300x350')

base.configure(bg='lightgray')
global label 
font1 = font.Font(family='Helvetica', size=20, weight='bold')
label = tk.Label(base,height=1,width=15,font=font1, anchor="center")
label.place(x=60,y=20)

button1 = tk.Button(base,text='１',width=8,height=3,command=lambda:btn_click('1'),font='Helvetica')
button1.place(x=70,y=80)
button2 = tk.Button(base,text='２',width=8,height=3,command=lambda:btn_click('2'),font='Helvetica')
button2.place(x=70,y=170)
button3 = tk.Button(base,text='＋',width=8,height=3,command=lambda:btn_click('+'),font='Helvetica')
button3.place(x=170,y=80)
button4 = tk.Button(base,text='－',width=8,height=3,command=lambda:btn_click('-'),font='Helvetica')
button4.place(x=170,y=170)
button5 = tk.Button(base,text='＝',width=8,height=3,command=lambda:btn_click('='),font='Helvetica')
button5.place(x=120,y=235)
button6 = tk.Button(base,text='リセット',width=15,height=2,command=lambda:btn_click('リセット'),font='Helvetica')
button6.place(x=92,y=300)
base.mainloop()