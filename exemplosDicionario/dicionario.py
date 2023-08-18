dicionario = {
    "montadora": "Ford",
    "modelo":"Mustang",
    "ano": 1964
}
# dicionario = dict(montadora = "Ford",
#                   modelo = "Mustang",
#                   ano = 2000)
# print(dicionario["modelo"])
# print(dicionario.get("modelo"))
# print(dicionario.keys())
# print(dicionario.values())

# dicionario["ano"] = 2023
# print(dicionario)

# dicionario.update({"modelo": "ferrari", "ano": 2023})
# dicionario["cor"] = "Preto"
# dicionario.update({"cor":"amarelo", "motor": 5.0})
# dicionario.pop("montadora")
# dicionario.popitem()
# print(dicionario)

# for i in dicionario.keys():
#     print(i)
for i in dicionario.values():
    print(i)