import tkinter                          #GUI作成用
from tkinter import messagebox          #メッセージボックス用
import smtplib                          #メール送信用
from email.mime.text import MIMEText    
from email.utils import formatdate


#########送信ボタンが押されたら呼び出される関数###########
def gmail():
    FROM_ADDRESS = '自分のアカウントのメールアドレス'
    MY_PASSWORD = '自分のアカウントのパスワード'
    TO_ADDRESS = txt1.get()
    BCC = ''
    SUBJECT = txt2.get()
    BODY = txt3.get()


    def create_message(from_addr, to_addr, bcc_addrs, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Bcc'] = bcc_addrs
        msg['Date'] = formatdate()
        return msg

    def send(from_addr, to_addrs, msg):
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
        smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
        smtpobj.close()

    to_addr = TO_ADDRESS   
    subject = SUBJECT
    body = BODY

    try:
        msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
        send(FROM_ADDRESS, to_addr, msg)
        messagebox.showinfo('成功','送信しました',)
    except:
        messagebox.showinfo('失敗','送信できませんでした')
########################################################


root = tkinter.Tk()
root.geometry('400x200')
root.title('G-mail 自作アプリ')

lbl1 = tkinter.Label(text='T O')
lbl1.place(x=30,y=30)

txt1 = tkinter.Entry(width=30)
txt1.place(x=90,y=30)

lbl2 = tkinter.Label(text='件名')
lbl2.place(x=30,y=60)

txt2 = tkinter.Entry(width=30)
txt2.place(x=90,y=60)
        
lbl3 = tkinter.Label(text='本文')
lbl3.place(x=30,y=90)

txt3 = tkinter.Entry(width=30)
txt3.place(x=90,y=90)

btn = tkinter.Button(text='送　信', command=gmail) #送信ボタン
btn.place(x=170,y=140)

root.mainloop()