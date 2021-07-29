import pygame
from pygame.locals import  * 

""" INICIALIZAR JOGO """
pygame.init() # Inicializa todas as funções e variáveis da biblioteca pygame.

""" CORES """
white = (255,255,255)
black = (0,0,0) 
red = (255,0,0)
green = (0,255,0)
aqua = (20,255,255)
blue = (0,0,255)

""" DEFINIÇÃO DE TELA """

length = 1280 # Comprimento
height = 650  # Altura

gamescreen = pygame.display.set_mode((length,height)) # Inicializa uma janela ou tela para exibição.
pygame.display.set_caption("Starving Snake") # Nome na janela do jogo.

""" IMPORTING THE SNAKE """

x = 520
y = 500 

snakesback = pygame.image.load("back/snakeback_0.png")
snakesback = pygame.transform.scale(snakesback,(100,100))
snakesfront = pygame.image.load("front/snakefront_0.png")
snakesfront = pygame.transform.scale(snakesfront,(100,100))
snakesright = pygame.image.load("right/snakeright_0.png")
snakesright = pygame.transform.scale(snakesright,(100,100))
snakesleft = pygame.image.load("left/snakeleft_0.png")
snakesleft = pygame.transform.scale(snakesleft,(100,100))

snake = snakesfront

time = pygame.time.Clock() # Relógio de frames.

""" DEFINIÇÃO DO LOOP """

OFF = True
while OFF:
    time.tick(5) # Frames por segundo (quanto maior, mais rápido fica).
    gamescreen.fill(white) # Cor de fundo da tela. 
    for choice in pygame.event.get(): # Interação com ocorrências/ Definição de eventos.
        if choice.type == QUIT: # Opção para sair do jogo. 
            OFF = False

    if pygame.key.get_pressed()[K_w]:
        snake = snakesback
        y -= 100 #UP
    if pygame.key.get_pressed()[K_s]:
        snake = snakesfront
        y += 100 #DOWN
    if pygame.key.get_pressed()[K_d]:
        snake = snakesright
        x += 100 #RIGHT
    if pygame.key.get_pressed()[K_a]:
        snake = snakesleft
        x -= 100 #LEFT

        
    if choice.type == KEYDOWN:
        if choice.key == pygame.K_UP:
            snake = snakesback
            y -= 100 #UP
        if choice.key == pygame.K_DOWN:
            snake = snakesfront
            y += 100 #DOWN
        if choice.key == pygame.K_RIGHT:
            snake = snakesright
            x += 100 #RIGHT
        if choice.key == pygame.K_LEFT:
            snake = snakesleft
            x -= 100 #LEFT
            
    gamescreen.blit(snake,(x,y))
    pygame.display.update() # Atualização da tela (porções da tela).

""" FINALIZAR JOGO """
pygame.quit()
quit()

