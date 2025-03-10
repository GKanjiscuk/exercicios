import string

texto = '''“The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()

resposta = []
for c in string.punctuation:
    texto = texto.replace(c,' ')

def isin(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False

for p in texto.split():
    if isin(p) and len(p) > 4:
        resposta.append(p)

print(resposta)
print(len(resposta))