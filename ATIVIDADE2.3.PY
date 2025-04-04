nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
nota3 = float(input("Digite a terceira nota"))

media = (nota1 + nota2 + nota3)/3

# aprovado >= 7 / recuperação >= 5 < 7 / reprovado < 5

if (media >= 7):
    print("Aluno aprovado!")
elif (media >= 5) and (media <7):
    print("Aluno recuperação!")
else:
    print("Aluno reprovado!")
    
            

