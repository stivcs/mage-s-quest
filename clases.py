import pygame 
import sys
import random
from funciones import *


class Protagonista():
    def __init__(self):
        self.image = movimientos_personajes('imagenes\\personajes\\protagonista1.png',65,94)
        self.x = 0
        self.y = 550 - 94
        self.velocidad_X = 0
        self.vida = 100
        self.ataque = 10
        self.move = 1
        self.dir = 0 #0 hacia la derecha, 1 hacia la izquierda
        self.y_inicial = self.y
        self.saltando = False
        self.velocidad_Y = 0
        self.altura_salto = 23  # Altura máxima del salto
        self.gravedad = 2  # Ajusta la gravedad para el salto
    def draw(self,ventana):
        if self.dir == 0:
            i = 0
        else:
            i = 7
        imagen = self.image[i]
        if self.velocidad_X != 0:
            if self.move == 1:
                if self.dir == 0:
                    i = 1
                else:
                    i = 6
                imagen = self.image[i]
            if self.move == 2:
                if self.dir == 0:
                    i = 2
                else:
                    i = 5
                imagen = self.image[i]
            if self.move == 3:
                if self.dir == 0:
                    i = 3
                else:
                    i = 4
                imagen = self.image[i]
            if self.move == 3:
                self.move = 1
            else:
                self.move += 1
        ventana.blit(imagen,(self.x,self.y))
    def saltar(self):
        if not self.saltando:
            self.saltando = True
            self.y_inicial = self.y  # Guarda la posición inicial en y
            self.velocidad_Y = -self.altura_salto
    def actualizar(self):
        self.x += self.velocidad_X
        if self.saltando:
            self.y += self.velocidad_Y
            self.velocidad_Y += self.gravedad
            # Cuando alcanza el suelo, detiene el salto y restaura la posición inicial en y
            if self.y >= 550 - 94:
                self.saltando = False
                self.y = 550 - 94
                self.velocidad_Y = 0
    def derecha(self):
        self.velocidad_X = 7
        self.dir = 0
    def izquierda(self):
        self.velocidad_X = -7
        self.dir = 1
    def detener(self):
        self.velocidad_X = 0
    def mostrar_vida(self, ventana):
        vida_maxima = 100  # Define la vida máxima visual en la barra
        longitud_barra = 200  # Define la longitud visual máxima de la barra

        # Calcular la vida visual limitada a 100
        vida_visual = min(self.vida, vida_maxima)

        # Calcular el porcentaje de vida visual con respecto a la vida máxima visual
        porcentaje_vida_visual = (vida_visual / vida_maxima)

        # Calcular la longitud visual de la barra según el porcentaje de vida visual
        longitud_actual = int(longitud_barra * porcentaje_vida_visual)

        # Dibujar la barra de vida
        pygame.draw.rect(ventana, (0, 0, 0), (5, 5, longitud_barra + 10, 30))
        pygame.draw.rect(ventana, (255, 0, 0), (10, 10, longitud_barra, 20))  # Barra de vida base
        pygame.draw.rect(ventana, (0, 255, 0), (10, 10, longitud_actual, 20))  # Barra de vida actual

        # Texto con el porcentaje de vida
        font = pygame.font.Font(None, 24)
        texto_vida = font.render(f'{vida_visual}%', True, (255, 255, 255))
        ventana.blit(texto_vida, (longitud_barra * 0.5, 12.5))
    def dire(self):
        if self.dir == 0:
            return 1
        else:
            return -1
    def impacto(self,obj):

        bool = False
        if self.x < obj.x < self.x + 65:
            if self.y < obj.y < self.y + 94:
                bool = True
        if self.x < obj.x + obj.width < self.x + 65:
            if self.y < obj.y < self.y + 94:
                bool = True
        if self.x < obj.x < self.x + 65:
            if self.y < obj.y + obj.heigth < self.y + 94:
                bool = True
        if self.x < obj.x + obj.width < self.x + 65:
            if self.y < obj.y + obj.heigth < self.y + 94:
                bool = True
        if bool:
            if obj.state == "alive" or obj.state == "fire": 
                self.vida -= obj.damage
                obj.reset()
        return bool
    def reset(self):
        self.x = 0
        self.y = 550 - 94
        self.velocidad_X = 0
        self.ataque = 10
        self.move = 1
        self.dir = 0

