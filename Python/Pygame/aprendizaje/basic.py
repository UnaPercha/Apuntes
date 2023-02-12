import pygame, sys #importar pygame
pygame.init() #iniciar pygame

#---------------------------------------------------------PANTALLA---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
size = (800, 600) #declaramos tamaño de la ventana
screen = pygame.display.set_mode(size) #crear ventana

while True: #declaramos void Update()
    #------------------------------------------------------SALIR---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get(): #estos son todos los eventos que ocurren en el juego(básicamente todo el juego)
        #esto es para salir del juego siempre
        if event.type == pygame.QUIT: #si el evento es QUITAR JUEGO
            sys.exit() #que salga del juego
    
    pygame.display.flip() #actualizar pantalla