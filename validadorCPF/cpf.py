import re
verificador1 = 0
verificador2 = 0

def valida_cpf():
    soma1 = soma2 = div1 = 0

    
    num1 = cpf[0]
    num2 = cpf[1]
    num3 = cpf[2]
    num4 = cpf[4]
    num5 = cpf[5]
    num6 = cpf[6]
    num7 = cpf[8]
    num8 = cpf[9]
    num9 = cpf[10]
    num10 = cpf[12]
    num11 = cpf[13]

    nums_cpf = [num1,num2,num3,num4,num5,num6,num7,num8,num9]
    multiplicacao1 = []
    multiplicacao2 = []
    indice = 10

    for i in nums_cpf:
        multiplicacao1.append(int(i)*indice)
        indice -= 1

    for i in multiplicacao1:
        soma1 += i

    div1 = soma1 % 11

    if div1 < 2:
        verificador1 = 0
    else:
        verificador1 = 11 - div1

    indice = 11
    nums_cpf.append(num10)

    for i in nums_cpf:
        multiplicacao2.append(int(i)*indice)
        indice -= 1
    
    for i in multiplicacao2:
        soma2 += i
    
    div2  = soma2 % 11
    
    if div2 < 2:
        verificador2 = 0
    else:
        verificador2 = 11 - div2

    if int(num10) == verificador1 and int(num11) == verificador2:
        print("CPF válido")
    else:
        print("CPF inválido")

def formato_cpf(cpfUser):
    if not re.search("\d{3}.\d{3}.\d{3}-\d{2}", cpfUser):
        print("CPF no formato errado. Digite no formato: 000.000.000-00")
    else:
        valida_cpf()
cpf = input("Digite seu CPF:")
formato_cpf(cpf)