# -*- coding: utf-8 -*-

# Script desenvolvido na linguagem Python para fins didáticos.
# Desafio de criação de uma Calculadora de Alcance de Anúncios.

# REQUISITOS
# Python 3
# https://www.python.org/downloads/

# INSTRUÇÔES PARA EXECUÇÂO
# 1 - Abra um terminal.
# 2 - Navegue até a pasta onde se encontra esse script. 
# 3 - Digite sem as aspas "python3 calculadora.py" e tecle ENTER.


# Importações necessárias
import math
import ast

# Cores para destaque no terminal
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"

# Função que exibe uma mensagem Boas Vindas.
def inicio():
    print(GREEN + '\nBem vindos!' + RESET)
    print(BOLD + 'Calculadora de Alcance de Anúncios - Divulga Tudo' + RESET)

# Chamamos a função de Boas Vindas.
inicio()

# Função que faz o cálculo.
def calcular():

    # Verificação do tipo de dado digitado pelo usuário.
    # Caso não for um número positivo gera um aviso.
    while True:
        try:
            valor = int(input('\nDigite o valor investido: R$ '))
            if valor <= 0:
                raise ValueError('Digite um valor positivo!')
        except ValueError as e:
            print('Digite um número inteiro para o Valor!')
        else:
            break

    # R$ 1 investido = 30 views.
    views = valor * 30

    # 100 views = 12 clicks (12/100 = 0.12).
    clicks = (views * 0.12)

    # 20 clicks = 3 compartilhamentos (3/20 = 0.15).
    share = (clicks * 0.15)

    # 1 compartilhamento = + 40 novas views (share * 40).
    # Consideramos que o anúncio foi compartilhado 4 vezes ((share * 40) * 4).
    # Por fim adicionamos as views do anúncio original ((share * 40) * 4) + views).

    resultado(int(((share * 40) * 4) + views))
       
# Função que pergunta ao usuário se deseja repetir o cálculo.
def recalcular():
    print('Deseja calcular novamente?')
    option = input(GREEN +'Digite S para SIM ou N para NÃO: ' + RESET)

    if option.upper() == 'S':
        # Chama a função que executa o cálculo.
        calcular()
    elif option.upper() == 'N':
        print(BLUE + '\nGratidão! Nos vemos em breve ;)' + RESET)
        print(BOLD + 'Desenvolvido por Josiane Andrade\n' + RESET)
        # Encerra a execução do script.
        quit()
    else:
        # Caso não seja digitado o valor esperado retorna a pergunta.
        recalcular()

# Imprime o resultado do cálculo.
def resultado(res):
    print('-----------------------------------------------------')
    print(GREEN + '>>> Quantidade aproximada de visualizações: %s' % res)
    print(RESET + '-----------------------------------------------------')
    recalcular()

# Chama a função que executa o cálculo.
calcular()
