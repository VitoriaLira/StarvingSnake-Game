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
        self.snakesfront = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.snakesback = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png")]
        self.snakesright = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
        self.snakesleft = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
        self.currently = 0
        self.sprite = self.snakesfront[self.currently]
        self.image = pygame.transform.scale(self.sprite,(200,200))

        self.rect = self.image.get_rect()
        self.rect.topleft = 520,500
        
        self.above = False
        self.below = False
        self.east = False #Right
        self.west = False #Left


    def up(self):
        self.above = True

    def down(self):
         self.below = True

    def right(self):
        self.east = True

    def left(self):
        self.west = True
     

    def update(self):
        self.currently = self.currently + 1
        if self.above == True:
            self.rect.y -= 100
            self.above = False            
            if self.currently >= len(self.snakesfront):
                self.currently = 0
            self.sprite = self.snakesback[self.currently]
           
        if self.below == True:
            self.rect.y += 100
            self.below = False
            
            if self.currently >= len(self.snakesback):
                self.currently = 0
            self.sprite = self.snakesfront[self.currently]


        if self.east == True:            
            self.rect.x += 100
            self.east = False
            if self.currently >= len(self.snakesright):
                self.currently = 0
            self.sprite = self.snakesright[self.currently]
           
            

        if self.west == True:
            self.rect.x -= 100
            self.west = False
            
            if self.currently >= len(self.snakesleft):
                self.currently = 0
            self.sprite = self.snakesleft[self.currently]

        self.image = pygame.transform.scale(self.sprite, (200,200))
	
                
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

        if choice.type == KEYDOWN:
            if choice.key == pygame.K_UP:
                snake.up()
            if choice.key == pygame.K_DOWN:
                snake.down()
            if choice.key == pygame.K_RIGHT:
                snake.right()
            if choice.key == pygame.K_LEFT:
                snake.left()


        """if pygame.key.get_pressed()[K_w]:
            snake.up()
        if pygame.key.get_pressed()[K_s]:
            snake.down()
        if pygame.key.get_pressed()[K_d]:
            snake.right()
        if pygame.key.get_pressed()[K_a]:
            snake.left()"""
        


        if choice.type == KEYDOWN:
            if choice.key == K_w:
                snake.up()
                #y -= 20 #UP
            if choice.key == K_s:
                snake.down()
                #y += 20 #DOWN
            if choice.key == K_d:
                snake.right()
                #x += 20 #RIGHT
            if choice.key == K_a:
                snake.left()
                #x -= 20 #LEFT
    
    all.draw(gamescreen)
    all.update()
    
    pygame.display.flip() # Atualização da tela (porções da tela).

""" FINALIZAR JOGO """
pygame.quit()

