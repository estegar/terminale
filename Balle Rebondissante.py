import pygame, sys
import time
from random import randint
from pygame.locals import *

FPS = 120
clock = pygame.time.Clock()
ecran = (640, 480)
vitesse = 5
pygame.display.init()
fenetre = pygame.display.set_mode((ecran[0], ecran[1]))
fenetre.fill([0, 0, 0])


class balle:
    def __init__(self, couleur, taille):
        self.couleur = couleur
        self.x = randint(10, 630)
        self.y = randint(10, 470)
        self.dx = randint(-5, 5)
        self.dy = randint(-5, 5)
        self.taille = taille
        self.s = 1
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.taille)

    def afficher(self):
        print(self.s)
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.taille)
        self.x += self.dx
        self.y += self.dy
        if self.x > ecran[0] - 15 or self.x < 0 + 10:
            self.dx = -self.dx
        if self.y > ecran[1] - 10 or self.y < 0 + 10:
            self.dy = -self.dy
        for balles in listeBalles:
            if balles.couleur == (randint(10,255), 255, 0) or self.couleur == (0, 255, 0):
                if self.x != balles.x and self.y != balles.y:
                    if (((self.x - balles.x) ** 2 + (self.y - balles.y) ** 2) ** 0.5) < 20:
                        if self.x > balles.x:
                            self.dx = vitesse
                            self.dy = vitesse
                            balles.dx = -vitesse
                            balles.dy = -vitesse


listeBalles = [balle((0, 255, 0), 10) for i in range(1)]

while True:

    fenetre.fill([0, 0, 0])

    for i in range(len(listeBalles)):
        listeBalles[i].afficher()

    clock.tick(FPS)
    pygame.display.flip()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()

    time.sleep(0.01)
