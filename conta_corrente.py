menu = '''

      [d] Depositar
      [s] Sacar
      [e] Extrato
      [x] Sair

    ==> '''

saldo = 0
limite = 500
extrato = ''
saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == 'd':
        valor = float(input('Qual valor deseja depositar? R$ '))
        if valor > 0 :
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else :
            print('Valor inválido')
    elif opcao.upper() == 'S':

        excedeu_saques = saques >= LIMITE_SAQUES
        if excedeu_saques :
            print(f'Número máximo de saques excedido (limite de {LIMITE_SAQUES} saques diário)')
        else: 
            valor = float(input('Qual valor deseja sacar? R$ '))
            excedeu_saldo = valor > saldo
            excedou_limite = valor > limite

            if valor > 0 :
                if excedeu_saldo :
                    print('Você não tem saldo suficiente')
                elif excedou_limite :
                    print(f'O valor do saque excedeu o limite de  R$ {valor:.2f}')
                else:
                    saldo -= valor
                    extrato += f'Saque: R$ -{valor:.2f}\n'
                    saques += 1
            else:
                print('Valor inválido')
    elif opcao.upper() == 'E':
        print('\n############## EXTRATO ##############')
        print('Não foram realizadoas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('#####################################')
    elif opcao.upper() == 'X':
        break
    else :
        print('Opção inválida')