class BolaFuego:
    def __init__(self,x=0,y=1000):
        pygame.mixer.init()
        self.x = x
        self.y = y
        self.dir = 1
        self.vel = 13
        self.bulletImg = pygame.image.load(f"imagenes\\ataques\\fireball.png")
        self.width = self.bulletImg.get_size()[0]
        self.heigth = self.bulletImg.get_size()[1]
        self.state = "ready"
        self.damage = 10
        self.sonido = pygame.mixer.Sound('sonidos\\04_Fire_explosion_04_medium.wav')
    def draw(self,ventana):
        if self.dir == -1:
            image = pygame.transform.flip(self.bulletImg, True,False)
        else:
            image = self.bulletImg
        ventana.blit(image,(self.x,self.y))
    def fire(self,x,y,n):
        if self.state == "fire":
            return
        self.state = "fire"
        self.sonido.play()
        xe = 65 * n
        self.x = x + xe
        self.y = y + 20
        self.vel *= n
        self.dir = n
    def move(self):
        if self.state == "fire":
            self.x += self.vel
        if self.x > 800 or self.x < 0:
            self.reset()
    def reset(self):
        self.x = 0
        self.y = 1000
        self.vel = 13
        self.state = "ready"

class BolaTierra(BolaFuego):
    def __init__(self,x=0,y=1000):
        super().__init__(x,y)
        self.sonido = pygame.mixer.Sound("sonidos\\30_Earth_02.wav")
        self.bulletImg = pygame.image.load(f"imagenes\\ataques\\stoneball.png")
        self.damage = 8

class IceAttack(BolaFuego):
    def __init__(self,x=0,y=1000):
        super().__init__(x,y)
        self.sonido = pygame.mixer.Sound("sonidos\\13_Ice_explosion_01.wav")
        self.bulletImg = pygame.image.load(f"imagenes\\ataques\\iceAttack.png")
        self.damage = 15
    def draw(self,ventana):
        if self.dir == 1:
            image = pygame.transform.flip(self.bulletImg, True,False)
        else:
            image = self.bulletImg
        ventana.blit(image,(self.x,self.y))

class VerticalAttack(IceAttack):
    def __init__(self,x=0,y=1000):
        super().__init__(x,y)
        self.sonido = pygame.mixer.Sound("sonidos\\13_Ice_explosion_01.wav")
        #rota la imagen 90 grados
        self.bulletImg = pygame.transform.rotate(self.bulletImg,90)
        self.damage = 10
    def draw(self,ventana):
        if self.dir == 1:
            image = pygame.transform.flip(self.bulletImg, True,False)
        else:
            image = self.bulletImg
        ventana.blit(image,(self.x,self.y))
    def fire(self,x,y):
        if self.state == "fire":
            return
        self.state = "fire"
        self.sonido.play()
        self.x = x + 20
        self.y = y
    def move(self):
        if self.state == "fire":
            self.y += self.vel
        if self.y > 800 or self.y < 0:
            self.reset()
    
