from random import randint
from time import sleep
computador = randint(0, 5) 
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
jogador = int(input('Em que número eu pensei? '))
print('processando...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! eu Pensei no número {} e não no número {}!'.format(computador, jogador))
