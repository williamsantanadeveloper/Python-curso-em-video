#Desafio 010
reais = float(input("Quantos reais você tem? "))
conversor = reais / 3 
print(f"Da para comprar {conversor:.1f} doláres")

#Desafio 011
largura = float(input("Informe a largura: "))
altura = float(input("Informe a altura: "))
area = largura * altura
print(f"A sua parede tem dimensão {largura}x{altura} e sua área é de {area}m.")
tinta = area / 2
print(f"Você precisa de {tinta}l para pintar a parede.")