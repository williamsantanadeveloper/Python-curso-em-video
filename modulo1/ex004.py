#Desafio 004
x = input("Digite algo: ")

print(f"Qual o tipo? {type(x)}")
print(f"É boleâno? {bool(x)}" )
print(f"É númerico? {x.isnumeric()}.")
print(f"É alfabético?{x.isalpha()}.")
print(f"É alfabético e numérico? {x.isalnum()}.")
print(f"Tem somente letras maiúsculas? {x.isupper()}")
