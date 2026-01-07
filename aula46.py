for i in range(10):
    if i == 2:
        print()
        print('i é 2, pulando...')
        print()
        continue

    if i == 6:
        print('i é 6, seu else não executará')
        print()
        break

    for j in range(1, 3):
        print(i, j)
    print()
else:
    print('For completo com sucesso!')
    print()
