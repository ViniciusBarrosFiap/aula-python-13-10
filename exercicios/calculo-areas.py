# Faça um programa que lê 4 valores I, A, B e C onde I
# é um número inteiro e positivo e A, B, e C são
# quaisquer valores reais. O programa deve escrever
# os valores lidos e:
# • se I = 1, calcular a área do quadrado com o valor A
# • se I = 2, calcular a área do retângulo com os valores A e B
# • se I = 3, calcular a área do triângulo com os valores A e B
# • se I = 4, calcular a área do trapézio com os valores A, B e C
# • se I não for um dos quatro valores acima, dar uma
# mensagem indicando isto.

print("""1, calcular a área do quadrado 
2, calcular a área do retângulo 
3, calcular a área do triângulo 
4, calcular a área do trapézio""")
opcoes = int(input())

match opcoes:
    case 1:
        altura_quad = float(input("Digite a altura do quadrado: "))
        largura_quad = float(input("Digite a largura do quadrado: "))

        area_quad = altura_quad * largura_quad

        print("A area do quadrado é igual a: ", area_quad)
    case 2:
        altura_ret = float(input("Digite a altura do retângulo: "))
        largura_ret = float(input("Digite a largura do retângulo: "))

        area_ret = altura_ret * largura_ret

        print("A area do retângulo é igual a: ", area_ret)
    case 3:
        altura_tri = float(input("digite a altura do triangulo: "))
        base_tri = float(input("digite a base: "))

        area_tri = (base_tri * altura_tri) / 2

        print("A area do triangulo equivale a:", area_tri)
    case 4:
        base_maior_trap = float(input("Digite a base maior do trapézio: "))
        base_menor_trap = float(input("Digite a base menor do trapézio: "))
        altura_trap = float(input("Digite a altura do trapézio: "))

        area_trap = ((base_maior_trap + base_menor_trap) * altura_trap) / 2

        print("A area do trapézio equivale a:", area_trap)
