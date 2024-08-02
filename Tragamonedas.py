import random

class Tragamonedas():
    def __init__(self, creditos, bonus):
        self.creditos = creditos
        self.bonus = bonus
        self.opciones = [
            {'naranja': 10},
            {'campana': 15},
            {'bar': 50},
            {'bar/bar': 100},
            {'manzana': 5},
            {'77': 40},
            {'cereza': 2},
            {'melon': 20},
            {'sandia': 25},
            {'cereza': 2},
            {'manzana': 5},
            {'cereza': 2},
            {'naranja': 10},
            {'campana': 15},
            {'cereza': 2},
            {'77': 40},
            {'manzana': 5},
            {'cereza': 2},
            {'melon': 20},
            {'estrellas': 30},
            {'cereza': 2},
            {'manzana': 5},
            {'cereza': 2}
        ]

    def insertar_monedas(self):
        while True:
            monedas = int(input("Ingrese el numero de monedas: "))
            if 0 < monedas <= 999:
                self.creditos += monedas
                print(f"Ingresastes {monedas} monedas lo cual se cambia a {self.creditos} creditos")
                break
            else:
                print("El numero maximo de monedas que se puede es de 999")

    def bonus(self):
        self.bonus += 1

    def tablero(self):
        print("***TABLERO***\n")
        print("a) Bar/Bar")
        print("b) Bar")
        print("c) 77")
        print("d) Estrellas")
        print("e) Sandia")
        print("f) Melon")
        print("g) Campana")
        print("h) Naranja")
        print("i) Manzana")
        print("j) Cereza")
    
    def mostrar_opciones(self):
        print("1. TABLERO")
        print("2. INSERTAR MONEDAS")
        print("3. APUESTA")
        print("0. SALIR")
    
    def apuesta(self):
        nu_apuestas = int(input("Cuantas apuestas desea realizar: "))
        while nu_apuestas:
            if self.creditos > 0:
                creditos_apostar = int(input("Cuantos creditso desea apostar: "))
                self.creditos -= creditos_apostar
            elif self.creditos <= 0:
                print("No tiene saldo para hacer la apuesta, ¿desea insertar? (Si/No)")
                insertar = input().lower()
                if insertar == 'si':
                    tragamonedas.insertar_monedas()
                else:
                    print("Opcion incorrecta")
            else: 
                girar = random.choice(self.opciones)
                print(girar)
                break

tragamonedas = Tragamonedas(creditos=0, bonus=0)
while True:
    print("OPCIONES")
    print(tragamonedas.mostrar_opciones())
    opc = int(input("Ingrese una opcion: "))
    if opc == 1:
        print(tragamonedas.tablero())
    elif opc == 2:
        print(tragamonedas.insertar_monedas())
    elif opc == 3:
        print(tragamonedas.apuesta())
    elif opc == 0:
        break