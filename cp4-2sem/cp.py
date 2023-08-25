import random
import re
def escolheFuncionario(integrantes):
    numero = random.randint(0, 3)
    funcionario = integrantes[numero]
    return funcionario

integrantesGrupo = ("pedro", "Rodrigo", "Vinicius", "Guilherme")

funcionario = escolheFuncionario(integrantesGrupo)

vinhos = {
    "suvignon": {
        "preço": 50,
        "estoque": 5
    },
    "branco" :{
        "preço": 30,
        "estoque": 10
    },
    "suave": {
        "preço": 70,
        "estoque": 15
    },
    "tinto":{
        "preço": 20,
        "estoque": 40
    },
    "seco":{
        "preço": 50,
        "estoque": 0
    }
}

#Mensagem de boas vindas
print("BEM VINDO A VINHERIA AGNELLO")
print(f"O funcionário {funcionario} irá te atender")

# Validando nome
cliente = {}
nomeCliente = input("Por favor, diga seu nome: ")
while re.search(r"\d", nomeCliente):
    nomeCliente = input("Por favor, diga seu nome corretamente: ")

cliente["nome"] = nomeCliente

# Validando CEP
cepCliente = input(f"{nomeCliente}, por gentileza informe seu CEP: ")
while not re.search(r"\d{5}-\d{3}", cepCliente) or len(cepCliente) > 9:
    cepCliente = input(f"{nomeCliente}, por gentileza informe seu CEP corretamente (00000-000): ")

cliente["CEP"] = cepCliente

# Validando ano de nascimento:
anoNascimentoCliente = input(f"{nomeCliente}, por gentileza, informe seu ano de nascimento: ")
while not re.match(r"\d{4}", anoNascimentoCliente):
    anoNascimentoCliente = input(f"{nomeCliente}, por gentileza, informe seu ano de nascimento corretamente: ")
cliente["nascimento"] = anoNascimentoCliente

if int(anoNascimentoCliente) > 2005:
    print("Você é menor de idade, a venda de alcool para menores de idade é proibida")
    print("Obrigado por escolher a Vinheria Agnello")
else:
    for i in vinhos:
        if vinhos[i]["estoque"] >0:
            print(f"{i}   {vinhos[i]}  R$: {vinhos[i]['preço']}  {vinhos[i]['estoque']}")
    
    print("Escolha alguma opção:\n(1)\n(2)\n(3)\n(4)")
    escolha = int(input())
    if escolha != 1 and escolha !=2 and escolha != 3 and escolha != 4:
        print("opção inválida")
        raise ValueError
    vinho =""
    match escolha:
        case 1:
            vinho = "suvignon"
        case 2:
            vinho = "branco"
        case 3: 
            vinho = "suave"
        case 4:
            vinho = "tinto"
    print(f"Quantas garrafas você quer comprar do {vinhos[vinho]} ?")
    quantidade = int(input())
    if quantidade > vinhos[vinho]["estoque"]:
        print("Não temos essa quantidade no estoque, seu cachaceiro!")
        raise ValueError
    cliente.update({"Pagamento": dict(name = vinhos[vinho], price = (vinhos[vinho]["preço"]*quantidade), qtd = (quantidade))}) 
    vinhos[vinho]["estoque"] = vinhos[vinho]["estoque"] - quantidade
    print("\n")
    for x in vinhos:
        if vinhos[i]["estoque"] > 0:
            print(f"{i}   {vinhos[i]}  R$: {vinhos[i]['preço']}  {vinhos[i]['estoque']}")
    print("-"*40)
    print("Compra final:")
    print(f"{cliente['pagamento']['nome']}  R$: {cliente['pagamento']['preço']}  {cliente['pagamento']['estoque']}")
    print("Favor transferir o valor para o pix do professor Gilberto. Chave: Astrogildo")