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


""" IMPORTING THE BACKGROUND """

background = pygame.image.load("images/Cenário Deserto3D.png").convert() 
background = pygame.transform.scale(background,(1280,650)) 


""" IMPORTING THE SNAKE """

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 650,50
        
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
            del self.snakes[0:4]
            self.snakes.append(pygame.image.load("back/snakeback_0.png"))
            self.snakes.append(pygame.image.load("back/snakeback_1.png"))
            self.snakes.append(pygame.image.load("back/snakeback_2.png"))
            #self.snakes = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png"),pygame.image.load("back/snakeback_2.png")]
            self.rect.y -= 100
            self.above = False
                    
        if self.below == True:
            del self.snakes[0:4]
            self.snakes.append(pygame.image.load("front/snakefront_0.png"))
            self.snakes.append(pygame.image.load("front/snakefront_1.png"))
            #self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
            self.rect.y += 100
            self.below = False

        if self.east == True:
            del self.snakes[0:4]
            self.snakes.append(pygame.image.load("right/snakeright_0.png"))
            self.snakes.append(pygame.image.load("right/snakeright_1.png"))
            #self.snakes = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
            self.rect.x += 100
            self.east = False

        if self.west == True:
            del self.snakes[0:4]
            self.snakes.append(pygame.image.load("left/snakeleft_0.png"))
            self.snakes.append(pygame.image.load("left/snakeleft_1.png"))
            #self.snakes = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
            self.rect.x -= 100
            self.west = False
            
        if self.currently >= len(self.snakes):
            self.currently = 0
        self.image = self.snakes[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))

all = pygame.sprite.Group()
snake = Snake()
all.add(snake)


""" IMPORTING CACTO """

class Cacto1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto1 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto1
        self.image = pygame.transform.scale(self.image,(100,200))

        self.rect = self.image.get_rect()
        self.rect.topleft = 520,0
        
obstaculos_deserto = pygame.sprite.Group()

cacto1 = Cacto1()
all.add(cacto1)
obstaculos_deserto.add(cacto1)



class Cacto11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto11 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto11
        self.image = pygame.transform.scale(self.image,(100,200))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,200
        
cacto11 = Cacto11()
all.add(cacto11)
obstaculos_deserto.add(cacto11)



class Cacto12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto12 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto12
        self.image = pygame.transform.scale(self.image,(100,200))

        self.rect = self.image.get_rect()
        self.rect.topleft = 750,280
        

cacto12 = Cacto12()
all.add(cacto12)
obstaculos_deserto.add(cacto12)



class Cacto13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto13 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto13
        self.image = pygame.transform.scale(self.image,(100,200))

        self.rect = self.image.get_rect()
        self.rect.topleft = 1000,420
        
        
cacto13 = Cacto13()
all.add(cacto13)
obstaculos_deserto.add(cacto13)



class Cacto2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto2 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto2
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 1100,190
        
cacto2 = Cacto2()
all.add(cacto2)
obstaculos_deserto.add(cacto2)


class Cacto21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto21 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto21
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 780,0
        
cacto21 = Cacto21()
all.add(cacto21)
obstaculos_deserto.add(cacto21)


class Cacto22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto22 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto22
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100,20
        
cacto22 = Cacto22()
all.add(cacto22)
obstaculos_deserto.add(cacto22)


class Cacto23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto23 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto23
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 150,470
        
cacto23 = Cacto23()
all.add(cacto23)
obstaculos_deserto.add(cacto23)


class Cacto24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto24 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto24
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 520,440
        
cacto24 = Cacto24()
all.add(cacto24)
obstaculos_deserto.add(cacto24)


class Cacto25(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto25 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto25
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 275,220
        
cacto25 = Cacto25()
all.add(cacto25)
obstaculos_deserto.add(cacto25)


""" IMPORTING ESCORPIÃO"""

class Escorpiao1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao1 = pygame.image.load("images/escorpião1.png")
        self.image = self.escorpiao1
        self.image = pygame.transform.scale(self.image,(64,64))

        self.rect = self.image.get_rect()
        self.rect.topleft = 400,0

    def update(self):
        if self.rect.bottom > height:
            self.rect.y = 0
        self.rect.y += 20
        self.image = self.escorpiao1
        self.image = pygame.transform.scale(self.image,(64,64))
    
escorpiao1 = Escorpiao1()
all.add(escorpiao1)
obstaculos_deserto.add(escorpiao1)


class Escorpiao2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao2 = pygame.image.load("images/escorpião1.png")
        self.image = self.escorpiao2
        self.image = pygame.transform.scale(self.image,(64,64))

        self.rect = self.image.get_rect()
        self.rect.topleft = 900, 550

    def update(self):
        if self.rect.bottom < 0:
            self.rect.y = height
        self.rect.y -= 20
        self.image = self.escorpiao2
        self.image = pygame.transform.scale(self.image,(64,64))
    
escorpiao2 = Escorpiao2()
all.add(escorpiao2)
obstaculos_deserto.add(escorpiao2)




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



    collides = pygame.sprite.spritecollide(snake,obstaculos_deserto,False)
        
    if collides:
       break
    else:
        all.update()



    gamescreen.blit(background,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
    all.draw(gamescreen)
    all.update()
    
    pygame.display.flip() # Atualização da tela (porções da tela).

""" FINALIZAR JOGO """
pygame.quit()
quit()

