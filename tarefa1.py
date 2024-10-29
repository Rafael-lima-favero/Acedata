'''1) Desenvolver um sistema para calcular o valor que será pago a um 
empregado horista. O usuário deverá informar o valor do salário hora, 
a quantidade de horas trabalhadas no mês e a quantidade de filhos menores de 14 anos. 
A partir daí o sistema deve calcular o
salário bruto, salário família e o salário líquido do empregado 
(salário bruto + salário família).
Para o cálculo do salário família, levar em consideração:
a) Se o salário bruto for até R$ 788,00 o salário família será de R$ 30,50 para cada
filho.
b) Se o salário bruto for acima de R$ 788,00 até R$ 1.100,00 o salário família será de
R$ 18,50 por filho.
c) Se o salário bruto for acima de R$ 1.100,00 o salário família será de R$ 11,90 por
filho.'''

# Variáveis
salario_hora = float(input("Digite o Valor da sua Hora: " ))
qtd_hora = int(input("Digite a Quantidade de Horas Trabalhadas no mês: "))
qtd_filhos = int(input("Digite a quantidade de filhos menores de 14 anos: "))

#Calculos
Sl_bruto = salario_hora * qtd_hora
print('-'*40)
print(f'O Salario Bruto é de: {Sl_bruto} ')

if Sl_bruto <= 788:
    sl_fml = 30.50 * qtd_filhos
    salario_liquido = Sl_bruto + sl_fml
    print('-'*40)
    print(f'Seu Salario Familia é de: {sl_fml}')
    print('-'*40) 
    print(f'Seu Salario Liquido Total é: {salario_liquido} ')

elif Sl_bruto <= 1100:
    sl_fml = 18.50 * qtd_filhos
    salario_liquido = Sl_bruto + sl_fml
    print('-'*40)
    print(f'Seu Salario Familia é de: {sl_fml}')
    print('-'*40)
    print(f'Seu Salario Liquido Total é: {salario_liquido} ')

else:
    sl_fml = 11.90 * qtd_filhos
    salario_liquido = Sl_bruto + sl_fml
    print('-'*40)
    print(f'Seu Salario Familia é de: {sl_fml}')
    print('-'*40)
    print(f'Seu Salario Liquido Total é: {salario_liquido} ')

print('-'*40)