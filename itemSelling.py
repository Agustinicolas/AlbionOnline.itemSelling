# author: Agustin Hernandez / IGN: Barrilete / Discord: Barrilete#9691

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
incorrectValue = ["Valor incorrecto.", "Incorrect value."]
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
while reparacion < 0:
    print(incorrectValue[opt])
    reparacion = int(input(repairText[opt]))

file.write(f"repair cost / costo de reparación: {reparacion}\n\n")  # repairing cost is addede to the file selling.txt

tax = float(input(taxText[opt]))
while not(0 < tax < 100):
    print(incorrectValue[opt])
    tax = float(input(taxText[opt]))

file.write(f"tax/impuesto: {tax}%\n\n")

cant = int(input(cantText[opt]))
while cant < 1:
    print(incorrectValue[opt])
    cant = int(input(cantText[opt]))

file.write(f"Players / Jugadores: {cant} \n\n")

sumatoria = 0
continuar = True
while continuar:

    item = input(priceInputText[opt])
    if not(item.isnumeric()):
        item = 0
        print(invalidInputText[opt])
    elif item == "0":
        continuar = False
    else:
        item = int(100 * int(item) / (100 - tax))
        file.write("{}\n".format(str(item)))
        sumatoria = sumatoria + item

total = int(sumatoria * (100 - tax)/100) - reparacion
ganancia = int(total / cant)


print(sellingValueDisplay[opt] + str(sumatoria))
file.write(f"\nVALOR TOTAL DE VENTA / SELLING VALUE: {sumatoria}  \n")

print(totalEarningsDisplay[opt] + str(total))
file.write(f"GANANCIA TOTAL / TOTAL PROFIT: {total}  \n")

print(individualEarningsDisplay[opt] + str(ganancia) + "\n\n")
file.write(f"GANANCIA INDIVIDUAL / INDIVIDUAL PROFIT ({cant} PARTICIPANTES/PLAYERS)  {ganancia} \n \n")

file.close()  # Closes venta.txt

print(thanksText[opt] + "Barrilete#9691\n\n")
input(endText[opt])
