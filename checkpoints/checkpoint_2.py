import random

#sorteio do funcionario
sorteio = random.randint(1,5)
if sorteio == 1:
    nomefunc = "Vinicius"
elif sorteio == 2:
    nomefunc = "Pedro"
elif sorteio == 3:
    nomefunc = "Ricardo"
elif sorteio == 4:
    nomefunc = "Guilherme"
elif sorteio == 5:
    nomefunc = "João"

#Mensagem de boas vindas
print(f"""Bem-vindo a vinheria Agnelo.\nO 
{nomefunc} irá relizar seu atendimento""")

#Perguntando informações do cliente
nome = input("Informe seu nome:\n")
cep = int(input("Informe seu CEP:\n"))
anonasc = int(input("Informe o ano de seu nascimento: "))

#verifica a maioridade
maioridade = 2023 - anonasc

if maioridade < 18:
    print(f"{nome}, você é menor de idade e não é permitido a venda para menores de idade")
else:
    #variáveis para auxiliar os cálculos
    subtotal = total = 0

    #preparando a mensagem final
    msgfinal = f"""Dados da compra:\n
    Atendido por:{nomefunc}\n
    Cliente: {nome}\n 
    Itens da compra\tValor\tQuantidade\tSubtotal"""

    #repetindo a venda de vinhos
    continua = "sim"
    while continua.lower() == "sim":
        #exibindo opções de vinhos
        print("""Escolha um dos vinhos da lista:\n
(1)Vinho suave tinto\tR$ 15.00
(2)Vinho seco tinto\tR$ 25.00
(3)Vinho suave branco\tR$ 35.00
(4)Vinho seco branco\tR$ 30.00
(5)Vinho sem álcool\tR$ 40.00""")

        #armazenamento do vinho escolhido e a quantidade
        vinho = int(input())
        quantidade = int(input("Em qual quantidade deseja adquirir este vinho ?\n"))

        match vinho:
            case 1:
                subtotal = 15 * quantidade
                msgfinal += f"Vinho suave tinto\t R$ 15.00\t{quantidade}\tR$ {subtotal :.2f}\n"
            case 2:
                subtotal = 25 * quantidade
                msgfinal += f"Vinho seco tinto\t R$ 25.00\t{quantidade}\tR$ {subtotal :.2f}\n"
            case 3:
                subtotal = 35 * quantidade
                msgfinal += f"Vinho suave branco\t R$ 35.00\t{quantidade}\tR$ {subtotal :.2f}\n"
            case 4:
                subtotal = 30 * quantidade
                msgfinal += f"Vinho seco branco\t R$ 30.00\t{quantidade}\tR$ {subtotal :.2f}\n"
            case 5:
                subtotal = 40 * quantidade
                msgfinal += f"Vinho sem álcool\t R$ 40.00\t{quantidade}\tR$ {subtotal :.2f}\n"
            case _ :
                print("Por favor escolha uma das opções da lista")
        
        total += subtotal #total = total + subtotal

        #continuando ou não a compra
        continua = input("Deseja continuar a compra ? responda: sim ou não\n")

    #Exibindo informções finais
    print(msgfinal)
    print(f"Total da compra foi {total}")

    #Verificando frete
    if total < 200:
        print("Valor do frete R$ 30.00")
    else:
        print("FRETE GRÁTIS!")

#Exibindo mensagem de despedida
print(f"{nome}, foi um prazer atende-lo. Volte sempre")