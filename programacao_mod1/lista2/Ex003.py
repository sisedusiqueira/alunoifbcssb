'''
 3. Analise o programa abaixo e, para cada uma das saídas (comandos
 print), detalhe passo a passo como o Python (segundo suas
 prioridades) resolveria as equações e o resultado final obtido. x = 2 y
 = 3 z = 0.5 print(x + x * x ** (y * x) / z) print(not x + z < y or x + x *
 z >= y and True)
'''
# variaveis x=2 y=3 z=0.5

# (x + x * x ** (y * x)/z)
print(2+2*2**(3*2)/0.5)
# print(2+2*2**6/0.5)
# print(2+2*64/0.5)
# print(2+128/0.5)
# print(2+256.0)
print(258.0)

# print(not x + z <y or x + x * z>= y and True)
# print(not 2 + 0.5 < 3 or 2 + 2 * 0.5 >= 3 and True)
# print(not 2 + 0.5 < 3 or 2 + 1.0 >= 3 and True)
# print(not 2.5 < 3 or 3.0 >= 3 and True)
# print(not 2.5 < 3 or 3.0 >= 3 and True)
# print(not V or (V and True)
# print(F or V and V)
print('F')