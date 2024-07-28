import random
import pygame, sys

class Tragamonedas():
    def __init__(self, creditos, bonus):
        self.creditos = creditos
        self.bonus = bonus
        self.opciones = {'naranja':10,'campana':15,'bar':50, 'bar/bar':100, 
                         'manzana':5, '77':40, 'cereza':2, 'melon':20,
                         'sandia': 25, 'cereza':2, 'manzana': 5, 'cereza':2,
                         'naranja':10, 'campana':15, 'cereza':2, '77':40, 
                         'manzana':5, 'cereza':2, 'melon':20, 'estrellas':30,
                         'cereza':2, 'manzana':5, 'cereza':2}

    def insertar_creditos(self):
        self.creditos += 1
    def bonus(self):
        self.bonus += 1
    def aleatorio(self):
       clave_aleatoria = random.choice(list(self.opciones.keys()))
       valor = self.opciones[clave_aleatoria]
       return valor

pygame.init()
size = (1500, 1000)
blanco = 255, 255, 255
cafe = 128, 64, 0
rojo = (255, 0, 0)
fuente = pygame.font.Font(None, 74) 
def mostrar_texto(ventana, texto, color, posicion):
    superficie_texto = fuente.render(texto, True, color)
    ventana.blit(superficie_texto, posicion)

ventana = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ventana.fill(blanco)

    for x in range (100, 700, 100):
        pygame.draw.rect(ventana, cafe, (x, 10, 90, 90))
        for y in range (10, 700, 100):
            pygame.draw.rect(ventana, cafe, (100, y, 90, 90))

    for x in range (200, 600, 100):
        pygame.draw.rect(ventana, cafe, (x, 610, 90, 90))
        for y in range (10, 700, 100):
            pygame.draw.rect(ventana, cafe, (600, y, 90, 90)) 

    pygame.draw.rect(ventana, rojo, (100, 10, 90, 90), 5)

    mostrar_texto(ventana, 'BONUS', rojo, (100, 100))

    pygame.display.flip()