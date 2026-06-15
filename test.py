import pygame
import sys

# 1. On démarre Pygame et on crée une petite fenêtre (obligatoire pour capter le clavier)
pygame.init()
fenetre = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Déplacement Pygame")

# 2. Nos variables de position de départ
x = 200
y = 200

# Pour contrôler la vitesse du jeu
horloge = pygame.time.Clock()

# Boucle de jeu principale
while True:
    # Sécurité : Permet de fermer la fenêtre proprement si on clique sur la croix rouge
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 3. ON DETECTE LES TOUCHES ENFONCÉES
    touches = pygame.key.get_pressed()

    if touches[pygame.K_UP]:       # Si la flèche HAUT est enfoncée
        y -= 2                     # Note : Dans Pygame, aller vers le haut, c'est DIMINUER 'y' !
    if touches[pygame.K_DOWN]:     # Si la flèche BAS est enfoncée
        y += 2
    if touches[pygame.K_LEFT]:     # Si la flèche GAUCHE est enfoncée
        x -= 2
    if touches[pygame.K_RIGHT]:    # Si la flèche DROITE est enfoncée
        x += 2

    # 4. On affiche la position dans la console pour voir si ça marche
    print(f"Position actuelle : ({x}, {y})")

    # On limite le jeu à 60 calculs par seconde (ça remplace le 'time.sleep' d'avant)
    horloge.tick(60)