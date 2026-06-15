import pygame

pygame.init()

LARGEUR_GRILLE = 10
LONGEUR_GRILLE = 10
TAILLE_CASE = 40

LARGEUR_LABYRINTHE = TAILLE_CASE * LARGEUR_GRILLE
LONGEUR_LABYRINTHE = TAILLE_CASE * LONGEUR_GRILLE

ECRAN = pygame.display.set_mode((LONGEUR_LABYRINTHE, LARGEUR_LABYRINTHE))

labyrinthe = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, "S", 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, "E", 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

joueur_x = 40
joueur_y = 40

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Détection des touches du clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                joueur_x -= TAILLE_CASE
            if event.key == pygame.K_RIGHT:
                joueur_x += TAILLE_CASE
            if event.key == pygame.K_UP:
                joueur_y -= TAILLE_CASE
            if event.key == pygame.K_DOWN:
                joueur_y += TAILLE_CASE

    ECRAN.fill((255, 255, 255))

    y = 0
    for ligne in labyrinthe:
        x = 0
        for case in ligne:
            if case == 1:
                pygame.draw.rect(ECRAN, (0, 0, 0), (x, y, TAILLE_CASE, TAILLE_CASE))
            x += TAILLE_CASE
        y += TAILLE_CASE

    # Dessin du joueur (un carré rouge)
    pygame.draw.rect(ECRAN, (255, 0, 0), (joueur_x, joueur_y, TAILLE_CASE, TAILLE_CASE))

    pygame.display.flip()