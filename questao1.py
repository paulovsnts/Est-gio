'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Inicialização as variáveis com os dois primeiros números da sequências de fibonacci
a, b = 0, 1
sequencia = [a, b]

# Geração da sequência de Fibonacci
while b < numero:
    a, b = b, a + b
    sequencia.append(b)

# Verificação se o número pertence à sequência
pertence = False
for num in sequencia:
    if num == numero:
        pertence = True
        break

# Exibição do resultado
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# Exibição da sequência gerada
print(f"Sequência de Fibonacci até {numero}:")
for num in sequencia:
    if num > numero:
        break
    print(num, end=" ")
print()