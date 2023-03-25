milimetro = 25.4  # 1" = 25,4mm

polegada_input = float(input("Digite as polegadas: "))  # entrada de dados

mm = polegada_input * milimetro  # faz a conversão

print(f'{polegada_input}\" equivale a {mm:.2f} mm')
