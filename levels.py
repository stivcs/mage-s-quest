import pygame
from clases import *

escenarios = []
escenarios.append(pygame.image.load("imagenes\\escenarios\\escenario-1.1.png")) 
escenarios.append(pygame.image.load("imagenes\\escenarios\\escenario-2.1.png"))
escenarios.append(pygame.image.load("imagenes\\escenarios\\escenario-3.1.png"))
escenarios.append(pygame.image.load("imagenes\\escenarios\\escenario-4.1.png"))
escenarios.append(pygame.image.load("imagenes\\escenarios\\escenario-5.1.png"))
piso = pygame.image.load("imagenes\\escenarios\\piso.png")
pygame.mixer.init()
level_complete = pygame.mixer.Sound('sonidos\\gmae.wav')

def manejar_eventos(prota, ataque):
    runing = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runing = False
            if event.key == pygame.K_d:
                prota.derecha()
            if event.key == pygame.K_a:
                prota.izquierda()
            if event.key == pygame.K_w:
                prota.saltar()
            if event.key == pygame.K_SPACE:
                ataque.fire(prota.x, prota.y, prota.dire())
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                prota.detener()
    return runing

def level_01():
    pygame.init()
    pygame.mixer.init()
    # Cargar la canción
    pygame.mixer.music.load('sonidos\\Race With Life.wav')  # Reemplaza con la ruta de tu canción
    # Reproducir la canción en bucle
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    clock = pygame.time.Clock()
    runing = True
    fondo = escenarios[0]
    screen = pygame.display.set_mode(fondo.get_size())
    pygame.display.set_caption("mages quest")
    screen.blit(fondo,(0,0))
    prota = Protagonista()
    ataqueProtagonista = BolaFuego()
    ataqueVillano = BolaTierra()
    villano = Villano()
    # mensaje_inicial(screen,fondo)

    while runing:
        runing = manejar_eventos(prota, ataqueProtagonista)

        screen.blit(fondo,(0,0))
        prota.actualizar()
        prota.draw(screen)
        ataqueProtagonista.move()
        ataqueProtagonista.draw(screen)
        ataqueVillano.move()
        ataqueVillano.draw(screen)
        prota.impacto(ataqueVillano)
        prota.impacto(villano) 
        prota.mostrar_vida(screen)
        villano.actualizar()
        villano.draw(screen)
        villano.atacar(ataqueVillano)
        villano.impacto(ataqueProtagonista)
        villano.mostrar_vida(screen)
        if prota.vida <= 0:
            runing = False
            mostrar_mensaje(screen, "perdiste, lo siento", 2)
            game_over()
        if villano.vida <= 0 and prota.x >= 800:
            runing = False
            level_complete.play()
            mostrar_mensaje(screen, "Pasas al siguiente nivel", 2)
            #level 2
            
            level_02(prota)

        clock.tick(30)
        pygame.display.update()

    pygame.quit()

def level_02(prota):
    pygame.init()
    clock = pygame.time.Clock()
    runing = True
    fondo = escenarios[1]
    screen = pygame.display.set_mode(fondo.get_size())
    pygame.display.set_caption("mages quest")
    screen.blit(fondo,(0,0))
    screen.blit(piso,(0,550))
    prota.reset()
    ataqueProtagonista = BolaFuego()
    ataqueVillano = IceAttack()
    villano = villanoHielo()
    ataqueProtagonista.damage = 30
    while runing:
        runing =  manejar_eventos(prota, ataqueProtagonista)

        screen.blit(fondo,(0,0))
        screen.blit(piso,(0,550))
        prota.actualizar()
        prota.draw(screen)
        ataqueProtagonista.move()
        ataqueProtagonista.draw(screen)
        ataqueVillano.move()
        ataqueVillano.draw(screen)
        prota.impacto(ataqueVillano) 
        prota.impacto(villano)
        prota.mostrar_vida(screen)
        villano.actualizar()
        villano.draw(screen)
        villano.atacar(ataqueVillano)
        villano.impacto(ataqueProtagonista)
        villano.mostrar_vida(screen)
        if prota.vida <= 0:
            runing = False
            mostrar_mensaje(screen, "perdiste, lo siento", 2)
            game_over()
        if villano.vida <= 0 and prota.x >= 800:
            runing = False
            level_complete.play()
            mostrar_mensaje(screen, "Pasas al siguiente nivel", 2)
            #level 3
            level_03(prota)

        clock.tick(30)
        pygame.display.update()

    pygame.quit()

def level_03(prota):
    pygame.init()
    clock = pygame.time.Clock()
    runing = True
    fondo = escenarios[2]
    screen = pygame.display.set_mode(fondo.get_size())
    pygame.display.set_caption("mages quest")
    screen.blit(fondo,(0,0))
    screen.blit(piso,(0,550))
    prota.reset()
    ataqueProtagonista = BolaFuego()
    ataqueVillano = BolaTierra()
    villano = Villano()
    ataqueProtagonista.damage = 35
    revivir_villano = False
    tiempo_revivir = 0
    i  = 1
    # mensaje_inicial(screen,fondo)
    while runing:
        runing =  manejar_eventos(prota, ataqueProtagonista)

        screen.blit(fondo,(0,0))
        screen.blit(piso,(0,550))
        prota.actualizar()
        prota.draw(screen)
        ataqueProtagonista.move()
        ataqueProtagonista.draw(screen)
        ataqueVillano.move()
        ataqueVillano.draw(screen)
        prota.impacto(ataqueVillano) 
        prota.impacto(villano)
        prota.mostrar_vida(screen)
        villano.actualizar()
        villano.draw(screen)
        villano.atacar(ataqueVillano)
        villano.impacto(ataqueProtagonista)
        villano.mostrar_vida(screen)
        if prota.vida <= 0:
            runing = False
            mostrar_mensaje(screen, "perdiste, lo siento", 2)
            game_over()
        if villano.vida <= 0 and i == 1:
            i += 1
            
            # Establecer el temporizador para revivir al villano
            revivir_villano = True
            tiempo_revivir = pygame.time.get_ticks()  # Capturar el tiempo actual

        # Si ha pasado el tiempo de espera y se debe revivir al villano
        if revivir_villano and pygame.time.get_ticks() - tiempo_revivir >= 2000:  # 2000 milisegundos = 2 segundos
            mostrar_mensaje(screen,"¡cuidado!",1)
            villano = villanoHielo()  # Revivir al villano
            ataqueVillano = IceAttack()  # Reiniciar los ataques del villano
            revivir_villano = False  # Restablecer la bandera de revivir
        if villano.vida <= 0 and prota.x >= 800:
            runing = False
            level_complete.play()
            mostrar_mensaje(screen, "Pasas al siguiente nivel", 2)
            #level 4
            prota.vida += 20
            level_04(prota)

        clock.tick(30)
        pygame.display.update()

    pygame.quit()

