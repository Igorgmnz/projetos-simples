a = int(input("digite o primeiro numero: ") )
operacao = input("digite a operacao: ")
b = int(input("digite o segundo numero: ") )

if operacao == '+':
    resultado = a + b

elif operacao == '-':
    resultado = a - b

elif operacao == '/':
    resultado = a / b

elif operacao == '*':
    resultado = a * b

else :
    resultado = "seleciona uma operacao valida fdp"

print (resultado)