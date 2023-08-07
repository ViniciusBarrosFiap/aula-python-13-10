import random

def desenhaForca():
    forca

def escolhePalavraEFraseAleatoria():
    palavras = ['HIPOCRITA', 'IGNORANTE', 'CONSTANTE']
    numero = random.randint(0,2)
    palavraSecreta = palavras[numero]
    frases = ['Julga mas faz igual', 'Não busca conhecimento', 'Que fica em movimento...']
    fraseSecreta = frases[numero]
    return palavraSecreta, fraseSecreta


def mostraPalavra(palavra, chute):
    palavraExibida = ''
    lista = []
    for letra in palavra:
        lista.append(letra)
    for i in lista:
        if letra in chute:
            palavraExibida += letra
        else:
            palavraExibida += "_ "

    print(palavraExibida,)
    
            
        
    

def inputUsuario():
    chute = input("\nDigite uma letra: ").upper()
    return chute


pSecreta = escolhePalavraEFraseAleatoria()[0]
print(pSecreta)

while True:
    palpite = inputUsuario()
    mostraPalavra(pSecreta, palpite)

           