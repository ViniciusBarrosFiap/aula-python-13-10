import random
import re
def escolheFuncionario(integrantes):
    numero = random.randint(0, 3)
    funcionario = integrantes[numero]
    return funcionario

integrantesGrupo = ("pedro", "Rodrigo", "Vinicius", "Guilherme")

funcionario = escolheFuncionario(integrantesGrupo)

vinhos = {
    1: {
        "nome": "Rosé",
        "preço": 50,
        "estoque": 5
    },
    2 :{
        "nome": "branco",
        "preço": 30,
        "estoque": 10
    },
    3: {
        "nome": "suave",
        "preço": 70,
        "estoque": 15
    },
    4:{
        "nome": "tinto",
        "preço": 20,
        "estoque": 40
    },
    5:{
        "nome": "seco",
        "preço": 50,
        "estoque": 0
    }
}

#Mensagem de boas vindas
print("BEM VINDO A VINHERIA AGNELLO")
print(f"O funcionário {funcionario} irá te atender")

# Validando nome
cliente = {}
nomeCliente = input("Por favor, diga seu nome:\n")
while re.search(r"\d", nomeCliente):
    nomeCliente = input("Por favor, diga seu nome corretamente:\n")

cliente["nome"] = nomeCliente

# Validando CEP
cepCliente = input(f"{nomeCliente}, por gentileza informe seu CEP:\n")
while not re.search(r"\d{5}-\d{3}", cepCliente) or len(cepCliente) > 9:
    cepCliente = input(f"{nomeCliente}, por gentileza informe seu CEP corretamente (00000-000):\n")

cliente["CEP"] = cepCliente

# Validando ano de nascimento:
anoNascimentoCliente = input(f"{nomeCliente}, por gentileza, informe seu ano de nascimento:\n")
while not re.match(r"\d{4}", anoNascimentoCliente):
    anoNascimentoCliente = input(f"{nomeCliente}, por gentileza, informe seu ano de nascimento corretamente:\n")
cliente["nascimento"] = anoNascimentoCliente

if int(anoNascimentoCliente) > 2005:
    print("Você é menor de idade, a venda de alcool para menores de idade é proibida")
    print("Obrigado por escolher a Vinheria Agnello")

else:
    print("=="*50)
    print("Opções\t Vinhos\t\t Preço")
    for i in vinhos:
        if vinhos[i]["estoque"] >0:
            print(f"{i}\t {vinhos[i]['nome']}\t\t R$: {vinhos[i]['preço']}")

    print("=="* 50)
    print("Escolha uma opção:\n(1)\n(2)\n(3)\n(4)")

    escolha = int(input())

    if escolha != 1 and escolha !=2 and escolha != 3 and escolha != 4:
        print("opção inválida")
        raise ValueError
    vinho = ""
    match escolha:
        case 1:
            vinho = "Rosé"
        case 2:
            vinho = "Branco"
        case 3: 
            vinho = "Suave"
        case 4:
            vinho = "Tinto"

    quantidade = int(input(f"Quantas garrafas de {vinho} você quer comprar ?\n"))

    if quantidade > vinhos[escolha]["estoque"]:
        print("Não temos essa quantidade no estoque!")
        
    cliente.update({"pagamento": {"nome": vinho, "preço": vinhos[escolha]["preço"] * quantidade, "quantidade": quantidade}})

    vinhos[escolha]["estoque"] -= quantidade
    
    print("==" * 50)
    print("Compra final:")
    print("Vinho\t Preço\t Quantidade\t Total")

    print(f"{cliente['pagamento']['nome']}\t {vinhos[escolha]['preço']}\t {cliente['pagamento']['quantidade']}\t\t R$: {cliente['pagamento']['preço']}\n")
    print("Favor transferir o valor para o pix do professor Gilberto. Chave: Astrogildo")
    print("=="* 50)
    print("\nEstoque atualizado:")
    print("Opções\t Preço\t Estoque")
    for i in vinhos:
        if vinhos[i]["estoque"] > 0:
            print(f"{i}\t R$: {vinhos[i]['preço']}\t {vinhos[i]['estoque']}")