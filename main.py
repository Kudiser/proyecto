Traductor = {
            "JUICIOSO": "Algo excepcionalmente raro o embarazoso",
            "CANGUIL": "maiz pira o palomitas de maiz",
            "AGUACATE": "Es una fruta tambien conocida como palta",
            
            }

palabra = input("Ingresa una palabra en mayuscula, que quieras traducir: ")

if palabra in Traductor.keys():
    print("Su significado es: ",Traductor[palabra])
else:
    print("la palabra no existe")
