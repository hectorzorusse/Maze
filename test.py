import pygame

pygame.init()

LARGEUR_GRILLE = 15
LONGEUR_GRILLE = 15
TAILLE_CASE = 40

LARGEUR_LABYRINTHE = TAILLE_CASE * LARGEUR_GRILLE
LONGEUR_LABYRINTHE = TAILLE_CASE * LONGEUR_GRILLE

ECRAN = pygame.display.set_mode((LONGEUR_LABYRINTHE, LARGEUR_LABYRINTHE))

labyrinthe = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, "S", 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, "E", 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

joueur_x = 40
joueur_y = 40

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            prochain_x = joueur_x
            prochain_y = joueur_y

            if event.key == pygame.K_LEFT:
                prochain_x -= TAILLE_CASE
            if event.key == pygame.K_RIGHT:
                prochain_x += TAILLE_CASE
            if event.key == pygame.K_UP:
                prochain_y -= TAILLE_CASE
            if event.key == pygame.K_DOWN:
                prochain_y += TAILLE_CASE

            case_x = prochain_x // TAILLE_CASE
            case_y = prochain_y // TAILLE_CASE

            if labyrinthe[case_y][case_x] != 1:
                joueur_x = prochain_x
                joueur_y = prochain_y

            if labyrinthe[case_y][case_x] == "E":
                pygame.quit()
                exit()

    ECRAN.fill((255, 255, 255))

    y = 0
    for ligne in labyrinthe:
        x = 0
        for case in ligne:
            if case == 1:
                pygame.draw.rect(ECRAN, (0, 0, 0), (x, y, TAILLE_CASE, TAILLE_CASE))
            elif case == "E":
                pygame.draw.rect(ECRAN, (0, 255, 0), (x, y, TAILLE_CASE, TAILLE_CASE))
            x += TAILLE_CASE
        y += TAILLE_CASE

    pygame.draw.rect(ECRAN, (255, 0, 0), (joueur_x, joueur_y, TAILLE_CASE, TAILLE_CASE))

    pygame.display.flip()