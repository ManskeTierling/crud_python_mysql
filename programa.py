from funcao import add, delete, read

while True:
    print('======== BANCO DE DADOS ========')
    nome = str(input('Nome: '))
    sobrenome = str(input('Sobrenome: '))
    cpf = input('CPF: ')
    email = input('E-mail: ')
    telefone = int(input('Telefone: '))
    print('''======== OPÇÕES ========
1. Adicionar
2. Deletar
3. Ler''')
    opcao = int(input('Opção: '))

    if opcao == 1:
        add(nome, sobrenome, cpf, email, telefone)
    elif opcao == 2:
        delete(cpf)
    elif opcao == 3:
        read(cpf)
    



