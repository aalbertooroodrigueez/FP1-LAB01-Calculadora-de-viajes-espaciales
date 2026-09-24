distancia_km = 225000000

for x in range(10000, 50000, 10000):
    velocidad_kmh = x
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    semanas = tiempo_dias // 7
    dias_restantes = tiempo_dias - (semanas * 7)
    
    print(f"Velocidad: {velocidad_kmh} -> Tiempo: {tiempo_horas} horas ({semanas} semanas y {dias_restantes} días)")