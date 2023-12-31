'''
Números em ponto flutuante podem ser bastante extensos para mostrar.
Nesses casos, é conveniente usar a notação científica.

Você deve escrever um programa que, dado um número em ponto flutuante,
mostre este número na notação científica: sempre mostre o sinal da mantissa;
sempre mostre 4 casas decimais na mantissa; use o caractere 'E' para separar
a mantissa do expoente; sempre mostre o sinal do expoente; e mostre o expoente
com pelo menos 2 dígitos.

Entrada
A entrada é um número em ponto flutuante de dupla precisão X (de acordo com o
padrão IEEE 754-2008). Nunca haverá um número com mais de 110 caracteres
nem com mais de 6 casas decimais.

Saída
A saída é o número X em uma única linha na notação científica detalhada acima
'''

# Variaveis:
# float number, exp_number, mantissa, exponent, negative_exponent, final_number

# Entrada
float_number = float(input())

# Processamento
exp_number = "{:.4E}".format(float_number)
mantissa, exponent = exp_number.split('E')

# Saída
if float_number > 0:
    final_number = '+' + mantissa + 'E' + exponent
else:
    negative_exponent = exponent.replace('+', '-')
    final_number = mantissa + 'E' + negative_exponent

print(final_number)
