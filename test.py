import pygame
import sys

# 1. On démarre Pygame et on crée une petite fenêtre
pygame.init()
fenetre = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Déplacement Pygame")

# 2. Nos variables de position de départ
x = 200
y = 200
taille_perso = 20  # Largeur et hauteur de notre carré

# Pour contrôler la vitesse du jeu
horloge = pygame.time.Clock()

# Boucle de jeu principale
while True:
    # Sécurité : Permet de fermer la fenêtre proprement
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Récupération des touches enfoncées
    touches = pygame.key.get_pressed()

    # Déplacements verticaux
    if touches[pygame.K_UP]:
        y -= 2
    if touches[pygame.K_DOWN]:
        y += 2

    # CORRECTION : Remplissage des mouvements horizontaux
    if touches[pygame.K_LEFT]:
        x -= 2
    if touches[pygame.K_RIGHT]:
        x += 2

    # 3. AFFICHAGE GRAPHIQUE (Ajouté pour voir le résultat)
    # On remplit l'écran de noir pour effacer l'image précédente
    fenetre.fill((0, 0, 0))

    # On dessine un carré rouge à la position (x, y)
    pygame.draw.rect(fenetre, (255, 0, 0), (x, y, taille_perso, taille_perso))

    # On actualise l'affichage de la fenêtre
    pygame.display.flip()

    # 4. On affiche la position dans la console
    print(f"Position actuelle : ({x}, {y})")

    # Limite à 60 images par seconde
    horloge.tick(60)