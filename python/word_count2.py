import sys
from janome.tokenizer import Tokenizer

filename = sys.argv[1]

fp = open(filename, 'rt',encoding='sjis')
text = fp.read()

tok = Tokenizer()
tokens = tok.tokenize(text)
counter = {}
for t in tokens:
    bf = t.base_form
    if bf not in counter:
        counter[bf] = 0
    counter[bf] += 1

sc = sorted(counter.items(), key = lambda x:x[1], reverse=True)

for i, t in enumerate(sc):
    if i >= 100:
        break
    key, cnt = t
    print((i + 1),'.',key, '=',cnt)