def level_04(prota):
    pygame.init()
    clock = pygame.time.Clock()
    runing = True
    fondo = escenarios[3]
    screen = pygame.display.set_mode(fondo.get_size())
    pygame.display.set_caption("mages quest")
    screen.blit(fondo,(0,0))
    screen.blit(piso,(0,550))
    prota.reset()
    ataqueProtagonista = BolaFuego()
    ataqueVillano = BolaTierra()
    ataqueVillano2 = BolaTierra()
    villano = Villano()
    prota.vida += 25
    ataqueProtagonista.damage = 40
    revivir_villano = False
    tiempo_revivir = 0
    i  = 1
    # mensaje_inicial(screen,fondo)
    while runing:
        runing =  manejar_eventos(prota, ataqueProtagonista)

        screen.blit(fondo,(0,0))
        screen.blit(piso,(0,550))
        prota.actualizar()
        prota.draw(screen)
        ataqueProtagonista.move()
        ataqueProtagonista.draw(screen)
        ataqueVillano.move()
        ataqueVillano.draw(screen)
        ataqueVillano2.move()
        ataqueVillano2.draw(screen)
        prota.impacto(ataqueVillano)
        prota.impacto(ataqueVillano2) 
        prota.impacto(villano)
        prota.mostrar_vida(screen)
        villano.actualizar()
        villano.draw(screen)
        villano.atacar(ataqueVillano,ataqueVillano2)
        villano.impacto(ataqueProtagonista)
        villano.mostrar_vida(screen)
        if prota.vida <= 0:
            runing = False
            mostrar_mensaje(screen, "perdiste, lo siento", 2)
            game_over()
        if villano.vida <= 0 and i == 1:
            i += 1
            
            # Establecer el temporizador para revivir al villano
            revivir_villano = True
            tiempo_revivir = pygame.time.get_ticks()  # Capturar el tiempo actual

        # Si ha pasado el tiempo de espera y se debe revivir al villano
        if revivir_villano and pygame.time.get_ticks() - tiempo_revivir >= 2000:  # 2000 milisegundos = 2 segundos
            mostrar_mensaje(screen,"¡cuidado!",1)
            villano = villanoHielo()  # Revivir al villano
            ataqueVillano = IceAttack()  # Reiniciar los ataques del villano
            ataqueVillano2 = IceAttack()
            revivir_villano = False  # Restablecer la bandera de revivir
        if villano.vida <= 0 and prota.x >= 800:
            runing = False
            level_complete.play()
            mostrar_mensaje(screen, "Pasas al siguiente nivel", 2)
            #level 5
            prota.vida += 50
            level_05(prota)

        clock.tick(30)
        pygame.display.update()

    pygame.quit()

def level_05(prota):
    pygame.init()
    clock = pygame.time.Clock()
    runing = True
    fondo = escenarios[4]
    screen = pygame.display.set_mode(fondo.get_size())
    pygame.display.set_caption("mages quest")
    screen.blit(fondo,(0,0))
    screen.blit(piso,(0,550))
    prota.reset()
    ataqueProtagonista = BolaFuego()
    ataqueVillano = VerticalAttack()
    ataques = []
    ataques.append(BolaFuego())
    ataques.append(BolaTierra())
    ataques.append(IceAttack())
    villano = VillanoFinal()
    prota.vida += 25
    ataqueProtagonista.damage = 40
    while runing:
        runing =  manejar_eventos(prota, ataqueProtagonista)

        screen.blit(fondo,(0,0))
        screen.blit(piso,(0,550))
        prota.actualizar()
        prota.draw(screen)
        ataqueProtagonista.move()
        ataqueProtagonista.draw(screen)
        ataqueVillano.move()
        ataqueVillano.draw(screen)
        for ataque in ataques:
            ataque.move()
            ataque.draw(screen)
            prota.impacto(ataque)
        prota.impacto(ataqueVillano) 
        prota.impacto(villano)
        prota.mostrar_vida(screen)
        villano.actualizar()
        villano.draw(screen)
        villano.atacar(ataques,ataqueVillano)
        villano.impacto(ataqueProtagonista)
        villano.mostrar_vida(screen)
        if prota.vida <= 0:
            runing = False
            mostrar_mensaje(screen, "perdiste, lo siento", 2)
            game_over()
        if villano.vida <= 0:
            runing = False
            level_complete.play()
            mostrar_mensaje(screen, "Felicidades", 1)
            win()

        clock.tick(30)
        pygame.display.update()

    pygame.quit()