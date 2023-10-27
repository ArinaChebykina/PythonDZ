import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 50
sc = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Тараканьи бега")
clock = pygame.time.Clock()


black = (0, 0, 0)
white = (255, 255, 255)
orange = (225, 133, 65)
gold = (218, 165, 32)
grey = (168, 168, 168)
darkgrey = (128, 128, 128)

x1 = x2 = x3 = x4 = x5 = 50
y1 = 70
y2 = 160
y3 = 250
y4 = 340
y5 = 430
vx = 50
s = 90
e = 400
finished = False

sc.fill(white)
pygame.draw.rect(sc, black, (530, 20, 20, 460),1)
for a in range(20, 480, 20):
    pygame.draw.rect(sc, black, (530, a, 10, 10))
    pygame.draw.rect(sc, black, (540, a+10, 10, 10))
pygame.draw.circle(sc, orange, (int(x1), int(y1)), 35)
pygame.draw.circle(sc, orange, (int(x2), int(y2)), 35)
pygame.draw.circle(sc, orange, (int(x3), int(y3)), 35)
pygame.draw.circle(sc, orange, (int(x4), int(y4)), 35)
pygame.draw.circle(sc, orange, (int(x5), int(y5)), 35)
bw = 100
bh = 50
bx = 300
by = 500
pygame.draw.rect(sc, grey, (bx, by, bw, bh))
pygame.draw.rect(sc, darkgrey, (bx, by, bw, bh), 2)
                
pygame.display.update()
                    
                

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONUP:
            mp = pygame.mouse.get_pos()
            if bx<=mp[0]<=bx+bw and by<=mp[1]<=by+bh:
                while x1<550 and x2<550 and x3<550 and x4<550 and x5<550:
                    dt1 = clock.tick(FPS)/(randint(s, e))
                    dt2 = clock.tick(FPS)/(randint(s, e))
                    dt3 = clock.tick(FPS)/(randint(s, e))
                    dt4 = clock.tick(FPS)/(randint(s, e))
                    dt5 = clock.tick(FPS)/(randint(s, e))

                    x1+=vx*dt1
                    x2+=vx*dt2
                    x3+=vx*dt3
                    x4+=vx*dt4
                    x5+=vx*dt5

                    sc.fill(white)
                    pygame.draw.rect(sc, black, (530, 20, 20, 460),1)
                    for a in range(20, 480, 20):
                        pygame.draw.rect(sc, black, (530, a, 10, 10))
                        pygame.draw.rect(sc, black, (540, a+10, 10, 10))
                    
                    pygame.draw.circle(sc, orange, (int(x1), int(y1)), 35)
                    pygame.draw.circle(sc, orange, (int(x2), int(y2)), 35)
                    pygame.draw.circle(sc, orange, (int(x3), int(y3)), 35)
                    pygame.draw.circle(sc, orange, (int(x4), int(y4)), 35)
                    pygame.draw.circle(sc, orange, (int(x5), int(y5)), 35)
                    
                    pygame.display.update()
          
    if x1>=550:
        pygame.draw.polygon(sc, gold, ((620, int(y1+20)), (620, int(y1-20)), (630, int(y1-5)), (640, int(y1-20)), (650, int(y1-5)), (660, int(y1-20)), (660, int(y1+20))))
    if x2>=550:
        pygame.draw.polygon(sc, gold, ((620, int(y2+20)), (620, int(y2-20)), (630, int(y2-5)), (640, int(y2-20)), (650, int(y2-5)), (660, int(y2-20)), (660, int(y2+20))))
    if x3>=550:
        pygame.draw.polygon(sc, gold, ((620, int(y3+20)), (620, int(y3-20)), (630, int(y3-5)), (640, int(y3-20)), (650, int(y3-5)), (660, int(y3-20)), (660, int(y3+20))))
    if x4>=550:
        pygame.draw.polygon(sc, gold, ((620, int(y4+20)), (620, int(y4-20)), (630, int(y4-5)), (640, int(y4-20)), (650, int(y4-5)), (660, int(y4-20)), (660, int(y4+20))))
    if x5>=550:
        pygame.draw.polygon(sc, gold, ((620, int(y5+20)), (620, int(y5-20)), (630, int(y5-5)), (640, int(y5-20)), (650, int(y5-5)), (660, int(y5-20)), (660, int(y5+20))))
        
    pygame.display.update()

pygame.quit()
