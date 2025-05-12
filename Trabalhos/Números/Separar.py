numero = int (input("Digite sua Senha"))

if numero <1000 or numero >9999:
    print("Este número não tem 4 dígitos")
else:

    milhar = numero // 1000
    centena = (numero // 100) %10
    dezena = (numero // 10) %10
    unidade = numero %10

    print("Milhar:", milhar)
    print("Centena:", centena)
    print("Dezena:", dezena)
    print("Unidade:", unidade)
    if milhar == centena or milhar == dezena or milhar == unidade or centena == dezena or centena == unidade or dezena == unidade:
        print("Digitos iguais")
    else:
        print("Não há dígitos repetidos")

soma = unidade + dezena + centena + milhar
print("a soma é", soma)

if milhar == unidade or centena == dezena:
    print("é um palindromo")
else: 
    print("não é um palindromo")

maiorvalor = max(unidade, dezena, centena, milhar)
print("O maior valor:", maiorvalor)

if (maiorvalor==unidade):
    print("O maior valor é a unidade")

if (maiorvalor==dezena):
    print("O maior valor é a dezena")

if (maiorvalor==centena):
    print("O maior valor é a centena")

if (maiorvalor==milhar):
    print("O maior valor é a milhar")