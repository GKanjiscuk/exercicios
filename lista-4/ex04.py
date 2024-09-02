texto = 'The Python Software Foundation and the global Pythoncommunity welcome and encourage participation by everyone. Our community is based onmutual respect, tolerance, and encouragement, and we are working to help each other live upto these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'.lower()
texto = texto.replace(',', ' ')
texto = texto.replace('.', ' ')
texto = texto.replace(':', ' ')

resposta= []
for i in texto.split():
    if i[0] in 'python' or i[-1] in 'python':
        resposta.append(i)

print(resposta)