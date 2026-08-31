print("exercicio 1")
idade = int(input(" Escreva sua idade: "))
if(idade >=18 ):
    print (" você é maior de idade")
else:
    print(" você e menor de idade")
    
print("exercicio 2 ")

numero = int(input(" Digite um numero: "))
if (numero %2  == 0 ):
    print (" O numero e par ")
elif (numero %2 == 1):
    print("numero e impar")
else:
    print("numero nao axeito")

print(" Exercicio 3")
numero = int(input(" Digite um numero: "))
if (numero >= 0):
    print(" O numero e positivo ")
else:   
    print("o numero e negativo")

print("exercicio 4")
numero1 = int(input(" Digite o numero A: "))
numero2 = int(input(" Digite o numero B: "))

if(numero1 > numero2 ):
    print(" O numero A e maior que B ")
elif(numero1 == numero2):
    print(" Ambos são iguais")
else:     print(" O numero A e menor que B")

print("exercicio 5")

nota = int(input(" Digite sua nota: "))
if(nota>=7):
    print("Aprovado ")

else:
    print("Reprovado ")

print("exercicio 6")

nascimento = int(input(" Digite sua data de nascimento: "))
idade = 2026-nascimento
if(idade >= 16):
    print(" Pode votar ")
else:
    print(" Nao pode votar")

print(" Exercicio 7")
quantidade = int(input("Digite a quantidade da compra: "))
produto = int (10)
produtoDesc = int(8)
if(quantidade >= 10):   
    valorD = quantidade*produtoDesc
    print("Valor á pagar",valorD) 
else:
    valor = quantidade*produto
    print(" Valor a pagar ",valor) 

print(" Exercicio 8")

nota = int(input(" Digite sua nota: "))

if(nota >= 9 and nota <= 10):
    print("Sua nota é A")
elif(nota >= 7 and nota < 9):
    print("Sua nota é B")
elif(nota >= 5 and nota < 7):
    print("Sua nota é C")
else:
    print("Sua nota é D")

print(" Exericio 9")

idade = int(input(" Digite sua idade: "))

if(idade >= 0 and idade <=12):
    print("voce é criança")
elif(idade >= 13 and idade <=17):
    print("voce é adolecente")
elif(idade >= 18 and idade <=59):
    print("voce é adulto")
else:
    print("Voce e idoso")

print ("Exercicio 10")

numero1 = int(input(" Digite o numero A: "))
numero2 = int(input(" Digite o numero B: "))
numero3 = int(input(" Digite o numero C: "))

if(numero1 > numero2 and numero1 > numero3):
    print("Numero A é maior")
elif(numero2 > numero1 and numero2 > numero3):
    print("Numero A é maior")
elif(numero3 > numero1 and numero3 > numero2):
    print("Numero A é maior")

print("Exercicio 11")
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Escolha a operação \n 1-Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n"))
if(num3 == 1):
    result=num1+num1
    print("O resultado é: ",result)
elif(num3 == 2):
    result = num1-num2
    print("O resultado é: ",result)
elif(num3 == 3):
    result = num1*num2
    print("O resultado é: ",result)
elif(num3 == 4):
    result = num1/num2
    print("O resultado é: ",result)

print("Exercicio 12")

ano = int(input("Digite o ano: "))
if(ano %4 == 0):
        print("O ano é bissexto")
elif(ano %100 == 0):
        print("O ano não é bissexto")
elif(ano %400 == 0):
        print("O ano  é bissexto")
else:
    print("O ano não é bissexto")

print("Exercicio 13")

lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if(lado1< lado2+lado3 and lado2< lado1+lado3 and lado3< lado2+lado1   ):
    if(lado1 == lado2 == lado3):
        print(" É um Equilatero")
    elif(lado1 == lado2 or lado1 == lado3 or lado3 == lado2):
        print(" É um isóceles")
    elif(lado1 != lado2 or lado1 != lado3 or lado3 != lado2):
        print(" É um escaleno ")
