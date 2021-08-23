#importing modules
import pygame
import random
import math
from pygame import mixer
pygame.init()
#icon
score=0
level=1 
screen=pygame.display.set_mode((600,900))
pygame.display.set_caption("Raft Dodger")
icon=pygame.image.load("pygame\pirate-ship.png")
pygame.display.set_icon(icon)
#background
background=pygame.image.load("pygame\seabackground.png")
mixer.music.load('pygame\gbackground.wav')
mixer.music.play(-1)
#player
playerimg=pygame.image.load("pygame\pirate.png")
playerx=200
playery=800
playerxchang=0
playerychange=0
#enemy image
enemyimg=[]
enemyychange=[]
enemyx=[]
enemyy=[]
numenemys=5

#bullet
bulletimg=pygame.image.load("pygame\gun.png")
bulletx=0
bullety=800
bulletychange=10
bullet_State="ready"
#functions
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
def showbulletstate(x,y):
    bulletrender=font.render("bullet_State:"+bullet_State,True,(255,255,255))
    screen.blit(bulletrender,(x,y))
bulletrenderx=200
bulletrendery=10
def showschore(x,y):
    scorerender=font.render("score:"+str(score),True,(255,255,255))
    screen.blit(scorerender,(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(enemyimg,x,y):
    screen.blit(enemyimg,(x,y))
def firebullet(x,y):
    global bullet_State
    bullet_State="fire"
    screen.blit(bulletimg,(x,y))
def iscollision(enemyy,enemyx,bullety,bulletx):
    distance=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
    if distance<27:
        return True
    else:
        return False
def collisionplayer(enemyy,enemyx,playerx,playery):
      distance=math.sqrt(math.pow(enemyx-playerx,2)+math.pow(enemyy-playery,2))
      if distance<27:
        return True
      else:
        return False
#main loop
run=True
while run:
    for i in range(numenemys):
       enemyimg.append(pygame.image.load("pygame\enemy.png"))
       enemyx.append(random.randint(0,580))
       enemyy.append(random.randint(0,200))
       enemyychange.append(2)
    screen.blit(background,(0,0))#fills the background
    #events
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           run=False
       #right and left
       if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_LEFT:
               playerxchang=level*-5
           if event.key==pygame.K_RIGHT:
               playerxchang=level*5
           if event.key==pygame.K_SPACE:
               if bullet_State=="ready":
                 bulletsound=mixer.Sound('pygame\laser.wav')
                 bulletsound.play()
                 bulletx=playerx
                 firebullet(bulletx,bullety)
               
       if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_SPACE:
                playerxchang=0
                
   
    

    #boundaries
    playerx+=playerxchang
    if playerx<=0:
        playerx=0
    elif playerx>=540:
        playerx=540
    for i in range(numenemys):
        enemyy[i]+=enemyychange[i]
        if enemyy[i]<=0:
           enemyy[i]=0
        elif enemyy[i]>=859:
           enemyx[i]=random.randint(0,600)
           enemyy[i]=0
        collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:#collision between bullet and enemy
          
          explosion=mixer.Sound('pygame\explosion.wav')
          explosion.play()
          bullety=playery
          bullet_State="ready"
          score+=1
          print(score)
          enemyy[i]=0
          enemyx[i]=random.randint(0,580)
        if score==level*10:
          level+=1
          enemyychange[i]=level*2
          playerxchang=level-1
        collsionplayervar=collisionplayer(enemyy[i],enemyx[i],playerx,playery)
        if collsionplayervar:
             run=False
        enemy(enemyimg[i],enemyx[i],enemyy[i])
    #bulletmovement
    if bullety<=0:
        bullety=playery
        bullet_State="ready"
    if bullet_State == "fire":

      
        firebullet(bulletx,bullety)
        bullety-=bulletychange
    #collision

    #collsionplayer

    #displaying the pieces
    showbulletstate(bulletrenderx,bulletrendery)
    showschore(textx,texty)
    player(playerx,playery)
    pygame.display.update()