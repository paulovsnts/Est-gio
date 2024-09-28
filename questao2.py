'''
Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
'''

def verificar(string):
    string_lower = string.lower()
    quantidade_a = string_lower.count('a')
    existe_a = quantidade_a > 0
    return existe_a, quantidade_a

entrada = input("Digite uma string: ")
existe, quantidade = verificar(entrada)

if existe:
    print(f"A letra 'a' aparece {quantidade} vez(es) na string.")
else:
    print("A letra 'a' não está presente na string.")
