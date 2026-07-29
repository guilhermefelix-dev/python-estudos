livros_emprestados = 0

print("=== BEM-VINDO A BIBLIOTECA GALÁCTICA!=== ")
print("escolha uma opção: 1 - Emprestar livro, 2 - Devolver livro, 3 - livros emprestados, 4 - Sair")
opcao = int(input("Digite a opção desejada: "))

while opcao != 4: 
    if opcao == 1:
        if livros_emprestados < 3:
            livros_emprestados += 1
            print("Livro emprestado com sucesso!")
        else:
            print("Limite de livros emprestados atingido. Por favor, devolva um livro antes de emprestar outro.")
            
    elif opcao == 2:
        if livros_emprestados > 0:
            livros_emprestados -= 1
            print("Livro devolvido com sucesso!")
        else:
            print("Você não possui nenhum livro para devolver! ")
    elif opcao == 3:
        print(f"Total de livros emprestados: {livros_emprestados}")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    print("escolha uma opção: 1 - Emprestar livro, 2 - Devolver livro, 3 - livros emprestados, 4 - Sair")
    opcao = int(input("Digite a opção desejada: "))

print("OBRIGADO POR USAR A BIBLIOTECA GALÁCTICA! ")