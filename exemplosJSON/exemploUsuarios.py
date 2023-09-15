import json
usuarios = {
    "astro":{
        "nome":"Astrogildo",
        "login": "astro",
        "senha": "123"
    },
    "beri": {
        "nome":"Berisvaldo",
        "login": "beri",
        "senha": "456"
    }
}
try:
    with open("d:/usuarios.json","w") as arquivo:
        json.dump(usuarios, arquivo)

except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente!")