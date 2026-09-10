# ======================== game.py ========================

import pygame
import random
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITY, JUMP_VELOCITY, SPRING_JUMP_VELOCITY,
    DOODLE_SPEED, DOODLE_WIDTH, DOODLE_HEIGHT, PLATFORM_WIDTH,
    MIN_PLATFORM_GAP, MAX_PLATFORM_GAP, CAMERA_SCROLL_THRESHOLD,
    PLATFORMS, doodle_dict, DOODLE_START_X, DOODLE_START_Y, LIVES
)
from platforms import create_platform
from doodle import doodle_left_img, doodle_right_img
from window import generate_initial_platforms


# ======================== PARTIE 3.1 ========================
def apply_gravity():
    """
    Applique la gravité au Doodle en augmentant progressivement sa vitesse verticale (vel_y).
    Met à jour la position verticale (y) du Doodle.
    """
    # TODO :
    # 1. Ajouter GRAVITY à doodle_dict["vel_y"].
    # 2. Ajouter la nouvelle vitesse verticale à doodle_dict["y"].

    return

# ===========================================================


# ======================== PARTIE 1.2 ========================
def move_doodle():
    """
    Gère le déplacement horizontal du Doodle selon les touches pressées (Flèches ou A/D).
    Implémente le passage fluide d'un côté de l'écran à l'autre (Screen Wrap).
    """
    keys = pygame.key.get_pressed()

    # TODO : Gérez le déplacement vers la gauche et vers la droite.
    # - Mettre à jour doodle_dict["x"] avec DOODLE_SPEED.
    # - Mettre à jour doodle_dict["direction"].
    # - Mettre à jour doodle_dict["image"] avec doodle_left_img ou doodle_right_img.



    # TODO : Passage fluide d'un côté de l'écran à l'autre (Screen Wrap).
    # Utilisez SCREEN_WIDTH et DOODLE_WIDTH.



    return

# ===========================================================


# ======================== PARTIE 2.3 ========================
def move_platforms():
    """
    Déplace horizontalement les plateformes mobiles ("blue").
    Fait rebondir les plateformes lorsqu'elles atteignent les bords de la fenêtre.
    """
    # TODO :
    # - Parcourir PLATFORMS.
    # - Déplacer uniquement les plateformes bleues actives.
    # - Ajouter p["vx"] à p["x"].
    # - Inverser p["vx"] lorsqu'une plateforme touche un bord.

    return

# ===========================================================


# ======================== PARTIE 3.2 ========================
def check_platform_collisions():
    """
    Détecte si le Doodle atterrit sur une plateforme.
    Le rebond ne se produit QUE lorsque le Doodle descend (vel_y > 0)
    et que ses pieds touchent le haut de la plateforme.
    """
    # TODO : Complétez la logique de collision.
    #
    # Étapes suggérées :
    # 1. Si vel_y <= 0, quitter la fonction.
    # 2. Créer le rectangle du Doodle sous la forme (x, y, largeur, hauteur).
    # 3. Calculer la position des pieds du Doodle.
    # 4. Parcourir les plateformes actives.
    # 5. Créer le rectangle de chaque plateforme.
    # 6. Utiliser rects_collide(...) pour détecter le chevauchement.
    # 7. Vérifier que le Doodle arrive bien par le haut.
    #    Indice : la condition de référence utilise une tolérance de 14 pixels :
    #    doodle_feet - doodle_dict["vel_y"] <= p["y"] + 14
    # 8. Appliquer le rebond selon le type :
    #       spring -> SPRING_JUMP_VELOCITY
    #       brown  -> JUMP_VELOCITY et p["active"] = False
    #       autres -> JUMP_VELOCITY
    # 9. Sortir de la boucle après un rebond.

    return

# ===========================================================


# ======================== PARTIE 3.3 ========================
def scroll_camera():
    """
    Fait défiler l'arrière-plan vers le bas lorsque le Doodle dépasse le seuil
    CAMERA_SCROLL_THRESHOLD. Augmente le score et génère de nouvelles plateformes.
    """
    # TODO : Si doodle_dict["y"] < CAMERA_SCROLL_THRESHOLD :
    # - Calculer shift_y.
    # - Replacer le Doodle au seuil.
    # - Ajouter shift_y au score et mettre à jour high_score si nécessaire.
    # - Déplacer toutes les plateformes vers le bas de shift_y.
    # - Supprimer les plateformes qui sortent sous SCREEN_HEIGHT.
    # - Appeler generate_new_platforms().

    return

# ===========================================================


# ======================== PARTIE 3.4 ========================
def generate_new_platforms():
    """
    Génère de nouvelles plateformes au-dessus du haut de l'écran pour maintenir un flux continu.
    """
    # TODO :
    # 1. Si PLATFORMS est vide, quitter la fonction.
    # 2. Trouver la plus petite valeur de y dans PLATFORMS (highest_y).
    # 3. Tant que highest_y > 0 :
    #    - calculer new_y en retirant un espacement aléatoire ;
    #    - choisir new_x aléatoirement dans les limites de la fenêtre ;
    #    - choisir le type avec les probabilités suivantes :
    #          green  : 55 %
    #          blue   : 20 %
    #          spring : 13 %
    #          brown  : 12 %
    #    - ajouter create_platform(new_x, new_y, p_type) à PLATFORMS ;
    #    - mettre highest_y à jour.

    return

# ===========================================================


def check_game_over():
    """
    Vérifie si le Doodle tombe sous le bas de l'écran.
    Si oui, réduit les vies.
    Retourne True si la partie est terminée.
    """
    if doodle_dict["y"] > SCREEN_HEIGHT:
        doodle_dict["lives"] -= 1
        return True
    return False


def restart_game():
    """
    Réinitialise la partie : position du Doodle, vitesse, score et plateformes.
    """
    doodle_dict["x"] = DOODLE_START_X
    doodle_dict["y"] = DOODLE_START_Y
    doodle_dict["vel_y"] = 0.0
    doodle_dict["direction"] = "right"
    doodle_dict["image"] = doodle_right_img
    doodle_dict["score"] = 0
    doodle_dict["lives"] = LIVES

    generate_initial_platforms()


def rects_collide(r1, r2):
    """
    Vérifie si deux rectangles (x, y, largeur, hauteur) se chevauchent.
    Cette fonction est fournie et ne doit pas être modifiée.
    """
    return not (
        r1[0] + r1[2] <= r2[0] or r1[0] >= r2[0] + r2[2] or
        r1[1] + r1[3] <= r2[1] or r1[1] >= r2[1] + r2[3]
    )
