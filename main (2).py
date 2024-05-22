import pessoa as p
import estatistica as stat

saiu = True
pessoas = [] 
print("Bem vindo ao portal da Prefeitura de Campinas")
while saiu:
  try:
    idade = int(input("digite sua idade: "))
    if idade< 0:
      saiu = False
      break
    sexo = input("Qual seu sexo?(M/masculino ou F/Feminino): ")
    if sexo != "M" and sexo != "F":
      print("Apenas Masculino e Feminino")
    else:
      salario = int(input("Quanto ganhas?: "))
      filhos = int(input("Quantos filhos possui?: "))
      pessoas.append(p.criaPessoa(idade, sexo,salario,filhos))
  except ValueError:
    print("Insira os valores validos")
print("Total entrevistados: " + str(len(pessoas)))
print("Média saláral das mulheres:" + str(stat.mediaSalario(pessoas)))
print("Maior salário masculino: " + str(stat.maiorSalario(pessoas)))
stat.SalarioMinimo(pessoas)
print("Total pessoas com mais de dois filhos: " + str(stat.maisDoisFilhos(pessoas)))
