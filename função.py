def bemVindo(qualquer="visitante"):
    print(f"Olá, seja bem vindo{qualquer}!")

nome = input("Informe o seu nome:")

while(nome == ""):
    print("Campo vazio, informe um valor válido")
    nome = input("Informe seu nome: ")
else:
    bemVindo(nome)


def somarValores(numero1,numero2):
    soma = numero1 + numero2
    print(f"O resultado da soma é: {soma}")

somarValores(5,2)


def somarValores2():
    numero1 = int(input("Digite o primeiro valor:"))
    numero2 = int(input("Digite o segundo valor:"))
    soma = numero1 + numero2
    print(f"O resultado da soma é: {soma}")

somarValores2()  



#Função lambda - função anonima


soma = lambda numero1, numero2: numero1 + numero2
print(soma(3,5))


soma = lambda numero1, numero2: numero1 + numero2

numero1 = float(input("digite o valor: "))
numero2 = float(input("digite o valor: "))
print(soma(numero1,numero2))

