# DESAFIO 004

# Faça um programa que leia pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

test = input("Digite alguma coisa: ")
print()
print(f"O valor informado \033[34m{test}\033[0m, é alfanúmerico?(possui letras ou/e números) \033[36m{test.isalnum()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, possui apenas letras? \033[36m{test.isalpha()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, possui apenas números? \033[36m{test.isnumeric()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, são decimais (apenas números)? \033[36m{test.isdecimal()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, é ASCII? \033[36m{test.isascii()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, são digitos (0-9)? \033[36m{test.isdigit()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, é um indetifcador válido em Python? \033[36m{test.isidentifier()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, possui todos os caracteres imprimíveis? \033[36m{test.isprintable()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, possui apenas espaços em branco? \033[36m{test.isspace()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, cada palavra em sua composição começa com letras maiusculas? \033[36m{test.istitle()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, todos os caracteres são maiúsculos? \033[36m{test.isupper()}\033[0m")
print(f"O valor informado \033[34m{test}\033[0m, todos os caracteres são minúsculos? \033[36m{test.islower()}\033[0m")