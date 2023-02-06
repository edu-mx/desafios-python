print('Calculo do IMC.')
nome=input('Digite o seu nome')
peso=float(input('Digite o seu peso:'))
altura=float(input('Digite a sua altura:'))
print('Calculando...')
altura_ao_quadrado = altura * altura
imc = peso / altura_ao_quadrado
imc_resultado = str(imc)
print('o seu IMC é:')
print(f'{imc:.2f}')
