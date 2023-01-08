casa = float(input('Qual o valor da casa que você quer comprar? R$'))
salario = float(input('Qual é o seu salário mensal? R$'))
prazo = int(input('Em quantos \033[1;31mANOS\033[m você quer financiar a casa? '))

prestacao = casa / (prazo * 12)

if prestacao > 0.3 * salario:
    print('Seu financiamento foi \033[1;31mNEGADO!!\033[m')
    print('Sua prestação ficou no valor de {:.2f} reais.'.format(prestacao))
else:
    print('\033[1;32mPARABENS!\033[m Seu financiamento foi aprovado!')
    print('Sua prestação ficou no valor de {:.2f} reais.'.format(prestacao))
