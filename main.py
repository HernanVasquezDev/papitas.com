import time
print("Hello, Bienvenido a papitas.com")

print("\n" "="*2 + "\n")
print("1. Papitas de Pollo")
print("2. Papitas de Tomate")
print("3. Papitas Naturales")
print("4. Papitas de Limon")
print("5. Papitas de Queso")

print("\n" "="*2 + "\n")

opcion = input("\nIngrese el numero de sus papitas: ")

if opcion == "1":
    papitas = "Papitas de Pollo"
elif opcion == "2":
    papitas = "Papitas de Tomate"
elif opcion == "3":
    papitas = "Papitas Naturales"
elif opcion == "4":
    papitas = "Papitas de Limon"
elif opcion == "5":
    papitas = "Papitas de Queso"
else:
    print("Lo sentimos, de esas no tenemos :c")
    papitas = None

if papitas:
    print(f"\n Preparando sus {papitas}... ")
    time.sleep(2)
    print("\n Frintando Papitas")
    time.sleep(2)
    print(f"\n Agregando Sabor de sus {papitas} ")
    time.sleep(2)

print("\n Sus papitas estan listas, si quieres añadir salsa a tus {papitas}")
print("\n tenemos las siguiente opciones: ")

print(f"\n Adicionalmente puedes elegir uno los siguientes toppings para potenciar tus {papitas}")
print("\n Toppings: ")

print(f"\n ¡Listo!, Sus {papitas} estan listas, Buen provecho :3...")
