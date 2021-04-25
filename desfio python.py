from random import randint
from time import sleep

lista = list()
cont = 0
while True:
  num = randint(1, 60)
  if num not in lista:
      lista.append(num)
      cont += 1
  if cont >= 6:
    break
lista.sort()
print("digite num papel seus numeros e depois analise se voce ganhou ou perdeu")
sleep(5)
print(f'\033[32m os numeros da sorte foi {lista}\033[m') 
sleep(2)
print('\033[31mse voce acertou os 6 numeros da mega sena parabéns voce ganhou na mega sena\033[m')
sleep(2)
print('fim do programa')

























