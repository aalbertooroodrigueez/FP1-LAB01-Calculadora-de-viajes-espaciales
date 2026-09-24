distancia_total = int(input("Introduce la distancia total en km: "))
autonomia = 150000
paradas = 0
for km in range(autonomia, distancia_total, autonomia):
    print(f"Parada en el km {km}")
    paradas += 1

print(f"Total de paradas para repostar: {paradas}")