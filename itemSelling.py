# author: Agustin Hernandez / IGN: Barrilete / Discord: Barrilete#9691

def invalido(cadena):  # if parameter cadena isn't a whole number, returns False
    valor = False
    longitud = len(cadena)
    if longitud == 0:
        valor = True
    else:
        for i in range(longitud):
            if (ord(cadena[i]) < 48) or (ord(cadena[i]) > 57):
                valor = True
    return valor


def seleccionidioma():
    lan = " "
    while not(lan == "es" or lan == "en"):
        print("IDIOMA/LANGUAGE:\n English: type ´en´ \n Español: escriba ´es´")
        lan = input().lower()
    if lan == "es" or lan == "ES":
        option = 0
    else:
        option = 1
    return option


# List of messages, if english is selected the messages will be called by nameMessage[1], for spanish nameMessage[0]

repairText = ["Monto de reparación: ", "Repair cost: "]
taxText = ["Porcentaje de impuesto: ", "Market taxes: "]
cantText = ["Cantidad de jugadores: ", "Amount of players: "]
itemInputText = ["Ingresar precio de item\n", "Type in the item's price\n"]
priceInputText = ["Ingresar precio de item o el valor 0 para finalizar \n", "Type in the item´s price or 0 to finish \n"]
invalidInputText = ["Entrada incorrecta \n", "Invalid input \n"]
sellingValueDisplay = ["\nVALOR TOTAL DE VENTA: ", "\nSELLING VALUE: "]
totalEarningsDisplay = ["\nGANANCIA TOTAL: ", "\nTOTAL PROFIT: "]
individualEarningsDisplay = ["\nGANANCIA INDIVIDUAL: ", "\nINDIVIDUAL PROFIT: "]
endText = ["Fin. Presione enter para salir.\n", "End, press enter to exit.\n"]
thanksText = ["Gracias por utilizar esta herramienta. Si tienes dudas/sugerencias contactame por Discord:", "Thanks for using this tool. If you have any doubts/suggestions pm me on Discord:"]

print("Barrilete's Item selling tool")
file = open("selling.txt", "w")  # The file selling.txt is created where this script is located. If a selling.txt already exists, it will be overwritten.
opt = seleccionidioma()  # language will be selected here by calling the function

reparacion = int(input(repairText[opt]))  # repairing cost is added here
file.write("repair cost / costo de reparación: {}\n\n".format(str(reparacion)))  # repairing cost is addede to the file selling.txt

tax = float(input(taxText[opt]))
file.write("tax/impuesto: {}%\n\n".format(str(tax)))

cant = int(input(cantText[opt]))
file.write("Players / Jugadores: {} \n\n".format(str(cant)))

sumatoria = 0
continuar = True
while continuar:

    item = input(priceInputText[opt])
    if invalido(item):
        item = 0
        print(invalidInputText[opt])
    elif item == 0:
        continuar = False
    else:
        item = int(100 * int(item) / (100 - tax))
        file.write("{}\n".format(str(item)))
        sumatoria = sumatoria + item

total = int(sumatoria * (100 - tax)/100) - reparacion
ganancia = int(total / cant)


print(sellingValueDisplay[opt] + str(sumatoria))
file.write("\nVALOR TOTAL DE VENTA / SELLING VALUE: {}  \n".format(str(sumatoria)))

print(totalEarningsDisplay[opt] + str(total))
file.write("GANANCIA TOTAL / TOTAL PROFIT: {}  \n".format(str(total)))

print(individualEarningsDisplay[opt] + str(ganancia) + "\n\n")
file.write("GANANCIA INDIVIDUAL / INDIVIDUAL PROFIT ({} PARTICIPANTES/PLAYERS)  {} \n \n".format(str(cant), str(ganancia)))

file.close()  # Closes venta.txt

print(thanksText[opt] + "Barrilete#9691\n\n")
input(endText[opt])
