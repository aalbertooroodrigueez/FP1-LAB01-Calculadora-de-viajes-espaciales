edad = int(input("Qué edad tienes: "))
nivel_fisico = int(input("Dígame tu nivel físico del 1 al 10: "))

while not (1<=nivel_fisico<=10):
    print("El valor no es válido.")
    nivel_fisico = int(input("Di tu nivel físico del 1 al 10: "))

if edad < 18:
    print("Debes ser mayor de edad.")
elif nivel_fisico < 5:
    print("Debes estar en mejor forma.")
else:
    print("¡Listo para despegar!")