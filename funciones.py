'''
Juego mage's quest funciones
fecha:20/11/23
version: 2
autores: ING(c): Stiven Castro Soto, Santiago Suaza Builes
'''
import pygame 
import sys
import random
from creditos import creditos
def mostrar_mensaje(ventana, mensaje, duracion_ms):
    """
    Muestra un mensaje en la ventana durante una duración específica.

    Parámetros:
    ventana (Surface): La ventana de Pygame donde se muestra el mensaje.
    mensaje (str): El mensaje que se mostrará en la ventana.
    duracion_segundos (float): La duración en segundos durante la cual se mostrará el mensaje.

    Salida:
    None
    """
    fuente1 = pygame.font.Font('letras\\PressStart2P-Regular.ttf', 20)
    fuente2 = pygame.font.Font('letras\\8-bit Arcade In.ttf', 36)
    fuente3 = pygame.font.Font('letras\\Crang.ttf', 36)
    duracion_ms *= 1000
    texto = fuente1.render(mensaje, True, (255, 255, 255))
    texto_ancho, texto_alto = texto.get_size()

    # Dibujar un rectángulo negro detrás del texto
    pygame.draw.rect(ventana, (0, 0, 0), ((ventana.get_width() - texto_ancho) // 2 - 10, (ventana.get_height() - texto_alto) // 2 - 10, texto_ancho + 20, texto_alto + 20))

    # Dibujar el texto en la ventana
    ventana.blit(texto, ((ventana.get_width() - texto_ancho) // 2, (ventana.get_height() - texto_alto) // 2))
    pygame.display.update()


    inicio_tiempo = pygame.time.get_ticks()
    tiempo_actual = 0

    while tiempo_actual < duracion_ms:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tiempo_actual = pygame.time.get_ticks() - inicio_tiempo

    # Limpiar la pantalla después del tiempo de duración
    pygame.display.update()

def mensaje_inicial(screen,fondo):
    """
    Muestra una serie de mensajes iniciales en la pantalla de juego.

    Parámetros:
    screen (Surface): La pantalla de Pygame donde se mostrarán los mensajes.
    fondo (Surface): La imagen de fondo de la pantalla de juego.

    Salida:
    None
    """
    mostrar_mensaje(screen, "Hola bienvenido a mi juego", 2)
    screen.blit(fondo,(0,0))
    mostrar_mensaje(screen, "te mueves con las teclas 'A' y 'D'", 2)
    screen.blit(fondo,(0,0))
    mostrar_mensaje(screen, "atacas con el espacio y saltas con 'w'", 2)
    screen.blit(fondo,(0,0))
    mostrar_mensaje(screen, "espero lo disfrutes", 2)
    screen.blit(fondo,(0,0))

def movimientos_personajes(imagen,width,height):
    """
    Carga una imagen con sprites y extrae los cuadros de animación.

    Parámetros:
    imagen (str): La ruta de la imagen que contiene los sprites.
    width (int): El ancho de cada cuadro de animación.
    height (int): La altura de cada cuadro de animación.

    Salida:
    list: Una lista de superficies, cada una representa un cuadro de animación.
    """
    sprite_sheet = pygame.image.load(imagen)  # Reemplaza con la ruta de tu imagen
    movimientos_personaje = []
    # Obtener cada cuadro de animación de la hoja de sprites y agregarlo a la lista
    for i in range(0, sprite_sheet.get_width(), width):
        cuadro = sprite_sheet.subsurface(pygame.Rect(i, 0, width, height))
        movimientos_personaje.append(cuadro)
    return movimientos_personaje

def rotar_imagen(list):
    """
    Voltea horizontalmente las imágenes en una lista.

    Parámetros:
    lista (list): Una lista de superficies (imágenes).

    Salida:
    list: Una lista de superficies (imágenes) volteadas horizontalmente.
    """
    list2 = []
    for i in list:
        list2.append(pygame.transform.flip(i, True,False))
    return list2

def game_over():
    """
    Pantalla de Game Over.

    Parámetros:
    Ninguno

    Salida:
    None
    """
    pygame.init()
    #fondo de la screen
    fondo = pygame.image.load("imagenes\\game-over.png")
    #la screen se adapta a la imagen
    screen = pygame.display.set_mode(fondo.get_size())
    screen.blit(fondo, (0, 0))
    pygame.mixer.init()
    # Cargar la canción
    pygame.mixer.music.load('sonidos\\Motivation Piano with   Cello and Drums .wav')  # Reemplaza con la ruta de tu canción
    # Reproducir la canción en bucle
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("game over")
    clock = pygame.time.Clock()
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                runing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    creditos()
                    runing = False
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

def win():
    """
    Pantalla de victoria.

    Parámetros:
    Ninguno

    Salida:
    None
    """
    pygame.init()
    #fondo de la screen
    fondo = pygame.image.load("imagenes\\win.png")
    #la screen se adapta a la imagen
    screen = pygame.display.set_mode(fondo.get_size())
    screen.blit(fondo, (0, 0))
    pygame.mixer.init()
    # Cargar la canción
    pygame.mixer.music.load('sonidos\\Calling A Hero.mp3')  # Reemplaza con la ruta de tu canción
    # Reproducir la canción en bucle
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("win")
    clock = pygame.time.Clock()
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                runing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    creditos()
                    runing = False
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

