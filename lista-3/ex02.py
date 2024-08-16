user = input('Digite um usuário: ')
senha = input('Crie uma senha: ')

while (senha == user):
    print('ERRO: A senha não pode ser igual ao nome de usuário.')
    user = input('Digite um usuário: ')
    senha = input('Crie sua senha: ')

print('Você foi registrado com sucesso!')