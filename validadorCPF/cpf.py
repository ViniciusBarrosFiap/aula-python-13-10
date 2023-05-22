import re
def valida_cpf():
    for i in range(9):
        num = cpfUser[i]
    
    
    



def formatoCpf(cpf):
    if not re.search("\d{3}.\d{3}.\d{3}-\d{2}", cpf):
        print("Inválido")
    
    else:
        valida_cpf()

cpfUser = input("Digite seu CPF(000.000.000-00): ")
formatoCpf(cpfUser)

