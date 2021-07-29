import pygame
from pygame.locals import *
from random import randrange

""" INICIALIZAR JOGO """
pygame.init() # Inicializa todas as funções e variáveis da biblioteca pygame.

""" CORES """
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
aqua = (20,255,255)
blue = (0,0,255)
forestgreen = (34,139,34)

""" CONFIGURAÇÕES DA TELA """
length = 1280
height = 650
score = 0
tamanho = 100

""" CENÁRIOS DO JOGO """
floresta = pygame.image.load("images/Cenário Floresta3D.png")
floresta = pygame.transform.scale(floresta,(length,height))

cidade = pygame.image.load("images/Cenário Cidade3D.png")
cidade = pygame.transform.scale(cidade,(length,height))

deserto = pygame.image.load("images/Cenário Deserto3D.png")
deserto = pygame.transform.scale(deserto,(length,height))

""" POSIÇÃO COBRA """
axis_x = length/2
axis_y = height/2

""" DEFINIÇÃO DE TELA """
gamescreen = pygame.display.set_mode((length,height)) #  Inicializa uma janela ou tela para exibição.
pygame.display.set_caption("Starving Snake") # Nome na janela do jogo.

""" FONTES DO JOGO """
textfont1 = pygame.font.SysFont('arial', 40, True, True)
textfont2 = pygame.font.SysFont('arial', 100, True, True)
textfont3 = pygame.font.SysFont('arial', 80, True, False)
textfont4 = pygame.font.SysFont('arial', 45, True, False)

""" IMPORTANDO MÚSICAS """
music = pygame.mixer.Sound("sounds/background_music.wav")
music.set_volume(0.2) # 0 até 1
 
score_sound = pygame.mixer.Sound("sounds/score.wav")
score_sound.set_volume(1) # 0 até 1

""" IMPORTANDO COBRA_FLORESTA """
class Snake1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes1 = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes1[self.currently]
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
            del self.snakes1[0:4]
            self.snakes1.append(pygame.image.load("back/snakeback_0.png"))
            self.snakes1.append(pygame.image.load("back/snakeback_1.png"))
            self.snakes1.append(pygame.image.load("back/snakeback_2.png"))
            #self.snakes = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png"),pygame.image.load("back/snakeback_2.png")]
            self.rect.y -= 50
            self.above = False
                    
        if self.below == True:
            del self.snakes1[0:4]
            self.snakes1.append(pygame.image.load("front/snakefront_0.png"))
            self.snakes1.append(pygame.image.load("front/snakefront_1.png"))
            #self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
            self.rect.y += 50
            self.below = False
 
        if self.east == True:
            del self.snakes1[0:4]
            self.snakes1.append(pygame.image.load("right/snakeright_0.png"))
            self.snakes1.append(pygame.image.load("right/snakeright_1.png"))
            #self.snakes = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
            self.rect.x += 50
            self.east = False
 
        if self.west == True:
            del self.snakes1[0:4]
            self.snakes1.append(pygame.image.load("left/snakeleft_0.png"))
            self.snakes1.append(pygame.image.load("left/snakeleft_1.png"))
            #self.snakes = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
            self.rect.x -= 50
            self.west = False
            
        if self.currently >= len(self.snakes1):
            self.currently = 0
        self.image = self.snakes1[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))

all_florest = pygame.sprite.Group()
all_city = pygame.sprite.Group()
all_desert = pygame.sprite.Group()
gp_maca = pygame.sprite.Group()
gp_lagartixa = pygame.sprite.Group()
gp_rato = pygame.sprite.Group()

snake1 = Snake1()
all_florest.add(snake1)

