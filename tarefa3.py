'''Os números de Fibonacci formam uma sequência em que cada número é igual à soma
dos dois anteriores. Os dois primeiros números são, por definição, iguais a 1. Veja o
exemplo a seguir: 1 1 2 3 5 8 13 ...
Escreva um programa que carregue um valor N pelo teclado e:
a) Imprima os N primeiros números da sequência de Fibonacci;
b) Indique se N faz parte da sequência de Fibonacci. '''
#comando de digitalização do usuario
print('-'*40)
numero = int(input('Digite um Valor inteiro: '))
#variáveis
pri,ulti = 1,1
lista = []
# o primeiro sempre vai substituir o proximo e somando > 1 + 1 = 2 , 1 + 2 = 3, 2 + 3 = 5...
for i in range(numero):
    lista.append(pri)
    pri, ulti = ulti, pri + ulti
#aqui se o numero digitado estiver dentro da lista quer dizer que , sim esta
if numero in lista:
    print('-'*40)
    print(f'O Numero digitado esta na Sequencia: {numero}')
    print('-'*40)
# caso o numero nao esteja
else:
    print('-'*40)
    print('O numero Digitado nao esta na lista! ')
    print('-'*40)
#pra mostrar o resultado
print(f"Os {numero} primeiros números da sequência de Fibonacci são: {lista} ")
print('-'*40)