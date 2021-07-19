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

""" DEFINIÇÃO DO LOOP """
time = pygame.time.Clock() # Relógio de frames. 

OFF = True
while OFF:
    time.tick(300) # Frames por segundo (quanto maior, mais rápido fica). 
    for choice in pygame.event.get(): # Interação com ocorrências/ Definição de eventos.
        if choice.type == QUIT: # Opção para sair do jogo. 
            OFF = False
            
    gamescreen.fill(white) # Cor de fundo da tela. 

    pygame.display.update() # Atualização da tela (porções da tela).

""" FINALIZAR JOGO """
pygame.quit()
quit()