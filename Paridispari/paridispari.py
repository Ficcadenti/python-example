def paridispari():
    inp = input("Digita il numero: ")
    numero = int(inp)
    modulo = numero % 2
    if modulo == 0:
        print("Il numero è pari")
    else:
        print("Il numero è dispari")

paridispari()