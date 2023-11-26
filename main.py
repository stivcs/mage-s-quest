import pygame 
import sys
import levels

def help():
    pygame.init()
    #quiero una imagen de fondo para la screen
    fondo = pygame.image.load("imagenes\\help.png")
    #quiero que la pantalla se adapte a la imagen
    screen = pygame.display.set_mode(fondo.get_size())
    screen.blit(fondo, (0, 0))
    pygame.display.set_caption("help")
    clock = pygame.time.Clock()
    runing = True
    while runing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                runing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 164 and pos[0] <= 441:
                    if pos[1] >= 441 and pos[1] <= 530:
                        menu()
                    

            
        clock.tick(60)
        pygame.display.update()

    pygame.quit() 

def menu():
    pygame.init()
    #quiero una imagen de fondo para la screen
    fondo = pygame.image.load("imagenes\\menu.png")
    #quiero que la pantalla se adapte a la imagen
    screen = pygame.display.set_mode(fondo.get_size())
    screen.blit(fondo, (0, 0))
    pygame.display.set_caption("mages quest menu")
    clock = pygame.time.Clock()
    pygame.mixer.init()
    # Cargar la canción
    pygame.mixer.music.load('sonidos\\rock.wav')  # Reemplaza con la ruta de tu canción
    # Reproducir la canción en bucle
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)
    runing = True
    white = (255, 255, 255)  # Color blanco
    while runing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if x >= 133 and x <= 471:
                    if y >= 255 and y <= 342:
                        pygame.mixer.music.stop()
                        help()
                    if y >= 371 and y <= 461:
                        pygame.mixer.music.stop()
                        levels.level_01()
                    if y >= 482 and y <= 565:
                        print("exit")
                        runing = False
            
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

def main():
    pygame.init()
    #fondo de la screen
    fondo = pygame.image.load("imagenes\\inicio.png")
    #la screen se adapta a la imagen
    screen = pygame.display.set_mode(fondo.get_size())
    screen.blit(fondo, (0, 0))
    pygame.mixer.init()
    # Cargar la canción
    pygame.mixer.music.load('sonidos\\Calling A Hero.mp3')  # Reemplaza con la ruta de tu canción
    # Reproducir la canción en bucle
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)
    pygame.display.set_caption("mages quest")
    clock = pygame.time.Clock()
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                runing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    menu()
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()