# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

opcoes = ('0','1','2','3','4')
menu = ("""
"******************* Calculadora em Python *******************"  
            
    Selecione uma das opções:
    0 - Sair
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão

"*************************************************************" 
        
Digite a operação desejada(0/1/2/3/4): """)



def adicao(n1, n2):
    resultado = n1 + n2
    return resultado

def subtracao(n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicacao(n1, n2):
    resultado = n1 * n2
    return resultado

def divisao(n1, n2):
    resultado = n1 / n2
    return resultado



while True:
    opcao = input(menu)

    if opcao == '0':
        break

    elif opcao not in opcoes:
        print("\nOperação inválida, por favor selecione novemente a operação desejada.")
        pass
    
    else:
        numero1 = float(input("\nDigite o primeiro número: "))
        numero2 = float(input("\nDigite o segundo número: "))

        if opcao == '1':
            print(f'\n{numero1} + {numero2} = {adicao(numero1, numero2)}')

        elif opcao == '2':
            print(f'\n{numero1} - {numero2} = {subtracao(numero1, numero2)}')

        elif opcao == '3':
            print(f'\n{numero1} * {numero2} = {multiplicacao(numero1, numero2)}')

        elif opcao == '4':
            if numero2 == 0:
                print('\nNão é possível realizar divisão por zero.')
            else: 
                print(f'\n{numero1} / {numero2} = {divisao(numero1, numero2)}')