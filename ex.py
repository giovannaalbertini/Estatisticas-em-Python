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
