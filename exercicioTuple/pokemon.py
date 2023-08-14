#RM97824 - Vinicius Oliveira de Barros
def verificaPokemon(pokemons, tipo):
    contador = 0
    pokemons_tipo = []
    for i in range(0, len(pokemons), 2):
        if pokemons[i + 1] == tipo:
            contador += 1
            pokemons_tipo.append(pokemons[i])
    if contador == 0:
        print(f"não existe pokemons do tipo: {tipo}")
    else:
        pokemons_formatado = ", ".join(pokemons_tipo)
        print(f"A tupla possui {contador} do tipo {tipo} e eles são: {pokemons_formatado}")

pokemons = ("Charmeleon", "FOGO", "Charmander", "FOGO", "Charizard", "FOGO", "Squirtle", "AGUA", "Blastoise", "AGUA", "Metapod", "INSETO", "Pidgeoto", "NORMAL","Pidgey", "NORMAL", "Rattata", "NORMAL", "Raticate","NORMAL")
pokemonUser = input("Digite um tipo de pokemon: ").upper()

verificaPokemon(pokemons, pokemonUser)