""" IMPORTANDO COBRA_CIDADE """
class Snake2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes2 = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes2[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 565,0
        
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
            del self.snakes2[0:4]
            self.snakes2.append(pygame.image.load("back/snakeback_0.png"))
            self.snakes2.append(pygame.image.load("back/snakeback_1.png"))
            self.snakes2.append(pygame.image.load("back/snakeback_2.png"))
            #self.snakes = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png"),pygame.image.load("back/snakeback_2.png")]
            self.rect.y -= 50
            self.above = False
                    
        if self.below == True:
            del self.snakes2[0:4]
            self.snakes2.append(pygame.image.load("front/snakefront_0.png"))
            self.snakes2.append(pygame.image.load("front/snakefront_1.png"))
            #self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
            self.rect.y += 50
            self.below = False
 
        if self.east == True:
            del self.snakes2[0:4]
            self.snakes2.append(pygame.image.load("right/snakeright_0.png"))
            self.snakes2.append(pygame.image.load("right/snakeright_1.png"))
            #self.snakes = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
            self.rect.x += 50
            self.east = False
 
        if self.west == True:
            del self.snakes2[0:4]
            self.snakes2.append(pygame.image.load("left/snakeleft_0.png"))
            self.snakes2.append(pygame.image.load("left/snakeleft_1.png"))
            #self.snakes = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
            self.rect.x -= 50
            self.west = False
            
        if self.currently >= len(self.snakes2):
            self.currently = 0
        self.image = self.snakes2[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))

snake2 = Snake2()
all_city.add(snake2)

""" IMPORTANDO COBRA_DESERTO """
class Snake3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes3 = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes3[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 650,120
        
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
            del self.snakes3[0:4]
            self.snakes3.append(pygame.image.load("back/snakeback_0.png"))
            self.snakes3.append(pygame.image.load("back/snakeback_1.png"))
            self.snakes3.append(pygame.image.load("back/snakeback_2.png"))
            #self.snakes = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png"),pygame.image.load("back/snakeback_2.png")]
            self.rect.y -= 50
            self.above = False
                    
        if self.below == True:
            del self.snakes3[0:4]
            self.snakes3.append(pygame.image.load("front/snakefront_0.png"))
            self.snakes3.append(pygame.image.load("front/snakefront_1.png"))
            #self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
            self.rect.y += 50
            self.below = False
 
        if self.east == True:
            del self.snakes3[0:4]
            self.snakes3.append(pygame.image.load("right/snakeright_0.png"))
            self.snakes3.append(pygame.image.load("right/snakeright_1.png"))
            #self.snakes = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
            self.rect.x += 50
            self.east = False
 
        if self.west == True:
            del self.snakes3[0:4]
            self.snakes3.append(pygame.image.load("left/snakeleft_0.png"))
            self.snakes3.append(pygame.image.load("left/snakeleft_1.png"))
            #self.snakes = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
            self.rect.x -= 50
            self.west = False
            
        if self.currently >= len(self.snakes3):
            self.currently = 0
        self.image = self.snakes3[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))
        
snake3 = Snake3()
all_desert.add(snake3)

