import pygame, sys
pygame.init()

#---------------------------------------------------------COLORES---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
BLACK = (0,0,0) #creamos el color negro con su código RGB
WHITE = (255,255,255)
GREEN = (0,255,0)
RED =  (255,0,0)
BLUE = (0,0,255)

#---------------------------------------------------------PANTALLA---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
size = (800, 600)
screen = pygame.display.set_mode(size)

while True: #declaramos void Update()
    #------------------------------------------------------SALIR---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(WHITE) #ponemos la pantalla de color blanco, por defecto es negro
    
    #-------------------------------------------------------DIBUJO---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #info en https://pygame.ord/docs/ref/draw.html
    pygame.draw.line(screen, GREEN, [0,100], [100,100], 5) #con draw.line(lugar, color, [de donde a donde en eje x], [de donde a donde en eje x], grosor) dibujamos una línea
    pygame.draw.rect(screen, BLACK, (150, 100, 80, 80)) #con draw.rect(lugar, color, (punto de inicio x, punto de inicio y, ancho, alto)) dibujamos un cuadrado
    pygame.draw.circle(screen, RED, (200, 200), 10) #con draw.circle(lugar, color, (x,y), radio, ancho(opcional)) dibujamos un circulo
    
    pygame.display.flip()