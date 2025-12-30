aa = 'AAAAA'
bb = 'BBBBBB'
cc = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=aa, nome2=bb, nome3=cc
)

print(formato)
