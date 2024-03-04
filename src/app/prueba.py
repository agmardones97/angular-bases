# instrucciones = "UNDDNNUUNNUNUUUUUNNUNUUUUNNUUNUUUUUNNUUNNSDDNNUUNNUNDNNSUNUUUNNUNUUUUNNUNNUUNUUUNNDDDNNUUUUUUNNDDDNNUUNUUUUUUNNUNNUNDNNUUUUUUNNS"
# instrucciones = "UNDDNNUUNNNUNUUUUUNNUNUUUUNNUUNUUUUUNNUUNNNSDDNNUUNNNUNDNNSUNUUUNNUNUUUUNNUNNNUUNUUUNNDDDNNUUUUUUNNDDDNNUUNUUUUUUNNUNNNUNDNNUUUUUUNNS"
# instrucciones = "DDNNNUNUUUUUNNUNUUNNUS"
# instrucciones = "UNDDNS"
instrucciones = "UNDDNNUUNNNUNUUUUUNNUNUUUUNNUUNUUUUUNNUUNNNSDDNNUUNNNUNDNNSUNUUUNNUNUUUUNNUNNNUUNUUUNNDDDNNUUUUUUNNDDDNNUUNUUUUUUNNUNNNUNDNNUUUUUUNS"

puntero = 0
cadena = ""
frases = []

for i, instruccion in enumerate(instrucciones):
  if (instruccion == "U"):
    puntero += 1
  if (instruccion == "D"):
    puntero -= 1
  if (instruccion == "N"):
    cadena += str(puntero % 10)
    puntero = 0
  if (instruccion == "S"):
    cadena += str(puntero % 10)
    puntero = 0
    frases.append(cadena)
    cadena = ""


palabra = ""

final = ""
for k in frases:
  for j in k.split("0"):
    if (len(j)!= 0):
      palabra += chr(int(j) + ord("A") - 1 )
  final += " "+palabra
  palabra = ""



print(final)


