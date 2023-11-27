'''
Juego mage's quest main
fecha:20/11/23
version: 2
autores: ING(c): Stiven Castro Soto, Santiago Suaza Builes
'''
import pygame 
import sys
import levels

def help():
    """
    Función que muestra la pantalla de ayuda.
    """
    pygame.init()
    fondo = pygame.image.load("imagenes\\help.png")  # Carga la imagen de fondo
    screen = pygame.display.set_mode(fondo.get_size())  # Ajusta la pantalla al tamaño de la imagen
    screen.blit(fondo, (0, 0))  # Muestra la imagen en la pantalla
    pygame.display.set_caption("help")  # Establece el título de la ventana
    clock = pygame.time.Clock()
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                runing = False  # Sale del bucle si se cierra la ventana o se presiona una tecla
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Verifica la posición del clic y llama al menú si se hace clic en una cierta área
                if 164 <= pos[0] <= 441 and 441 <= pos[1] <= 530:
                    menu()
        clock.tick(60)
        pygame.display.update()
    pygame.quit() 

def menu():
    """
    Función que muestra el menú principal del juego.
    """
    pygame.init()
    fondo = pygame.image.load("imagenes\\menu.png")  # Carga la imagen de fondo
    screen = pygame.display.set_mode(fondo.get_size())  # Ajusta la pantalla al tamaño de la imagen
    screen.blit(fondo, (0, 0))  # Muestra la imagen en la pantalla
    pygame.display.set_caption("mages quest menu")  # Establece el título de la ventana
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load('sonidos\\rock.wav')  # Carga la música de fondo
    pygame.mixer.music.play(-1)  # Reproduce la música en bucle
    pygame.mixer.music.set_volume(0.4)  # Establece el volumen de la música
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                # Verifica la posición del clic y realiza acciones según el área clicada
                if 133 <= x <= 471:
                    if 255 <= y <= 342:
                        pygame.mixer.music.stop()
                        help()
                    if 371 <= y <= 461:
                        pygame.mixer.music.stop()
                        levels.level_01()
                    if 482 <= y <= 565:
                        print("exit")
                        runing = False  # Sale del bucle al seleccionar salir
        clock.tick(60)
        pygame.display.update()
    pygame.quit()

def main():
    """
    Función principal que muestra la pantalla de inicio del juego.
    """
    pygame.init()
    fondo = pygame.image.load("imagenes\\inicio.png")  # Carga la imagen de fondo
    screen = pygame.display.set_mode(fondo.get_size())  # Ajusta la pantalla al tamaño de la imagen
    screen.blit(fondo, (0, 0))  # Muestra la imagen en la pantalla
    pygame.mixer.init()
    pygame.mixer.music.load('sonidos\\Calling A Hero.mp3')  # Carga la música de fondo
    pygame.mixer.music.play(-1)  # Reproduce la música en bucle
    pygame.mixer.music.set_volume(0.4)  # Establece el volumen de la música
    pygame.display.set_caption("mages quest")  # Establece el título de la ventana
    clock = pygame.time.Clock()
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                runing = False  # Sale del bucle si se cierra la ventana o se presiona una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    menu()  # Llama al menú principal al presionar la tecla "Enter"
        clock.tick(60)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()  # Inicia la función principal si este archivo es ejecutado directamente
