#Calculadora simples para saber se é melhor abastecer com álcool ou gasolina o carro
print("Qual combustível compensa mais usar na hora de abastecer o carro")

gasolina = float(input("Digite o valor da gasolina em reais: \n"))
alcool = float(input("Digite o valor do álcool em reais: \n"))

comparativo = alcool / gasolina

if (comparativo < 0.7):
    print("É melhor abastecer com álcool")

else:
    print("É melhor abaster com gasolina")
