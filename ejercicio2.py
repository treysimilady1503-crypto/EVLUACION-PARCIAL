# EJERCICIO 2
# Registro de ventas con datos ya definidos

ventas = [300, -50, 700, 200, 0]  # Datos ingresados
total_ventas = 0
bono = False

print("REGISTRO DE VENTAS\n")

i = 0
while i < len(ventas):
    venta = ventas[i]

    if venta == 0:
        break

    if venta < 0:
        print("Monto inválido:", venta)
        i += 1
        continue

    print("Venta registrada:", venta)
    total_ventas += 1

    if venta > 500:
        bono = True

    i += 1

print("\nRESUMEN FINAL")
print("Total de ventas válidas:", total_ventas)

if bono:
    print("El vendedor obtuvo bono")
else:
    print("El vendedor no obtuvo bono")