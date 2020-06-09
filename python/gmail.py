import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS =  '自分のアカウントのメールアドレス'
MY_PASSWORD = '自分のアカウントのパスワード'
TO_ADDRESS = '相手のメールアドレス'
BCC = ''
SUBJECT = '件名'
BODY = '本文'

def create_message(from_addr,to_addr,bcc_addrs,subject,body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg

def send(from_addr,to_addrs,msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com',587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS,MY_PASSWORD)
    smtpobj.sendmail(from_addr,to_addrs,msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = create_message(FROM_ADDRESS,to_addr,BCC,subject,body)
    send(FROM_ADDRESS,to_addr,msg)