primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor == segundo_valor:
    print(f'O {primeiro_valor=} é igual ao {segundo_valor=}')
elif primeiro_valor >= segundo_valor:
    print(f'O {primeiro_valor=} é maior ou igual ao {segundo_valor=}')
else:
    print(f'O {primeiro_valor=} é menor ou igual ao {segundo_valor=}')