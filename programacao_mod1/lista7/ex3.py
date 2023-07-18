#função
def verifica_faixa_etaria(idade):
  if media_idade >= 0 and media_idade <= 25:
    return "jovem"
  elif media_idade >= 26 and media_idade <= 59:
    return "adulto"
  else:
    return "idoso"


#programa principal
qnt_alunos = int(input("Digite a quantidade de pessoas na turma: "))
soma_idades = 0
for i in range (qnt_alunos):

  idade = int(input(f"Digite a idade da pessoa {i}: "))
  soma_idades += idade

media_idade = soma_idades / qnt_alunos

classificacao = verifica_faixa_etaria(media_idade)

print(f"A média de idade da turma é {media_idade} anos, a turma é classificada como {classificacao}.")