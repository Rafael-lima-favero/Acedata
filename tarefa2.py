'''Desenvolver um sistema que receba uma sequência de números digitada pelo usuário. 
O primeiro valor informado será a quantidade de números a ser digitada, 
e em seguida, a sequência de números. No final o sistema deverá apresentar:
a) A própria sequência digitada pelo usuário.

b) O menor e o maior número da sequência. '''

#Variável
usuario = int(input('Digite a Quantidade de numeros a ser digitado:  '))
#lista
numeros = []
#quantidade para ser repetida é adicionando o numero na lista
for i in range(usuario):
    numero = int(input(f'digite o {i + 1} numeros desejados: '))
    numeros.append(numero)
#codigo do maior e menor
maior = max(numeros)
menor = min(numeros)
#mostrar o resultado
print('-'*40)
print(f'Sequencia: {numeros}')
print('-'*40)
print(f'Maior numero é {maior}')
print('-'*40)
print(f'Menor numero é {menor}')
print('-'*40)