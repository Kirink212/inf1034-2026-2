def calcula_imc(peso, altura):
  return peso/altura**2

altura = input("Digite a sua altura:")
peso = input("Digite o seu peso:")

imc = calcula_imc(peso, altura)
print(f"O seu IMC é {imc}")

if imc > 30:
  print("Você está com obesidade. VAI PRO MÉDICO! POR FAVOR!!")

if imc < 17:
  print("Você está parecendo a Ariana Grande... VAI PRO COMER ALGUUMA COISA!")

