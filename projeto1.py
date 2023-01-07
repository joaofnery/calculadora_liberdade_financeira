#Calculadora financeira - tempo para "liberdade financeira"
print('x-' * 50)
print('Veja qual o caminho para conquistar sua liberdade financeira.')
print('Aqui você poderá calcular quanto dinheiro você terá depois de um tempo investindo. ')
print('Ou dizer quanto dinheiro você pretende ter, para atingir sua liberdade financeira.')
print('x-' * 50)

nome = str(input('Qual o seu nome? ')).strip().capitalize()
print('Olá \033[1;32m{}\033[m, seja bem vindo(a)!!'.format(nome))
# Saber qual das calculadoras irá utilizar.
# Se vai ser investimento inicial, e aportes por um tempo determinado,
# ou, montante de dinheiro final, e tempo, para saber quanto deverá investir por mês.
print('Você deseja saber quanto terá investido após realizar aportes mensais por um tempo determinado, ou,')
print('dizer quanto você quer receber na sua aposentadoria e ver se irá chegar lá com os seus investimentos?')
escolha = int(input('\033[33mDigite 1 para a primeira opção\033[m ou \033[34mDigite 2 para a segunda opção.\033[m '))
if escolha == 1:
    jurosa = float(input('Qual a taxa de juros anual? Um valor médio seria 10% ao ano. Somente números. '))
#Conversão de juros anual para mensal
    jurosm = (1 + (jurosa / 100))**(1/12) - 1
#aporte mensal
    pmt = float(input('Qual o aporte mensal? '))
    tempo = int(input('Finalmente! Por quantos meses irá fazer os investimentos? '))
#Formula juros compostos com aporte mensal
    valorf = pmt * ((1 + jurosm)**tempo - 1) / jurosm
    print('Muito bom, {}!!'.format(nome))
    print('Você terá \033[1;32mR${:.2f}\033[m, no final dos {} meses.'.format(valorf, tempo))
elif escolha == 2:
    aposendesejada = float(input('Qual a renda mensal que você gostaria de receber na sua aposentadoria? '))
    print('Agora vamos ver se com os aportes mensais e o tempo até a sua aposentadoria, qual será sua renda.')
#Tempo
    idade = int(input('Quantos anos você tem? '))
    idadeaposen = int(input('Com quantos anos irá se aposentar? '))
    t = idadeaposen - idade
    t = t * 12
#aporte mensal
    pmt1 = float(input('Qual será seu aporte mensal? '))
#taxa de juros
    ia = float(input('Qual a taxa de juros anual? 10% é uma boa média. Somente números. '))
    im = (1 + (ia / 100))**(1/12) - 1
#Formula juros compostos com aporte mensal
    fv = pmt1 * ((1 + im)**t - 1) / im
    aposentadoria = fv * im
#Verificar o montante necessário para liberdade financeira de acordo com o input aposentadoria desejada.
    fvteorico = aposendesejada / im
    if fv >= fvteorico:
        print('\033[32mPARABÉNS {}!!\033[m Você irá atingir sua liberdade financeira'.format(nome))
        print('Você irá receber mensalmente \033[34mR${:.2f}\033[m e terá um total de R${:.2f}!'.format(aposentadoria, fv))
    else:
        print('Que pena, você não chegará na aposentadoria com o valor desejado. Procure fazer aportes maiores.')
        print('Você terá uma renda mensal de \033[31mR${:.2f}\033[m e um montante de R${:.2f}.'.format(aposentadoria, fv))
        pmt2 = (fvteorico * im) / ((1 + im)**t - 1)
        print('O seu aporte deveria ser de no minímo \033[31mR${:.2f}\033[m.'.format(pmt2))
