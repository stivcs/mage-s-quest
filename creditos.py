'''
Juego mage's quest creditos
fecha:20/11/23
version: 2
autores: ING(c): Stiven Castro Soto, Santiago Suaza Builes
'''
import pygame

# Función para mostrar los créditos desplazándose hacia arriba desde la parte inferior de la pantalla
def creditos():
    """
    Función que muestra la pantalla de creditos del juego.
    """
    ancho_ventana = 800
    alto_ventana = 600  
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("creditos")
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.Font("letras\\PressStart2P-Regular.ttf", 19)
    pygame.mixer.init()
    # Cargar la canción
    pygame.mixer.music.load('sonidos\\rock.wav')  # Reemplaza con la ruta de tu canción
    # Reproducir la canción en bucle
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)
    texto_creditos = [
        "Desarrollado por:",
        "ING(c)",
        "Stiven Castro Soto",
        "",
        "Música por:",
        "kopinkop",
        "audiogarden",
        "Motion Array Originals: Classics",
        "",
        "Efectos por:",
        "",
        "leohpaz",
        "Brandon Morris",
        "HaelDB",
        "",
        "Arte por:",
        "",
        "Balmer",
        "thomaswp",
        "reivaxcorp",
        "Ramandu",
        "DALL-E 3 (IA)",
        "",
        "Gracias por jugar",
        "",
        "Presiona ESC para salir"
    ]

    run = True
    espacio_entre_lineas = 30  # Ajusta el espacio entre líneas
    velocidad_desplazamiento = 2.5  # Ajusta la velocidad de desplazamiento
    y = 600  # Inicializa la posición en la parte inferior de la pantalla

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        ventana.fill((0, 0, 0))  # Llena la pantalla con color negro

        # Mostrar los créditos línea por línea con desplazamiento hacia arriba
        offset = y
        for line in texto_creditos:
            texto = font.render(line, True, (255, 255, 255))
            text_rect = texto.get_rect(midtop=(400, offset))
            ventana.blit(texto, text_rect)
            offset += espacio_entre_lineas  # Espacio entre líneas

        y -= velocidad_desplazamiento  # Desplazamiento hacia arriba

        # Reiniciar el desplazamiento cuando alcanza cierto límite
        if y < -len(texto_creditos) * espacio_entre_lineas:
            y = 600

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
