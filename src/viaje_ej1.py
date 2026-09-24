distancia_km = 384400
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
semanas = tiempo_dias // 7
dias_restantes = tiempo_dias - (semanas * 7)

print(f"Tardarías {semanas} semanas y {dias_restantes} días en llegar.")