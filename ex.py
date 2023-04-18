#calculando a media das notas (A e B) com pesos

A = float(input())
B = float(input())
MEDIA = (A * 3.5 + B * 7.5) / 11
print(f'MEDIA = {MEDIA:.5f}')


#calculando o consumo medio de litros por km 

X = int(input())
Y = float(input())
consumo_medio = X / Y
print (f'{consumo_medio:.3f}', 'km/l')

#calculando o salario com base em formula definida 

num_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora

print('NUMBER =', num_funcionario)
print ( f'SALARY = U$ {salario:.2f}')


#calculando o salario com bonus em formula definida 

vendendor = input()
salario_fixo = float(input())
total_vendas = float(input())

comissao = total_vendas * 0.15
salario_total = salario_fixo + comissao

print(f'TOTAL = R$ {salario_total:.2f}')
