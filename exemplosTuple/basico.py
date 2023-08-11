frutas = {"maça", "uva"}
frutas.add("tomate")
print(frutas)
frutas2 = {"pera", "kiwi"}
frutas3 = {"amora", "caju"}
frutas.update(frutas2)
frutas.update(frutas3)
print(frutas)
frutas.remove("tomate")
frutas.discard("tangerina")
frutas.pop()
print(frutas)
frutas.clear()
print(frutas)
del(frutas)
print(frutas)