else:
    print(" Não é um triangulo ")       

print("Exercicio 14") 

usuario = input(" Digite o usuario :")
senha = int(input(" Digite a senha: "))

if(usuario != "admin"):
    print(" O usuario esta errado. ")
elif(senha != 12345):
    print(" A senha esta errada. ")
else:
    print(" Bem-vindo. Acesso permitido")

print("Exercicio 15")

peso = int(input(" Digite seu peso:"))
altura = int(input(" Digite sua altura: "))
resultado = peso/altura**2

if(resultado < 18.5):
    print(" Abaixo do peso")
elif(resultado >= 18.5 and resultado <= 24.9):
    print(" Peso normal")
elif(resultado >= 25 and resultado <= 29.9 ):
    print(" Acima do peso")
else:
    print(" Obesidade")

print("Exercicio 16 ")

salario = int(input(" D igite seu salario:"))
if(salario <= 2000):
    calculo = salario*0.15
    salarioMaior = salario+calculo
    print(" Seu salario agora é ",salarioMaior)
elif(salario >= 2001 and salario <= 5000):
    calculo  = salario*0.1
    salarioMaior  = salario+calculo
    print(" Seu salario agora é ",salarioMaior)
else:
    calculo = salario*0.05
    salarioMaior = salario+calculo
    print(" Seu salario agora é ",salarioMaior)
    
print(" Exercicio 17 ")

saque = int(input(" Digite a quantidade: "))

if(saque >= 10 and saque <= 1000):
    if(saque %10 == 0 or saque %20 == 0 or saque %50 == 0 or saque %100 == 0  ):
        print(" Você sacou: ",saque)
    else:
        print("Temos apenas notas de 10,20,50,100")
elif(saque>1000):
    print(" O saque é ate 1000")
else:
    print(" O saque é no minimo 10")

print(" Exercicio 18")

dia = int(input(" Digite o dia: "))
mes = int(input(" Digite o mes: "))
ano = int(input(" Digite o ano: "))

if(mes < 1 and mes > 12):
    print(" Data invalida:")
elif(mes == 2):

    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        if(dia >= 1 and dia  >= 29 ):
            print(" Data válida")
        else : 
            print(" Data invalida")
    else:
        if(dia >= 1 and dia  >= 29 ):
            print(" Data válida")
        else : 
            print(" Data invalida")

elif(mes == 4 and mes == 6 and mes == 9 and mes == 11):
    if(dia >= 1 and dia  <= 30 ):
                print(" Data válida")
    else : 
                print(" Data invalida")
else:
    if(dia >= 1 and dia  <= 31 ):
                    print(" Data válida")
    else : 
                    print(" Data invalida")
                    
print(dia, "/", mes, "/", ano)

print(" Exercicio 19")
horas = int(input(" Digite a quantidade de horas: "))

if(horas<2):
    calculo= 5*horas
    print(" Valor a pagar: ",calculo)
elif(horas >=2 and horas <=4):
    calculo = 9*horas
    print(" Valor a pagar: ",calculo)
    
elif(horas >4 ):
    calculo = 8*horas
    print(" Valor a pagar: ",calculo)
else:
    print(" Numero invalido")

print("Exercicio 20")

salario = int(input(" Digite seu salario: "))
valorCasa = int(input(" Digite o valor da casa: "))
pagarEmAnos = int(input(" Digite em quantos ano ira pagar: "))
pagarMensal = pagarEmAnos*12

if( salario >= 1000 and valorCasa >=0 and pagarEmAnos >= 0 and pagarEmAnos < 35):
    
    if(pagarMensal <= 0.30 * salario):
        print(" Valor a pagar mensal e de ",pagarMensal,"R$ ")
    else:
        print(" A parcela exede 30 porcento do salario ",pagarMensal," R$ mensal")
else:
    print(" Informaçoes invalida \n 1- Salario nao pode ser menor que 1000 \n 2- valor da casa nao pode ser menor que zero \n 3- Os anos nao podem exerder 35  ")