class Villano:
    def __init__(self):
        self.width = 117
        self.heigth = 80
        self.image = movimientos_personajes('imagenes\\personajes\\villano1.png', 117, 80)
        self.image = rotar_imagen(self.image)
        self.x = 650
        self.y = 550 - 80
        self.velocidad_X = -3  # Velocidad inicial de movimiento lateral
        self.velocidad_Y = 0  # Velocidad inicial de movimiento vertical
        self.max_altura = self.y - 200  # Altura máxima permitida para el vuelo
        self.max_lateral = self.x - 250  # Límite de movimiento lateral izquierdo
        self.min_lateral = self.x  # Límite de movimiento lateral derecho
        self.vida = 100
        self.damage = 10
        self.move = 1
        self.dir = 1  # 0 hacia la derecha, 1 hacia la izquierda
        self.y_inicial = self.y
        self.saltando = False
        self.altura_salto = 23  # Altura máxima del salto
        self.gravedad = 2  # Ajusta la gravedad para el salto
        self.tiempo_ultimo_salto = 0
        self.tiempo_ultimo_ataque = 0
        self.state = "alive"

    def draw(self, ventana):
        if self.state == "alive":
            imagen = self.image[0]
        elif self.state == "dead":    
            imagen = self.image[4]
        ventana.blit(imagen, (self.x, self.y))

    def saltar(self):
        if not self.saltando:
            self.saltando = True
            self.y_inicial = self.y  # Guarda la posición inicial en y
            self.velocidad_Y = -self.altura_salto

    def atacar(self, bola_tierra,bola2 = 0):
        if self.state == "alive":
            tiempo_actual = pygame.time.get_ticks()

            # Atacar cada dos segundos (2000 milisegundos)
            if tiempo_actual - self.tiempo_ultimo_ataque >= 1000:
                # Generar posición aleatoria en el rango especificado
                pos_y_aleatoria = random.randint(300, 500)
                pos_y_aleatoria2 = random.randint(300, 500)

                # Atacar en la posición X actual del villano y la posición Y generada aleatoriamente
                if self.dir == 1:
                    i = -1
                elif self.dir == 0:
                    i = 1
                if bola2 != 0:
                    bola2.fire(self.x, pos_y_aleatoria2, i)
                bola_tierra.fire(self.x, pos_y_aleatoria, i)

                self.tiempo_ultimo_ataque = tiempo_actual

    def actualizar(self):
        if self.state == "alive":
            # Movimiento lateral
            self.x += self.velocidad_X

            # Movimiento vertical
            if self.saltando:
                self.y += self.velocidad_Y
                self.velocidad_Y += self.gravedad

                # Cuando alcanza el suelo, detiene el salto y restaura la posición inicial en y
                if self.y >= 550 - 80:
                    self.saltando = False
                    self.y = 550 - 80
                    self.velocidad_Y = 0
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_salto >= 4000:  # 4000 milisegundos = 4 segundos
                self.saltar()
                self.tiempo_ultimo_salto = tiempo_actual
            # Control de límites
            if self.y <= self.max_altura:
                self.velocidad_Y = -self.velocidad_Y  # Cambia la dirección vertical si alcanza la altura máxima
            if self.x <= self.max_lateral or self.x >= self.min_lateral:
                self.velocidad_X = -self.velocidad_X  # Cambia la dirección lateral si alcanza los límites laterales
    def impacto(self,obj):
        if obj != None and self.state=="alive" :
            bool = False
            if self.x < obj.x < self.x + 65:
                if self.y < obj.y < self.y + 94:
                    bool = True
            if self.x < obj.x + obj.width < self.x + 65:
                if self.y < obj.y < self.y + 94:
                    bool = True
            if self.x < obj.x < self.x + 65:
                if self.y < obj.y + obj.heigth < self.y + 94:
                    bool = True
            if self.x < obj.x + obj.width < self.x + 65:
                if self.y < obj.y + obj.heigth < self.y + 94:
                    bool = True
            if bool:
                self.vida -= obj.damage
                obj.reset()
        if self.vida <= 0:
            self.state = "dead"
    def mostrar_vida(self, ventana):
        vida_maxima = 100  # Define la vida máxima visual en la barra
        longitud_barra = 200  # Define la longitud visual máxima de la barra

        # Calcular la vida visual limitada a 100
        vida_visual = min(self.vida, vida_maxima)

        # Calcular el porcentaje de vida visual con respecto a la vida máxima visual
        porcentaje_vida_visual = (vida_visual / vida_maxima)

        # Calcular la longitud visual de la barra según el porcentaje de vida visual
        longitud_actual = int(longitud_barra * porcentaje_vida_visual)

        # Dibujar la barra de vida
        pygame.draw.rect(ventana, (0, 0, 0), (800-longitud_barra-15, 5, longitud_barra +10, 30)) 
        pygame.draw.rect(ventana, (255, 0, 0), (800-longitud_barra-10, 10, longitud_barra, 20))  # Dibuja la barra de vida base
        pygame.draw.rect(ventana, (128, 0, 128), (800-longitud_barra-10, 10, longitud_actual, 20))  # Dibuja la barra de vida actual

        # Texto con el porcentaje de vida
        font = pygame.font.Font(None, 24)
        texto_vida = font.render(f'{vida_visual}%', True, (255, 255, 255))
        ventana.blit(texto_vida, (800-longitud_barra * 0.5, 12.5))
    def reset(self):
        self.x = 650
        self.y = 550 - 80
        self.velocidad_X = -3
        self.damage = 10
        self.move = 1
        self.dir = 1
    