""" IMPORTANDO MAÇÃ """
class Maca1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        maca1 = pygame.image.load("images/maca1.png")
        self.image = maca1
        self.image = pygame.transform.scale(self.image,(25*2,25*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 950,120
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30

apple1 = Maca1()
all_florest.add(apple1)
all_city.add(apple1)
all_desert.add(apple1)
gp_maca.add(apple1)

""" IMPORTANDO LAGARTIXA """
class Lagartixa1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        lagartixa1 = pygame.image.load("images/lagartixa1.png")
        self.image = lagartixa1
        self.image = pygame.transform.scale(self.image,(34*2,34*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 275,120
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30

gecko1 = Lagartixa1()
all_florest.add(gecko1)
all_city.add(gecko1)
all_desert.add(gecko1)
gp_lagartixa.add(gecko1)

""" IMPORTANDO RATO """
class Rato1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        rato1 = pygame.image.load("images/rato1.png")
        self.image = rato1
        self.image = pygame.transform.scale(self.image,(27*2,27*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,400
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30

rat1 = Rato1()
all_florest.add(rat1)
all_city.add(rat1)
all_desert.add(rat1)
gp_rato.add(rat1)

""" IMPORTANDO ÁRVORES """
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
all_florest.add(arvore1)
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
all_florest.add(arvore2)
obstaculos_floresta.add(arvore2)
 
""" IMPORTANDO ARBUSTOS """
class Arbusto1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto1 = pygame.image.load("images/arbusto.png")
        self.image = self.arbusto1
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 175,545
 
arbusto1 = Arbusto1()
all_florest.add(arbusto1)
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
all_florest.add(arbusto2)
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
all_florest.add(arbusto3)
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
all_florest.add(arbusto4)
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
all_florest.add(arbusto5)
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
all_florest.add(arbusto6)
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
all_florest.add(arbusto7)
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
all_florest.add(arbusto8)
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
all_florest.add(arbusto9)
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
all_florest.add(arbusto10)
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
all_florest.add(arbusto11)
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
all_florest.add(arbusto12)
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
all_florest.add(arbusto13)
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
all_florest.add(arbusto14)
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
all_florest.add(arbusto15)
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
all_florest.add(arbusto16)
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
all_florest.add(arbusto17)
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
all_florest.add(arbusto18)
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
all_florest.add(arbusto19)
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
all_florest.add(arbusto20)
obstaculos_floresta.add(arbusto20)
 
""" IMPORTANDO PÁSSAROS """
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
all_florest.add(bird2)
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
all_florest.add(bird1)
obstaculos_floresta.add(bird1)

""" IMPORTANDO CARROS """
class Carro1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        carro1 = pygame.image.load("images/carro1.png")
        self.image = carro1
        self.image = pygame.transform.scale(self.image,(400,150))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,300
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        self.rect.x += 20
 
obstaculos_cidade = pygame.sprite.Group()
car1 = Carro1()
all_city.add(car1)
obstaculos_cidade.add(car1)

class Carro2(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        carro2 = pygame.image.load("images/carro2.png")
        self.image = carro2
        self.image = pygame.transform.scale(self.image,(400,150))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,420
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        self.rect.x += 30
 
car2 = Carro2()
all_city.add(car2)
obstaculos_cidade.add(car2)

""" IMPORTANDO PESSOA E GATO """
class People(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.pessoa = [pygame.image.load("images/pessoa2.png"),pygame.image.load("images/pessoa3.png"),pygame.image.load("images/pessoa4.png"),pygame.image.load("images/pessoa5.png")]
        self.currently = 0
        self.image = self.pessoa[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,430
 
    def update(self):
        self.currently = self.currently + 1
        if self.rect.topright[0] < 0:
            self.rect.x = length
        self.rect.x -= 20
 
        if self.currently >= len(self.pessoa):
            self.currently = 0
        self.image = self.pessoa[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
 
people = People()
all_city.add(people)
obstaculos_cidade.add(people)
 
class Gato(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.gato = [pygame.image.load("images/gato0.png"),pygame.image.load("images/gato1.png"),pygame.image.load("images/gato2.png")]
        self.currently = 0
        self.image = self.gato[self.currently]
        self.image = pygame.transform.scale(self.image,(33*2,33*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 230,230
 
    def update(self):
        self.currently = self.currently + 1
        if self.rect.topright[0] > length:
            self.rect.x = 0
        self.rect.x += 20
 
        if self.currently >= len(self.gato):
            self.currently = 0
        self.image = self.gato[self.currently]
        self.image = pygame.transform.scale(self.image,(33*2,33*2))
 
gato = Gato()
all_city.add(gato)
obstaculos_cidade.add(gato)

""" IMPORTANDO CACTO """
class Cacto1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto1 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto1
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0
        
obstaculos_deserto = pygame.sprite.Group()
cacto1 = Cacto1()
all_desert.add(cacto1)
obstaculos_deserto.add(cacto1)

class Cacto11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto11 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto11
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 1200,0
        
cacto11 = Cacto11()
all_desert.add(cacto11)
obstaculos_deserto.add(cacto11)

class Cacto12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto12 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto12
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,height - 100
        
cacto12 = Cacto12()
all_desert.add(cacto12)
obstaculos_deserto.add(cacto12)
 
class Cacto13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto13 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto13
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 1200,height - 100
        
cacto13 = Cacto13()
all_desert.add(cacto13)
obstaculos_deserto.add(cacto13)
 
class Cacto2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto2 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto2
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0 + 100
        
cacto2 = Cacto2()
all_desert.add(cacto2)
obstaculos_deserto.add(cacto2)
 
class Cacto21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto21 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto21
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 300,0
        
cacto21 = Cacto21()
all_desert.add(cacto21)
obstaculos_deserto.add(cacto21)
 
class Cacto22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto22 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto22
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 400,0
        
cacto22 = Cacto22()
all_desert.add(cacto22)
obstaculos_deserto.add(cacto22)
 
class Cacto23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto23 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto23
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 600,0
        
cacto23 = Cacto23()
all_desert.add(cacto23)
obstaculos_deserto.add(cacto23)
 
class Cacto24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto24 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto24
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 700,0
        
cacto24 = Cacto24()
all_desert.add(cacto24)
obstaculos_deserto.add(cacto24)
 
class Cacto25(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto25 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto25
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 900,0
        
cacto25 = Cacto25()
all_desert.add(cacto25)
obstaculos_deserto.add(cacto25)

class Cacto26(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto26 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto26
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 1000,0

cacto26 = Cacto26()
all_desert.add(cacto26)
obstaculos_deserto.add(cacto26)

class Cacto27(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto27 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto27
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0 + 200

cacto27 = Cacto27()
all_desert.add(cacto27)
obstaculos_deserto.add(cacto27)

class Cacto28(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto28 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto28
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0 + 325

cacto28 = Cacto28()
all_desert.add(cacto28)
obstaculos_deserto.add(cacto28)

class Cacto29(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto29 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto29
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0 + 450

cacto29 = Cacto29()
all_desert.add(cacto29)
obstaculos_deserto.add(cacto29)

class Cacto30(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto30 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto30
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 300,height - 100

cacto30 = Cacto30()
all_desert.add(cacto30)
obstaculos_deserto.add(cacto30)

class Cacto31(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto31 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto31
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0 + 100

cacto31 = Cacto31()
all_desert.add(cacto31)
obstaculos_deserto.add(cacto31)

class Cacto32(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto32 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto32
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0 + 200

cacto32 = Cacto32()
all_desert.add(cacto32)
obstaculos_deserto.add(cacto32)

class Cacto33(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto33 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto33
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0 + 325

cacto33 = Cacto33()
all_desert.add(cacto33)
obstaculos_deserto.add(cacto33)

class Cacto34(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto34 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto34
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0 + 450

cacto34 = Cacto34()
all_desert.add(cacto34)
obstaculos_deserto.add(cacto34)

class Cacto35(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto35 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto35
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 400,height - 100

cacto35 = Cacto35()
all_desert.add(cacto35)
obstaculos_deserto.add(cacto35)

class Cacto36(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto36 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto36
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 600,height - 100

cacto36 = Cacto36()
all_desert.add(cacto36)
obstaculos_deserto.add(cacto36)

class Cacto37(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto37 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto37
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 700,height - 100

cacto37 = Cacto37()
all_desert.add(cacto37)
obstaculos_deserto.add(cacto37)

class Cacto38(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto38 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto38
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 900,height - 100

cacto38 = Cacto38()
all_desert.add(cacto38)
obstaculos_deserto.add(cacto38)

class Cacto39(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto39 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto39
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 1000,height - 100

cacto39 = Cacto39()
all_desert.add(cacto39)
obstaculos_deserto.add(cacto39)

""" IMPORTANDO ESCORPIÃO"""
class Escorpiao1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao1 = pygame.image.load("images/escorpião1.png")
        self.image = self.escorpiao1
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 500,0
 
    def update(self):
        if self.rect.bottom > height:
            self.rect.y = 0
        self.rect.y += 20
        self.image = self.escorpiao1
        self.image = pygame.transform.scale(self.image,(64,64))
    
escorpiao1 = Escorpiao1()
all_desert.add(escorpiao1)
obstaculos_deserto.add(escorpiao1)
 
class Escorpiao2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao2 = pygame.image.load("images/escorpião1.png")
        self.image = self.escorpiao2
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 800, 550
 
    def update(self):
        if self.rect.bottom < 0:
            self.rect.y = height
        self.rect.y -= 20
        self.image = self.escorpiao2
        self.image = pygame.transform.scale(self.image,(64,64))
    
escorpiao2 = Escorpiao2()
all_desert.add(escorpiao2)
obstaculos_deserto.add(escorpiao2)

class Escorpiao3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao3 = pygame.image.load("images/escorpião1.png")
        self.image = self.escorpiao3
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 200,0
 
    def update(self):
        if self.rect.bottom > height:
            self.rect.y = 0
        self.rect.y += 10
        self.image = self.escorpiao3
        self.image = pygame.transform.scale(self.image,(64,64))
    
escorpiao3 = Escorpiao3()
all_desert.add(escorpiao3)
obstaculos_deserto.add(escorpiao3)

class Escorpiao4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao4 = pygame.image.load("images/escorpião1.png")
        self.image = self.escorpiao4
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 1100, 550
 
    def update(self):
        if self.rect.bottom < 0:
            self.rect.y = height
        self.rect.y -= 10
        self.image = self.escorpiao4
        self.image = pygame.transform.scale(self.image,(64,64))
    
escorpiao4 = Escorpiao4()
all_desert.add(escorpiao4)
obstaculos_deserto.add(escorpiao4)

""" DEFINIÇÃO DO LOOP """
time = pygame.time.Clock() # Relógio do FPS.

play_screen = True
while play_screen:
    gamescreen.fill(forestgreen) # Cor de fundo da tela.

    text = ("Starving Snake")
    ftext = textfont2.render(text, True, white)
    gamescreen.blit(ftext, (280,40)) # Exibir o texto na tela.

    pygame.draw.rect(gamescreen, (blue), (460,290,360,100))
    text0 = ("Play")
    ftext0 = textfont3.render(text0, True, white)
    gamescreen.blit(ftext0, (560,293))

    for choice in pygame.event.get():
        if choice.type == QUIT:
            play_screen = False

        if choice.type == pygame.MOUSEBUTTONDOWN: # Eventos no mouse.
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            game_mode = True
            """ BOTÃO PLAY """
            if x > 460 and y > 290 and x < 820 and y < 390:

                """ LOOP DO MODO DE JOGO """
                while game_mode:
                    gamescreen.fill(forestgreen) # Cor de fundo da tela.

                    text1 = ("Starving Snake")
                    ftext1 = textfont2.render(text1, True, white)
                    gamescreen.blit(ftext1, (280,40)) # Exibir o texto na tela.

                    pygame.draw.rect(gamescreen, (blue), (495,230,230,80))
                    text2 = ("Fácil")
                    ftext2 = textfont4.render(text2, True, white)
                    gamescreen.blit(ftext2, (560,243))

                    pygame.draw.rect(gamescreen, (blue), (495,360,230,80))
                    text3 = ("Médio")
                    ftext3 = textfont4.render(text3, True, white)
                    gamescreen.blit(ftext3, (550,373))

                    pygame.draw.rect(gamescreen, (blue), (495,490,230,80))
                    text4 = ("Difícil")
                    ftext4 = textfont4.render(text4, True, white)
                    gamescreen.blit(ftext4, (555,503))

                    for choice in pygame.event.get():
                        if choice.type == QUIT:
                            game_mode = False
                            play_screen = False
                        
                        if choice.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]

                            game_scenery = True
                            """ BOTÃO FÁCIL """
                            if x > 495 and y > 230 and x < 725 and y < 310:

                                """ LOOP DOS CENÁRIOS """
                                while game_scenery:
                                    gamescreen.fill(forestgreen) # Cor de fundo da tela.

                                    text1 = ("Starving Snake")
                                    ftext1 = textfont2.render(text1, True, white)
                                    gamescreen.blit(ftext1, (280,40)) # Exibir o texto na tela.

                                    pygame.draw.rect(gamescreen, (blue), (495,230,230,80))
                                    text2 = ("Floresta")
                                    ftext2 = textfont4.render(text2, True, white)
                                    gamescreen.blit(ftext2, (525,243))

                                    pygame.draw.rect(gamescreen, (blue), (495,360,230,80))
                                    text3 = ("Cidade")
                                    ftext3 = textfont4.render(text3, True, white)
                                    gamescreen.blit(ftext3, (533,373))

                                    pygame.draw.rect(gamescreen, (blue), (495,490,230,80))
                                    text4 = ("Deserto")
                                    ftext4 = textfont4.render(text4, True, white)
                                    gamescreen.blit(ftext4, (525,503))

                                    for choice in pygame.event.get():
                                        if choice.type == QUIT:
                                            game_scenery = False
                                            game_mode = False
                                            play_screen = False

                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                            x = pygame.mouse.get_pos()[0]
                                            y = pygame.mouse.get_pos()[1]

                                            OFF = True
                                            """ BOTÃO FLORESTA """
                                            if x > 495 and y > 230 and x < 725 and y < 310:

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)
                                                
                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(5)
                                                    gamescreen.fill(white)
                        
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake1.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake1.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake1.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake1.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake1.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake1.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake1.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake1.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides1 = pygame.sprite.spritecollide(snake1,obstaculos_floresta,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake1,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake1,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake1,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides1:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                                
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake1.rect.topleft = 700,120
                                                                score = 0

                                                                gamescreen.blit(floresta,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_florest.draw(gamescreen)
                                                                all_florest.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                    
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake1.rect.topleft = 700,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True                                            

                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(floresta, (0,0))
                                                        all_florest.draw(gamescreen)
                                                        all_florest.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(5)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake2.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake2.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake2.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake2.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake2.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake2.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake2.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake2.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake2,obstaculos_cidade,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake2,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake2,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake2,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides2:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake2.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_city.draw(gamescreen)
                                                                all_city.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake2.rect.topleft = 565,0
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    

                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(cidade, (0,0))
                                                        all_city.draw(gamescreen)
                                                        all_city.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(5)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake3.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake3.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake3.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake3.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake3.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake3.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake3.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake3.left()
                                                                #x -= 20 #LEFT
                                                
                                                    obstacle_collides3 = pygame.sprite.spritecollide(snake3,obstaculos_deserto,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake3,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake3,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake3,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides3:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))
                                                        
                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake3.rect.topleft = 650,120
                                                                score = 0

                                                                gamescreen.blit(deserto,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_desert.draw(gamescreen)
                                                                all_desert.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake3.rect.topleft = 650,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(deserto, (0,0))
                                                        all_desert.draw(gamescreen)
                                                        all_desert.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                    pygame.display.update() # Atualização da tela (porções da tela).

                            """ BOTÃO MÉDIO """
                            if x > 495 and y > 360 and x < 725 and y < 440:

                                """ LOOP DOS CENÁRIOS """
                                while game_scenery:
                                    gamescreen.fill(forestgreen) # Cor de fundo da tela.

                                    text1 = ("Starving Snake")
                                    ftext1 = textfont2.render(text1, True, white)
                                    gamescreen.blit(ftext1, (280,40)) # Exibir o texto na tela.

                                    pygame.draw.rect(gamescreen, (blue), (495,230,230,80))
                                    text2 = ("Floresta")
                                    ftext2 = textfont4.render(text2, True, white)
                                    gamescreen.blit(ftext2, (525,243))

                                    pygame.draw.rect(gamescreen, (blue), (495,360,230,80))
                                    text3 = ("Cidade")
                                    ftext3 = textfont4.render(text3, True, white)
                                    gamescreen.blit(ftext3, (533,373))

                                    pygame.draw.rect(gamescreen, (blue), (495,490,230,80))
                                    text4 = ("Deserto")
                                    ftext4 = textfont4.render(text4, True, white)
                                    gamescreen.blit(ftext4, (525,503))

                                    for choice in pygame.event.get():
                                        if choice.type == QUIT:
                                            game_scenery = False
                                            game_mode = False
                                            play_screen = False
                                            
                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                            x = pygame.mouse.get_pos()[0]
                                            y = pygame.mouse.get_pos()[1]

                                            game_over = False
                                            OFF = True
                                            """ BOTÃO FLORESTA """
                                            if x > 495 and y > 230 and x < 725 and y < 310:

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(10)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake1.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake1.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake1.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake1.left()
                                                
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake1.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake1.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake1.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake1.left()
                                                                #x -= 20 #LEFT
                                            
                                                    obstacle_collides1 = pygame.sprite.spritecollide(snake1,obstaculos_floresta,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake1,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake1,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake1,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides1:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                                
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake1.rect.topleft = 700,120
                                                                score = 0

                                                                gamescreen.blit(floresta,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_florest.draw(gamescreen)
                                                                all_florest.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                    
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake1.rect.topleft = 700,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True                                            

                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(floresta, (0,0))
                                                        all_florest.draw(gamescreen)
                                                        all_florest.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:
                                                
                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(10)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake2.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake2.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake2.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake2.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake2.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake2.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake2.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake2.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake2,obstaculos_cidade,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake2,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake2,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake2,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides2:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake2.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_city.draw(gamescreen)
                                                                all_city.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake2.rect.topleft = 565,0
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(cidade, (0,0))
                                                        all_city.draw(gamescreen)
                                                        all_city.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:
                                                
                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(10)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake3.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake3.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake3.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake3.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake3.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake3.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake3.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake3.left()
                                                                #x -= 20 #LEFT
                                                
                                                    obstacle_collides3 = pygame.sprite.spritecollide(snake3,obstaculos_deserto,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake3,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake3,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake3,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides3:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))
                                                        
                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake3.rect.topleft = 650,120
                                                                score = 0

                                                                gamescreen.blit(deserto,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_desert.draw(gamescreen)
                                                                all_desert.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake3.rect.topleft = 650,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(deserto, (0,0))
                                                        all_desert.draw(gamescreen)
                                                        all_desert.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                    pygame.display.update() # Atualização da tela (porções da tela).

                            """ BOTÃO DIFÍCIL """
                            if x > 495 and y > 490 and x < 725 and y < 570:

                                """ LOOP DOS CENÁRIOS """
                                while game_scenery:
                                    gamescreen.fill(forestgreen) # Cor de fundo da tela.

                                    text1 = ("Starving Snake")
                                    ftext1 = textfont2.render(text1, True, white)
                                    gamescreen.blit(ftext1, (280,40)) # Exibir o texto na tela.

                                    pygame.draw.rect(gamescreen, (blue), (495,230,230,80))
                                    text2 = ("Floresta")
                                    ftext2 = textfont4.render(text2, True, white)
                                    gamescreen.blit(ftext2, (525,243))

                                    pygame.draw.rect(gamescreen, (blue), (495,360,230,80))
                                    text3 = ("Cidade")
                                    ftext3 = textfont4.render(text3, True, white)
                                    gamescreen.blit(ftext3, (533,373))

                                    pygame.draw.rect(gamescreen, (blue), (495,490,230,80))
                                    text4 = ("Deserto")
                                    ftext4 = textfont4.render(text4, True, white)
                                    gamescreen.blit(ftext4, (525,503))

                                    for choice in pygame.event.get():
                                        if choice.type == QUIT:
                                            game_scenery = False
                                            game_mode = False
                                            play_screen = False
                                            
                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                            x = pygame.mouse.get_pos()[0]
                                            y = pygame.mouse.get_pos()[1]

                                            game_over = False
                                            OFF = True
                                            """ BOTÃO FLORESTA """
                                            if x > 495 and y > 230 and x < 725 and y < 310:

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(15)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake1.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake1.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake1.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake1.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake1.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake1.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake1.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake1.left()
                                                                #x -= 20 #LEFT
                                            
                                                    obstacle_collides1 = pygame.sprite.spritecollide(snake1,obstaculos_floresta,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake1,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake1,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake1,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides1:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                                
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake1.rect.topleft = 700,120
                                                                score = 0

                                                                gamescreen.blit(floresta,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_florest.draw(gamescreen)
                                                                all_florest.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                    
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake1.rect.topleft = 700,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(floresta, (0,0))
                                                        all_florest.draw(gamescreen)
                                                        all_florest.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:
                                                
                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(15)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake2.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake2.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake2.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake2.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake2.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake2.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake2.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake2.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake2,obstaculos_cidade,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake2,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake2,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake2,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides2:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)
                                                                
                                                                OFF = True
                                                                snake2.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_city.draw(gamescreen)
                                                                all_city.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake2.rect.topleft = 565,0
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(cidade, (0,0))
                                                        all_city.draw(gamescreen)
                                                        all_city.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:
                                                
                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(15)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake3.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake3.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake3.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake3.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake3.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake3.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake3.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake3.left()
                                                                #x -= 20 #LEFT
                                                
                                                    obstacle_collides3 = pygame.sprite.spritecollide(snake3,obstaculos_deserto,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake3,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake3,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake3,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides3:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))
                                                        
                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake3.rect.topleft = 650,120
                                                                score = 0

                                                                gamescreen.blit(deserto,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_desert.draw(gamescreen)
                                                                all_desert.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake3.rect.topleft = 650,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(deserto, (0,0))
                                                        all_desert.draw(gamescreen)
                                                        all_desert.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()
                    
                                    pygame.display.update()
                    
                    pygame.display.update()

    time.tick(0.5) # FPS
    pygame.display.update()

""" FINALIZAR JOGO """
pygame.quit()
quit()
