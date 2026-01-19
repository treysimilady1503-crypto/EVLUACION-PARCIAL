# EJERCICIO 1
# Evaluación de estudiantes usando for, condiciones y contadores

estudiantes = [
    {"nombre": "Ana", "nota": 15, "asistencia": 80, "activo": True},
    {"nombre": "Luis", "nota": 11, "asistencia": 75, "activo": True},
    {"nombre": "Marta", "nota": 16, "asistencia": 60, "activo": True},
    {"nombre": "Pepe", "nota": 18, "asistencia": 90, "activo": False},
]

aprobados = 0
desaprobados = 0

print("=== EVALUACIÓN DE ESTUDIANTES ===\n")

for estudiante in estudiantes:
    print("Estudiante:", estudiante["nombre"])

    if not estudiante["activo"]:
        print("Resultado: No evaluado (inactivo)\n")
        continue

    if estudiante["nota"] >= 14 and estudiante["asistencia"] >= 70:
        print("Resultado: APROBADO\n")
        aprobados += 1
    else:
        print("Resultado: DESAPROBADO\n")
        desaprobados += 1

print("=== RESUMEN FINAL ===")
print("Aprobados:", aprobados)
print("Desaprobados:", desaprobados)
