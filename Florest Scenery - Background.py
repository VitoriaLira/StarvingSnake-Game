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

background = pygame.image.load("images/Cenário Floresta3D.png").convert() 
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
        self.rect.topleft = 700,120
        
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


"""IMPORTING ÁRVORE """

class Arvore1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arvore1 = pygame.image.load("images/arvore1.png")
        self.image = self.arvore1
        self.image = pygame.transform.scale(self.image,(300,400))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,300

obstaculos_floresta = pygame.sprite.Group()
arvore1 = Arvore1()
all.add(arvore1)
obstaculos_floresta.add(arvore1)


class Arvore2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arvore2 = pygame.image.load("images/arvore1.png")
        self.image = self.arvore2
        self.image = pygame.transform.scale(self.image,(300,400))

        self.rect = self.image.get_rect()
        self.rect.topleft = 1000,0

arvore2 = Arvore2()
all.add(arvore2)
obstaculos_floresta.add(arvore2)


""" IMPORTING ARBUSTO"""

class Arbusto1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto1 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto1
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 175,545

arbusto1 = Arbusto1()
all.add(arbusto1)
obstaculos_floresta.add(arbusto1)


class Arbusto2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto2 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto2
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 300,545

arbusto2 = Arbusto2()
all.add(arbusto2)
obstaculos_floresta.add(arbusto2)


class Arbusto3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto3 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto3
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 425,545

arbusto3 = Arbusto3()
all.add(arbusto3)
obstaculos_floresta.add(arbusto3)


class Arbusto4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto4 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto4
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 550,545

arbusto4 = Arbusto4()
all.add(arbusto4)
obstaculos_floresta.add(arbusto4)


class Arbusto5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto5 = pygame.image.load("images/arbusto2.png")
        self.image = self.arbusto5
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0

arbusto5 = Arbusto5()
all.add(arbusto5)
obstaculos_floresta.add(arbusto5)


class Arbusto6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto6 = pygame.image.load("images/arbusto2.png")
        self.image = self.arbusto6
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,125

arbusto6 = Arbusto6()
all.add(arbusto6)
obstaculos_floresta.add(arbusto6)


class Arbusto7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto7 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto7
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 500,0

arbusto7 = Arbusto7()
all.add(arbusto7)
obstaculos_floresta.add(arbusto7)


class Arbusto8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto8 = pygame.image.load("images/arbusto2.png")
        self.image = self.arbusto8
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 1200,505

arbusto8 = Arbusto8()
all.add(arbusto8)
obstaculos_floresta.add(arbusto8)


class Arbusto9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto9 = pygame.image.load("images/arbusto2.png")
        self.image = self.arbusto9
        self.image = pygame.transform.scale(self.image,(100,150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 1200,380

arbusto9 = Arbusto9()
all.add(arbusto9)
obstaculos_floresta.add(arbusto9)


class Arbusto10(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto10 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto10
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 625,0

arbusto10 = Arbusto10()
all.add(arbusto10)
obstaculos_floresta.add(arbusto10)


class Arbusto11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto11 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto11
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 675,545

arbusto11 = Arbusto11()
all.add(arbusto11)
obstaculos_floresta.add(arbusto11)

class Arbusto12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto12 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto12
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 800,545

arbusto12 = Arbusto12()
all.add(arbusto12)
obstaculos_floresta.add(arbusto12)


class Arbusto13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto13 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto13
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 925,545

arbusto13 = Arbusto13()
all.add(arbusto13)
obstaculos_floresta.add(arbusto13)


class Arbusto14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto14 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto14
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 1050,545

arbusto14 = Arbusto14()
all.add(arbusto14)
obstaculos_floresta.add(arbusto14)


class Arbusto15(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto15 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto15
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 750,0

arbusto15 = Arbusto15()
all.add(arbusto15)
obstaculos_floresta.add(arbusto15)


class Arbusto16(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto16 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto16
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 750,0

arbusto16 = Arbusto16()
all.add(arbusto16)
obstaculos_floresta.add(arbusto16)


class Arbusto17(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto17 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto17
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 875,0

arbusto17 = Arbusto17()
all.add(arbusto17)
obstaculos_floresta.add(arbusto17)


class Arbusto18(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto18 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto18
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 375,0

arbusto18 = Arbusto18()
all.add(arbusto18)
obstaculos_floresta.add(arbusto18)


class Arbusto19(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto19 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto19
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 250,0

arbusto19 = Arbusto19()
all.add(arbusto19)
obstaculos_floresta.add(arbusto19)


class Arbusto20(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto20 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto20
        self.image = pygame.transform.scale(self.image,(150,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 125,0

arbusto20 = Arbusto20()
all.add(arbusto20)
obstaculos_floresta.add(arbusto20)


""" IMPORTING BIRDS"""


class Bird2(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.bird2 = [pygame.image.load("images/passaro2.1.png"),pygame.image.load("images/passaro2.2.png"),pygame.image.load("images/passaro2.3.png"),pygame.image.load("images/passaro2.4.png"),pygame.image.load("images/passaro2.5.png")]
        self.currently = 0
        self.image = self.bird2[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,220

    def update(self):
        self.currently +=1
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        self.rect.x += 35

        if self.currently >= len(self.bird2):
            self.currently = 0
            
        self.image = self.bird2[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))

bird2 = Bird2()
all.add(bird2)
obstaculos_floresta.add(bird2)


class Bird1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.bird1 = [pygame.image.load("images/passaro1.1.png"),pygame.image.load("images/passaro1.2.png"),pygame.image.load("images/passaro1.3.png"),pygame.image.load("images/passaro1.4.png"),pygame.image.load("images/passaro1.5.png")]
        self.currently = 0
        self.image = self.bird1[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,350

    def update(self):
        self.currently +=1
        if self.rect.topright[0] < 0:
            self.rect.x = length
        self.rect.x -= 20

        if self.currently >= len(self.bird1):
            self.currently = 0
            
        self.image = self.bird1[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))

bird1 = Bird1()
all.add(bird1)
obstaculos_floresta.add(bird1)


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


    collides = pygame.sprite.spritecollide(snake,obstaculos_floresta,False)
        
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

