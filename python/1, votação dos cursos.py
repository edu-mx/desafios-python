cursos = [
  'Engenharia de Software',
  'Python para Data Science',
  'Introdução a Java'
]
respostas = [1, 2, 0, 1, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1,
  1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2,
  2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1
]
#
print('Exibindo resultado da votação.')
item=(0, 1, 2)
engenharia = respostas.count(item[0])
python = respostas.count(item[1])
java = respostas.count(item[2])
engenharia_porcento = 100/len(respostas)*(engenharia)
python_porcento = 100/len(respostas)*(python)
java_porcento = 100/len(respostas)*(java)
#
print('Ao todo, '+str(len(respostas))+' pessoas votaram.')
print(str(engenharia)+' pessoas votaram em engenharia de software, que corresponde a '+str(engenharia_porcento)+'% dos votos.')
print(str(python)+' pessoas votaram em python, que corresponde a '+str(python_porcento)+'% dos votos.')
print(str(java)+' pessoas votaram em java, que corresponde a '+str(java_porcento)+'% dos votos.')
#
curso_porcento=(engenharia_porcento, python_porcento, java_porcento)
contador=0
curso_escolhido=0.0
for x in curso_porcento:
  if x >curso_escolhido:
    curso_escolhido+=x
    contador+=1
else:
  print('O curso escolhido foi ('+str(cursos[contador-1])+') com '+str(curso_porcento[contador-1])+' dos votos.')
