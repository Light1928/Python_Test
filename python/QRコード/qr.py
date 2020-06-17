import qrcode


#URLをQRコードにして生成
encode_text = 'https://google.com'
img = qrcode.make(encode_text)
img.show()