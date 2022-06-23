def dimensoesObjeto():
    while True: 
        try: #tentativa para a entrada dos valores das dimensões do objeto.
            c = float(input('Digite a comprimento do objeto(cm): '))
            l = float(input('Digite a  largura do objeto(cm): '))
            h = float(input('Digite a altura do objeto(cm): '))
            D = c * l * h #o cálculo das dimensões serão armazenados na variável D.
            print('O volume do Objeto é de:', D, 'cm³')
            if D < 1000:
                return 10
            elif 1000 <= D < 10000:
                return 20
            elif 10000 <= D < 30000:
                return 30
            elif 30000 <= D < 100000:
                return 50
            else: #caso nenhuma das condições sejam concedidas retornará que o volume é excedente.
                print('Volume muito excedente')
                print('Entre com as dimensões desejadas novamente')
                continue #o programa continuará no começo do laço para que o usuário entre com as dimensões novamente
        except ValueError: #caso o usuário não digite um valor númerico, será retornado o erro
            print('Você digitou alguma dimensão do objeto com valor não númerico')
            print('Entre com as dimensões desejadas novamente')
            continue 
def pesoObjeto():
    while True:
        try:
            peso = float(input('Entre com o peso do objeto(kg): ')) #a variavel peso receberá o peso do produto
            if peso < 0.1:
                return 1
            elif 0.11 <= peso < 1 :
                return 1.5
            elif 1.10 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else: #caso nenhuma das condições sejam concedidas retornará que o peso é excedente
                print('Não aceitamos objetos tão pesados!')
                print('Entre com o peso novamente')
                continue 
        except ValueError: 
            print('Você digitou o peso do objeto com um valor não númerico')
            print('Entre com o peso novamente')
            continue 
def rotaObjeto():
    while True: 
        rota = input('Selecione a rota:\n'
                  'RS - De Rio de Janeiro até São Paulo \n'
                  'SR - De São Paulo até Rio de Janeiro \n'
                  'BS - De Brasília até São Paulo \n'
                  'SB - De São Paulo até Brasília \n'
                  'BR - De Brasília até Rio de Janeiro \n'
                  'RB - Rio de Janeiro até Brasília\n'
                  '>> ')
        if rota == 'RS' or rota == 'SR':
            return 1
        elif rota == 'BS' or rota == 'SB':
            return 1.2
        elif rota == 'BR' or rota == 'RB':
            return 1.5
        else: #caso nenhuma das condições sejam concedidas retornará que a rota é inexistente.
            print('Você digitou uma rota que não existe!')
            print('Por favor entre com a rota desejada novamente!')
            continue 

print('Seja Bem Vindo a Companhia de Logística Ghabriel Machado Rodrigues S.A.') 
dim = dimensoesObjeto()
pesoO = pesoObjeto()
rotaO = rotaObjeto()

total = dim * pesoO * rotaO #o valor total é calculado pela multiplicação dos valores retornados das funções

print('Total a pagar (R$): {:.2f} (dimensoes: {} * peso: {} * rota: {} )'.format(total, dim,pesoO,rotaO))

