# Mensagem de introdução

print('Olá! bem vindo a cálculadora de física! :D ')
print('Selecione uma das opções abaixo para calcular:')
print('Velocidade Média) - Digite Vm')
print('Aceleração Média) - Digite Am')
print('Aceleração Centrípeta - Digite Ac')
print('Aceleração Angular Média - Digite Aam')

opcao = 0

# Verificando se a opção escolhida pelo usuário não é inválida
while opcao not in ['vm', 'am', 'ac', 'aam']:
        opcao = input('Selecione qual operação você deseja realizar:  ').lower()
        if opcao not in ['vm', 'am', 'ac', 'aam']:
            print('Opção inválida, selecione novamente!')

else: # Execute a operação escolhida pelo usuário
    
    # -> Calculo da Velocidade média   
    if opcao == 'vm':
        movimento = float(input('Digite o ΔS (em metros):  '))
        tempo = float(input('Digite o ΔT (em segundos):  '))
        calculoVm = movimento / tempo
        print(f'Sua velocidade média é de: {calculoVm :.2f} m/s')

    # -> Calculo da Aceleração Média    
    elif opcao == 'am':
        movimento = float(input('Digite o ΔS (em metros):  '))
        tempo = float(input('Digite o ΔT (em segundos):  '))
        calculoAm = movimento / tempo 
        print(f'Sua aceleração média é de: {calculoAm :.2f} m/s²')

    # -> Calculo da Aceleração Centrípeta
    elif opcao == 'ac':
        velocidade = float(input('Digite sua velocidade (em metros por segundo):  '))
        raio = float(input('Digite o raio da circuferência (em metros):  '))
        calculoAc = (velocidade ** 2) / raio 
        print(f'Sua aceleração centrípeta é de {calculoAc :.2f} m/s²')

    # -> Calculo da Aceleração Angular Média
    elif opcao == 'aam':
        velAngular = float(input('Digite sua velocidade angular(em rad/s):  '))
        tempo = float(input('Digite o ΔT (em segundos)'))
        calculoAam = velAngular / tempo
        print(f'Sua aceleração angular média é de {calculoAam :.2f} rad/s²')