inicio=2
fim=100
print('mostrando números primos;')
for x in range(inicio, fim+1):
  if x>1:
   for z in range(2, x):
    if x%z==0:
     break
   else:
    print(x)
else:
  print(100)
  print('fim do programa.')