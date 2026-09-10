# ======================== platforms.py ========================

import os
import pygame
from config import ASSETS_DIR, PLATFORM_SIZE

# Chargement des différentes images de plateformes
platform_green_img = pygame.image.load(os.path.join(ASSETS_DIR, "platform_green.png"))
platform_green_img = pygame.transform.scale(platform_green_img, PLATFORM_SIZE)

platform_blue_img = pygame.image.load(os.path.join(ASSETS_DIR, "platform_blue.png"))
platform_blue_img = pygame.transform.scale(platform_blue_img, PLATFORM_SIZE)

platform_brown_img = pygame.image.load(os.path.join(ASSETS_DIR, "platform_brown.png"))
platform_brown_img = pygame.transform.scale(platform_brown_img, PLATFORM_SIZE)

platform_spring_img = pygame.image.load(os.path.join(ASSETS_DIR, "platform_spring.png"))
platform_spring_img = pygame.transform.scale(platform_spring_img, (PLATFORM_SIZE[0], PLATFORM_SIZE[1] + 10))

# Dictionnaire d'accès aux images selon le type de plateforme
platform_images = {
    "green": platform_green_img,
    "blue": platform_blue_img,
    "brown": platform_brown_img,
    "spring": platform_spring_img
}


# ======================== PARTIE 2.1 ========================
def create_platform(x, y, platform_type="green"):
    """
    Crée et retourne un dictionnaire représentant une plateforme.
    Types possibles :
      - "green"  : plateforme standard fixe
      - "blue"   : plateforme mobile horizontale
      - "brown"  : plateforme fragile qui se brise au contact
      - "spring" : plateforme munie d'un ressort (super saut)
    """

    # TODO : Complétez les valeurs des clés "vx" et "height".
    # - "vx" vaut 3.0 pour une plateforme bleue et 0.0 sinon.
    # - "height" vaut PLATFORM_SIZE[1] + 10 pour un ressort et
    #   PLATFORM_SIZE[1] pour les autres types.

    return {
        "x": float(x),
        "y": float(y),
        "type": platform_type,
        "image": platform_images[platform_type],
        "vx": 0.0,  # TODO
        "active": True,
        "width": PLATFORM_SIZE[0],
        "height": PLATFORM_SIZE[1]  # TODO
    }

# ===========================================================
