pokemons = ("Charmeleon", "FOGO", "Charmander", "FOGO", "Charizard", "FOGO", "Squirtle", "Agua", "Blastoise", "Agua", "Metapod", "Inseto", "Pidgeoto", "Normal","Pidgey", "Normal", "Rattata", "Normal", "Raticate", "Normal")

pokemonUser = input("Digite um tipo de pokemon: ").upper()

if pokemonUser == "FOGO":
    print(pokemons.count("FOGO"))
    for i in pokemons:
        if i == "FOGO":
            i += 1
            print(i-1)
    
        

