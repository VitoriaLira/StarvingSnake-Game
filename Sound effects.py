import pygame
from pygame.locals import  * 
from time import sleep

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

background = pygame.image.load("images/Cenário Cidade3D.png").convert() 
background = pygame.transform.scale(background,(1280,650)) 


""" IMPORTING THE BACKGROUND MUSIC """

music = pygame.mixer.Sound("sounds/background_music.wav")
music.play(-1) # -1 Para que recomece a música após o término.
music.set_volume(0.2) # 0 até 1


score = pygame.mixer.Sound("sounds/score.wav")
score.play()
score.set_volume(1) # 0 até 1


collision = pygame.mixer.Sound("sounds/collision.wav")
collision.set_volume(1) # 0 até 1


gameover = pygame.mixer.Sound("sounds/gameover.wav")
gameover.set_volume(1) # 0 até 1


""" IMPORTING THE SNAKE """

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes[self.currently]
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


""" IMPORTING THE CARS """

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
all.add(car1)
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
all.add(car2)
obstaculos_cidade.add(car2)

""" IMPORTING PEOPLE """

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
all.add(people)
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
all.add(gato)
obstaculos_cidade.add(gato)



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


    collides = pygame.sprite.spritecollide(snake,obstaculos_cidade,False)
        
    if collides:
        music.set_volume(0)
        collision.play()
        sleep(1)
        gameover.play()
        sleep(3)
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

