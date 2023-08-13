sair = "sair"

while True:
    numero1 = input ("digite o primeiro número?:")
    numero2 = input ("digite o segundo número?:")
    operador = input ("digite o operador (+-*/)?:")


    numeros_corretos = None
    numero1_float = 0
    numero2_float = 0


    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_corretos = True
    except:
        numeros_corretos = None

    if numeros_corretos is None:
        print ("um ou ambos os números recebidos não são válidos.")
        continue

    operador_aceito = "+-*/"
    if operador not in operador_aceito:
        print ("operador inválido")
        continue

    if len(operador) > 1:
        print ("digite apenas um operador.")
        continue


    print ("realizando o calculo:")
    if operador == "+":
        print(f"{numero1_float} + {numero2_float} =", numero1_float + numero2_float)
    elif operador == "-":
         print(f"{numero1_float} - {numero2_float} =", numero1_float - numero2_float)
    elif operador == "*":
         print(f"{numero1_float} * {numero2_float} =", numero1_float * numero2_float)
    elif operador == "/":
         print(f"{numero1_float} / {numero2_float} =", numero1_float / numero2_float)
    else:
        print("error")

    sair = input ("quer sair?").lower().startswith("s")

    if sair is True:
        break
    