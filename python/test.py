def hoge():
    def moge():
        a = '111'
        print(a)

    a = '222'
    moge()
    print(a)

a = '333'
hoge()
print(a)