class villanoHielo(Villano):
    def __init__(self):
        super().__init__()
        self.width = 77
        self.heigth = 89
        self.image = movimientos_personajes('imagenes\\personajes\\magoHielo.png', 77, 89)
        self.image = rotar_imagen(self.image)
        self.vida = 150
        self.damage = 15
        self.tiempo_ultimo_ataque = 0
        self.altura_salto = 30
        self.max_altura = self.y - 250
        self.max_lateral = self.x - 150
        self.state = "alive"
    def draw(self, ventana):
        if self.state == "alive":
            imagen = self.image[0]
        elif self.state == "dead":    
            imagen = self.image[3]
        ventana.blit(imagen, (self.x, self.y))
    def actualizar(self):
        if self.state == "alive":
            # Movimiento lateral
            self.x += self.velocidad_X

            # Movimiento vertical
            if self.saltando:
                self.y += self.velocidad_Y
                self.velocidad_Y += self.gravedad

                # Cuando alcanza el suelo, detiene el salto y restaura la posición inicial en y
                if self.y >= 550 - 80:
                    self.saltando = False
                    self.y = 550 - 80
                    self.velocidad_Y = 0
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_salto >= 2500:  # 2000 milisegundos = 2 segundos
                self.saltar()
                self.tiempo_ultimo_salto = tiempo_actual
            # Control de límites
            if self.y <= self.max_altura:
                self.velocidad_Y = -self.velocidad_Y  # Cambia la dirección vertical si alcanza la altura máxima
            if self.x <= self.max_lateral or self.x >= self.min_lateral:
                self.velocidad_X = -self.velocidad_X  # Cambia la dirección lateral si alcanza los límites laterales
    def reset(self):
        self.x = 650
        self.y = 550 - 80
        self.velocidad_X = -3
   
class VillanoFinal(Villano):
    def __init__(self):
        super().__init__()
        self.width = 122
        self.heigth = 104
        self.image = movimientos_personajes('imagenes\\personajes\\villanoDef.png', self.width, self.heigth)
        self.image = rotar_imagen(self.image)
        self.vida = 200
        self.damage = 20
        self.tiempo_ultimo_ataque = 0
        self.altura_salto = 30
        self.max_altura = self.y - 250
        self.max_lateral = self.x - 150
        self.state = "alive"
    def draw(self, ventana):
        if self.state == "alive":
            imagen = self.image[0]
        elif self.state == "dead":    
            imagen = self.image[3]
        ventana.blit(imagen, (self.x, self.y))
    def actualizar(self):
        if self.state == "alive":
            # Movimiento lateral
            self.x += self.velocidad_X

            # Movimiento vertical
            if self.saltando:
                self.y += self.velocidad_Y
                self.velocidad_Y += self.gravedad

                # Cuando alcanza el suelo, detiene el salto y restaura la posición inicial en y
                if self.y >= 550 - 80:
                    self.saltando = False
                    self.y = 550 - 80
                    self.velocidad_Y = 0
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_salto >= 2500:  # 2000 milisegundos = 2 segundos
                self.saltar()
                self.tiempo_ultimo_salto = tiempo_actual
            # Control de límites
            if self.y <= self.max_altura:
                self.velocidad_Y = -self.velocidad_Y  # Cambia la dirección vertical si alcanza la altura máxima
            if self.x <= self.max_lateral or self.x >= self.min_lateral:
                self.velocidad_X = -self.velocidad_X  # Cambia la dirección lateral si alcanza los límites laterales
    def reset(self):
        self.x = 650
        self.y = 550 - 80
        self.velocidad_X = -3
    def atacar(self, ataques,bola2 = 0):
        if self.state == "alive":
            tiempo_actual = pygame.time.get_ticks()
            #numero aleatorio entre 0 y 2 y tiene que ser entero
            
            # Atacar cada dos segundos (2000 milisegundos)
            if tiempo_actual - self.tiempo_ultimo_ataque >= 1000:
                # Generar posición aleatoria en el rango especificado
                pos_y_aleatoria = random.randint(300, 500)
                pos_y_aleatoria2 = random.randint(0, 200)
                n = random.randint(0,2)
                # Atacar en la posición X actual del villano y la posición Y generada aleatoriamente
                if self.dir == 1:
                    i = -1
                elif self.dir == 0:
                    i = 1
                if bola2 != 0:
                    bola2.fire(pos_y_aleatoria2, 0)
                ataque = ataques[n]
                ataque.fire(self.x, pos_y_aleatoria, i)

                self.tiempo_ultimo_ataque = tiempo_actual
