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

x = length/2
y = height/2

gamescreen = pygame.display.set_mode((length,height)) # Inicializa uma janela ou tela para exibição.
pygame.display.set_caption("Starving Snake") # Nome na janela do jogo.

""" IMPORTING THE SNAKE """
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakesback = []
        self.snakesback.append(pygame.image.load("back/snakeback_0.png"))
        self.snakesback.append(pygame.image.load("back/snakeback_1.png"))
        self.snakesback.append(pygame.image.load("back/snakeback_2.png"))
        self.currently = 0
        self.image = self.snakesback[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))

        self.rect = self.image.get_rect()
        self.rect.topleft = 400,400

    def update(self):
        self.currently = self.currently + 1
        if self.currently >= len(self.snakesback):
            self.currently = 0
        self.image = self.snakesback[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))
        

all = pygame.sprite.Group()
snake = Snake()
all.add(snake)

time = pygame.time.Clock() # Relógio de frames. 

""" DEFINIÇÃO DO LOOP """

OFF = True
while OFF:
    time.tick(5) # Frames por segundo (quanto maior, mais rápido fica). 
    gamescreen.fill(white) # Cor de fundo da tela. 
    for choice in pygame.event.get(): # Interação com ocorrências/ Definição de eventos.
        if choice.type == QUIT: # Opção para sair do jogo. 
            OFF = False
        
        """if choice.type == KEYDOWN:
            if pygame.key.get_pressed()[K_w]:
                y -= 20 #UP
            if pygame.key.get_pressed()[K_s]:
                y += 20 #DOWN
            if pygame.key.get_pressed()[K_d]:
                x += 20 #RIGHT
            if pygame.key.get_pressed()[K_a]:
                x -= 20 #LEFT"""
    all.draw(gamescreen)
    all.update()

    pygame.display.flip() # Atualização da tela (porções da tela).

""" FINALIZAR JOGO """
pygame.quit()
quit()

