""" #Ex. 067
while True:
    num = int(input("Digite um número para ver sua tabuada: "))
    if num >= 0:
        print("-"*20)
        for cont in range(1, 11): 
            print(f"{num} x {cont:>2} = {num*cont}")
        print("-"*20)
        print("")
    else:
        break
print("\nPrograma finalizado!") """

""" #Ex. 068
numJog = numComp = vit = 0
from random import randint
while True:
    #Escolher Par ou Impar
    while True:
        jog = str(input("\nJogue ímpar ou par (I/P): ")).strip().upper()
        if "P" != jog != "I":
            print("Opção Inválida!")  
        else:
            break
    #Escolher número
    print("-"*20)
    numJog = int(input("Jogue um número: "))
    numComp = randint(0, 100)
    print("-"*20)
    #Análise
    print(f"Você jogou {numJog} e o computador, {numComp}")
    if ((numJog + numComp)%2 == 0) and (jog == "P"):
        print("\n\033[32mPARABÉNS, VOCÊ GANHOU!\033[m")
        vit += 1
        print("-"*23)
    elif ((numJog + numComp)%2 == 0) and (jog == "I"):
        print("\n\033[31mQUE PENA, O COMPUTADOR GANHOU!\033[m")
        break
    elif ((numJog + numComp)%2 != 0) and (jog == "I"):
        print("\n\033[32mPARABÉNS, VOCÊ GANHOU!\033[m")
        vit += 1
        print("-"*23)
    elif ((numJog + numComp)%2 != 0) and (jog == "P"):
        print("\n\033[31mQUE PENA, O COMPUTADOR GANHOU!\033[m")
        break
print(f"\n\033[33mVocê venceu {vit} veze(s)\033[m") """

""" #Ex. 069
sex = resp = ""
idad = pesMa18 = hom = mulMe20 = 0
while True:
    print("-"*22)
    while True:
        sex = str(input("Digite seu sexo (M/F): ")).strip().upper()
        if sex == "M":
            #Número de homens
            hom += 1
            break
        elif sex == "F":
            break
        else:
            print("Opção inválida!")
    idad = int(input("Digite sua idade: "))
    #Pessoas com mais de 18 anos
    if idad > 18:
        pesMa18 += 1
    #Mulheres com menos de 20 anos
    if (idad < 20) and (sex == "M"):
        mulMe20 += 1
    while True:
        resp = str(input("\nDeseja continuar (S/N)? ")).strip().upper()
        if "S" != resp != "N":
            print("Opção inválida!")
        elif (resp == "S") or (resp == "N"):
            break
    if resp == "N":
        break
print("-"*25)
print("\n---Resumo---")
print(f"Pessoas com mais de 18 anos: {pesMa18}")
print(f"Homens cadastrados: {hom}")
print(f"Mulheres com menos de 20 anos: {mulMe20}") """

""" #Ex. 070
from math import inf
tot = prodMa1000 = 0
prodMaBara = inf
nomProdMaBara = resp = ""
print("-"*25)
print("     LOJAS AFRICANAS")
print("-"*25)
while True:
    print("")
    prod = str(input("Digite o nome do produto: "))
    prec = float(input("Digite o preço do produto: R$"))
    #Total da compra
    tot += prec
    #Produtos que custam mais de R$1000,00
    if prec > 1000:
        prodMa1000 += 1
    #Nome do produto mais barato
    if prec < prodMaBara:
        prodMaBara = prec
        nomProdMaBara = prod
    while (resp != "S") and (resp != "N"):
        resp = str(input("Deseja continuar (S/N)? ")).strip().upper()
    if resp == "N":
        break
    #Reinicialização da resposta
    resp = ""
print("-"*25)
print("\n---Resumo---")
print(f"Total gasto na compra: R${tot:.2f}")
print(f"Produtos que custam mais de R$1000,00: {prodMa1000}")
print(f"Nome do produto mais barato: {nomProdMaBara}") """

""" #Ex. 071
C100 = C50 = C20 = C10 = C5 = C2 = C1 = 0
print("-"*25)
print("     Caixa Pythonico")
print("-"*25)

print('''\nCédulas disponíveis: 
\033[32m[R$100,00]
[R$50,00]
[R$20,00]
[R$10,00]
[R$5,00]
[R$2,00]
[R$1,00]\033[m''')

saque = float(input("\nQual valor deseja sacar (só valores inteiros)? R$"))
#Cédulas de R$100
C100 = saque//100
saque = saque%100
#Cédulas de R$50
C50 = saque//50
saque = saque%50
#Cédulas de R$20
C20 = saque//20
saque = saque%20
#Cédulas de R$10
C10 = saque//10
saque = saque%10
#Cédulas de R$5
C5 = saque//5
saque = saque%5
#Cédulas de R$2
C2 = saque//2
saque = saque%2
#Cédulas de R$1
C1 = saque//1

print(f'''\nCédulas entregues:
\033[33m{C100:.0f}\033[m nota(s) de \033[32m[R$100,00]\033[m
\033[33m{C50:.0f}\033[m nota(s) de \033[32m[R$50,00]\033[m
\033[33m{C20:.0f}\033[m nota(s) de \033[32m[R$20,00]\033[m
\033[33m{C10:.0f}\033[m nota(s) de \033[32m[R$10,00]\033[m
\033[33m{C5:.0f}\033[m nota(s) de \033[32m[R$5,00]\033[m
\033[33m{C2:.0f}\033[m nota(s) de \033[32m[R$2,00]\033[m
\033[33m{C1:.0f}\033[m nota(s) de \033[32m[R$1,00]\033[m''') """
