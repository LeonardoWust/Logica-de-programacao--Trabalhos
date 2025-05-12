estoque = 100
vendas = 0
reposicao = 0

def vender():
    global estoque, vendas
    while True:
        menu = (input('Digite "vender" para vender, ou "sair" para sair'))

        if menu == 'sair':
            break
        elif menu == 'vender':
            if estoque >0:
                estoque -=1
                vendas +=1
                print("produto vendido")
            else:
                print("Estoque zerado, não dá para vender")
        else:
            print("Opção inválida, digite vender ou sair")

def repor():
    global estoque, reposicao
    while True:
        menu = (input('Digite "repor" para repor, ou "sair" para sair'))

        if menu == 'sair':
            break
        elif menu == 'repor': 
            estoque +=1
            reposicao +=1
            print("Produto reposto")
        else:
            print("Opção inválida, digite repor ou sair")

def mostrar_estoque():
    print("Estoque: ", estoque)
    print("Vendas Realizadas: ", vendas)
    print("Reposições: ", reposicao)

while True:
    print("Menu Principal:")
    print("1 - Vender")
    print("2 - Repor")
    print("3 - Estoque")
    print("4 - Encerrar")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        vender()
    elif escolha == 2:
        repor()
    elif escolha == 3:
        mostrar_estoque()
    elif escolha == 4:
        print("Encerrando sistema")
        break
    else:
        print("Opção inválida.")
