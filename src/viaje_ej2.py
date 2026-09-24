distancia_km = int(input("Dígame la distancia: "))
velocidad_kmh = int(input("Dígame la velocidad: "))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
semanas = tiempo_dias // 7
dias_restantes = tiempo_dias - (semanas * 7)

print(f"Tardarías {semanas} semanas y {dias_restantes} días en llegar.")
