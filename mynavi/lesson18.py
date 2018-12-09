from janome.tokenizer import Tokenizer

with open("kokoro.txt", "rt", encoding="shift_jis") as f:
    text = f.read()

tok = Tokenizer()
tokens = tok.tokenize(text)

counter = {}
for t in tokens:
    bf = t.base_form
    if not bf in counter: counter[bf] = 0
    counter[bf] += 1

sc = sorted(counter.items(), key=lambda x: x[1], reverse=True)

for i, t in enumerate(sc):
    if i >= 100: breakk
    key, cnt = t
    print((i + 1), "." , key, "=", cnt)
