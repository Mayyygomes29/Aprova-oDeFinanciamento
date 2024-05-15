from time import sleep
#Aprovação de emprestimos
casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário ? "))
anos = int(input("Quantos anos desejar pagar ? "))
porcentagem = (salario * 30)/100 

mensalidade = casa/(anos * 12)
print("\033[1;32mPROCESSANDO\033[m")
sleep(3)

if mensalidade<= porcentagem :
    print("Empréstimo liberado! ")
    print("Para pagar uma casa de R${:.2f} por {} anos,".format(casa, anos),end="")
    print(" a prestação será de \033[1;32mR${:.2f}\033[m".format(mensalidade))
else:
    print("Emprestimo recusado! Infelizmente você não pode financiar essa casa!")