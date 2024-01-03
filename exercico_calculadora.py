from os import system


while True:
    try:
        primeiro_numero = float(input("Digite o primeiro numero: "))
        segundo_numero = float(input("Digite o segundo numero: "))
        
    except:
        print("voce não digitou numero, digite um numero e tente novamente...")
        continue
    operador = input("digite o operador '+,*,-,/': ")

    validade = None
    try:
        if operador == "+":
            validade = True
        elif operador == "-":
            validade = True
        elif operador == "/":
            validade = True
        elif operador == "*":
            validade = True
        else:
            print("Operador invalido, digite outro e tente novamente...")
            validade = False
    except:
        print("operador invalido")
        validade = False
        continue
    if validade:
        if operador == "+":
            resultado = primeiro_numero + segundo_numero
        elif operador =="-":
            resultado = primeiro_numero - segundo_numero
        elif operador == "/":
            resultado = primeiro_numero / segundo_numero
        elif operador == "*":
            resultado = primeiro_numero * segundo_numero
        print(f"{resultado=}")
        sair = input("Digite sair para sair:").lower().startswith("s")
        system("cls")
        if sair:
            print("saindo...")
            break
        else:
            continue