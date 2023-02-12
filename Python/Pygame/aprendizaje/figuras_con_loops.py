import pygame, sys
pygame.init()

#---------------------------------------------------------COLORES---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED =  (255,0,0)
BLUE = (0,0,255)
CARNE=(236,211,151)
#---------------------------------------------------------PANTALLA---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
size = (800, 600)
screen = pygame.display.set_mode(size)

while True:
    #------------------------------------------------------SALIR---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(WHITE)
    
    for x in range(100, 800, 100): #(pixel inicial, pixel final, recorreriendo cada x pixeles)
        #pygame.draw.rect(screen, BLUE, (x, 250, 50, 50)) #se dibujarán muchos cubos azules uno seguido de otro, con separaciones debido al tercer valor del range()
        #pygame.draw.line(screen, GREEN, (x,0),(x,100),10)
        pygame.draw.rect(screen, CARNE, (x,500, 50, 70))
    
    window = pygame.draw.rect
    for x in range (110, 140, 20):
        window(screen, BLUE, (x,515, 10, 10))
        for i in range(110, 800, 50):
            window(screen, BLUE, (i,515, 10, 10))
    pygame.display.flip()