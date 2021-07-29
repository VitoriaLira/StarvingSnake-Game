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
class Snakeback(pygame.sprite.Sprite):
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
        self.rect.topleft = 520,300
        
        self.above = False


    def up(self):
        self.above = True
     

    def update(self):
        self.currently = self.currently + 1
        """if self.rect.bottom < 0:
            self.rect.y = height""" #PARA QUE A COBRA VOLTE CASO ELA SUMA NA BORDA.
        """self.rect.y -= 20""" # PARA A COBRAR SE MOVIMENTAR SOZINHA NA VERTICAL.
        if self.above == True:
            self.rect.y -= 100
            self.above = False
        if self.currently >= len(self.snakesback):
            self.currently = 0
        self.image = self.snakesback[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))
        

allback = pygame.sprite.Group()
snakeback = Snakeback()
allback.add(snakeback)

class Snakefront(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakesfront = []
        self.snakesfront.append(pygame.image.load("front/snakefront_0.png"))
        self.snakesfront.append(pygame.image.load("front/snakefront_1.png"))
        self.currently = 0
        self.image = self.snakesfront[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 520,300

        self.below = False

    def down(self):
         self.below = True

    def update(self):
        self.currently = self.currently + 1
        if self.below == True:
            self.rect.y += 100
            self.below = False
        if self.currently >= len(self.snakesfront):
            self.currently = 0
        self.image = self.snakesfront[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))

allfront = pygame.sprite.Group()
snakefront = Snakefront()
allfront.add(snakefront)


class Snakeright(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakesright = []
        self.snakesright.append(pygame.image.load("right/snakeright_0.png"))
        self.snakesright.append(pygame.image.load("right/snakeright_1.png"))
        self.currently = 0
        self.image = self.snakesright[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 520,300

        self.east = False #Right

    def right(self):
        self.east = True

    def update(self):
        self.currently = self.currently + 1
        if self.east == True:
            self.rect.x += 100
            self.east = False
        if self.currently >= len(self.snakesright):
            self.currently = 0
        self.image = self.snakesright[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))

allright = pygame.sprite.Group()
snakeright = Snakeright()
allright.add(snakeright)        
        

class Snakeleft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakesleft = []
        self.snakesleft.append(pygame.image.load("left/snakeleft_0.png"))
        self.snakesleft.append(pygame.image.load("left/snakeleft_1.png"))
        self.currently = 0
        self.image = self.snakesleft[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 520,300

        self.west = False #Left

    def left(self):
        self.west = True

    def update(self):
        self.currently = self.currently + 1
        if self.west == True:
            self.rect.x -= 100
            self.west = False
        if self.currently >= len(self.snakesleft):
            self.currently = 0
        self.image = self.snakesleft[self.currently]
        self.image = pygame.transform.scale(self.image,(200,200))


allleft = pygame.sprite.Group()
snakeleft = Snakeleft()
allleft.add(snakeleft)



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
                snakeback.up()
            if choice.key == pygame.K_DOWN:
                snakefront.down()
            if choice.key == pygame.K_RIGHT:
                snakeright.right()
            if choice.key == pygame.K_LEFT:
                snakeleft.left()
                
        if choice.type == KEYDOWN:
            if choice.key == K_w:
                snakeback.up()
                #y -= 20 #UP
            if choice.key == K_s:
                snakefront.down()
                #y += 20 #DOWN
            if choice.key == K_d:
                snakeright.right()
                #x += 20 #RIGHT
            if choice.key == K_a:
                snakeleft.left()
                #x -= 20 #LEFT


    allback.draw(gamescreen)
    allback.update()
    allfront.draw(gamescreen)
    allfront.update()
    allright.draw(gamescreen)
    allright.update()
    allleft.draw(gamescreen)
    allleft.update()
    
    pygame.display.flip() # Atualização da tela (porções da tela).

""" FINALIZAR JOGO """
pygame.quit()
quit()

