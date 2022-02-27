from time import sleep

print('''
        CADASTRO
    ''')
nome = str(input('Digite seu nome:'))
while len(nome) < 6 or len(nome) > 100:
    nome = str(input('Digite seu nome:'))

print()

print('-' * 50)
idade = int(input('Digite sua idade:'))
while idade <= 17 or idade >= 100:
    idade = int(input('Digite seu idade:'))

print()

print('-' * 50)
peso = float(input('Digite seu peso:'))
while peso <= 10 or peso >= 100:
    peso = float(input('Digite seu peso:'))

print()

print('-' * 50)
altura = float(input('Digite sua altura:'))
while altura <= 0:
    altura = float(input('Digite sua altura:'))

print()

print('-' * 50)
sexo = input('[M] ou [F]:').upper()
while sexo != 'F' and sexo != 'M':
    sexo = input('[M] ou [F]:').upper()

print('CARREGANDO...')

sleep(2)
print()
print('=' * 20)
print('NOME:', nome)
print('IDADE:', idade)
print('PESO:', peso)
print('ALTURA:', altura)
print('SEXO:', sexo)
print('=' * 20)
