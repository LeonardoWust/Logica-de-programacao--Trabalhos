def contar_pares(inicio, fim):
        contador = 0
        for numeros in range(inicio, fim + 1):
            if numeros % 2 == 0:
                contador +=1
        print(f"Quantidade de números pares entre {inicio} e {fim}: {contador}")

def mostrar_tabuada(numero):
     print(f"Tabuada do numero {numero}")
     for i in range(1, 11):
          print(f"{numero} x {i} = {numero * i}")

def contar_positvos(inicio, fim):
    contador = 0
    for numero in range(inicio, fim + 1):
         if numero > 0:
              contador +=1
    print(f"Quantidade de numeros positivos entre {inicio} e {fim}: {contador}")

def verificar_primos(numero):
    if  numero < 2:
         print(f"O número {numero} não é primo")
         return
    for i in range(2, int(numero ** 0.5) + 1):
         if numero % i == 0:
            print(f"O número {numero} não é primo")
            return
    print(f"O número {numero} é primo.")

def menu():
    while True:
         try:
            print("\n=== MENU DE FUNCIONALIDADES ===")
            print("a) Contar números pares em um intervalo")
            print("b) Exibir a tabuada de um número")
            print("c) Contar números positivos em um intervalo")
            print("d) Verificar se um número é primo")
            print("e) Sair do sistema")

            opcao = input("Escolha uma opção (a/b/c/d/e): ")

            if opcao == "a":
                inicio = int(input("Digite o valor inicial: "))
                fim = int(input("Digite o valor final: "))
                contar_pares(inicio, fim)
            
            elif opcao == "b":
                 numero = int(input("Digite um número para exibir a tabuada: "))
                 mostrar_tabuada(numero)

            elif opcao == "c":
                inicio = int(input("Digite o valor inicial: "))
                fim = int(input("Digite o valor final: "))
                contar_positvos(inicio, fim)

            elif opcao == "d":
                 numero = int(input("Digite um numero para verificar se é primo: "))
                 verificar_primos(numero)

            elif opcao == "e":
                 print("Encerrando Sistema Até logo!")
                 break
            else:
                 print("Opção inválida! Tente novamente.")
         except KeyboardInterrupt:
              print("Você interrompeu o programa. Até logo!")
              break
         
menu()
