def mediaSalario(dados):
    total, itens = 0, 0
    for item in dados:
        valor = item.get('salario', 0)
        sexo = item.get('sexo')
        if valor and sexo == "F":
            itens += 1
            total += valor
    return (total / itens) if itens else 0

def maisDoisFilhos(dados):
    total = 0
    for item in dados:
      filhos = item.get('filhos')
      if filhos > 2:
        total += 1
    return total 

def SalarioMinimo(dados):
  minimo = 1200
  menorQMinimo = 0
  ateTres = 0
  ateCinco = 0
  maisCinco = 0
  for item in dados:
    salario = item.get('salario')
    if salario < minimo:
      menorQMinimo += 1
    elif salario > minimo and salario < (minimo*3):
      ateTres += 1
    elif salario > (minimo*3) and salario < (minimo*5):
       ateCinco += 1
    else:
      maisCinco += 1
  percentualMenor = (menorQMinimo / len(dados))*100
  percentualTres = (ateTres / len(dados))*100
  percentualCinco = (ateCinco / len(dados))*100
  percentualMais = (maisCinco / len(dados))*100
  print("Percentual de pessoas que recebem até um salario minimo" + str(round(percentualMenor, 2)) + "%")
  print("Percentual de pessoas que recebem entre um e tres salarios minimos" + str(round(percentualTres, 2)) + "%")
  print("Percentual de pessoas que recebem entre tres e cinco salarios minimos" + str(round(percentualCinco, 2)) + "%")
  print("Percentual de pessoas que recebem acima de cinco salario minimo" + str(round(percentualMais, 2)) + "%")
  
  
   
    
def maiorSalario(dados):
    maior = 0
    for item in dados:
      sexo = item.get('sexo')
      salario = item.get('salario')
      if salario > maior and sexo == "M":
        maior = salario
    return salario  