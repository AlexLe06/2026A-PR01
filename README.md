# Projet 1 - INF1007 Automne 2026

## Directives
:alarm_clock: Date de remise : **À compléter**

:mailbox_with_mail: À remettre sur **GitHub** (les modalités exactes seront précisées en classe)

## Introduction

Dans ce projet, vous aurez comme tâche de compléter une version du jeu **Doodle Jump** 🦘 avec la bibliothèque Python `pygame`.

L'objectif du jeu est de faire monter le personnage, appelé le **Doodle**, le plus haut possible en rebondissant automatiquement de plateforme en plateforme. Le joueur contrôle uniquement les déplacements horizontaux du Doodle. Lorsque celui-ci atteint une certaine hauteur dans la fenêtre, la caméra défile : les plateformes descendent à l'écran et le score augmente selon la distance parcourue.

Le jeu contient quatre types de plateformes :

- **Plateforme verte** : plateforme normale et fixe ;
- **Plateforme bleue** : plateforme qui se déplace horizontalement ;
- **Plateforme marron** : plateforme fragile qui se brise après le rebond ;
- **Plateforme à ressort** : plateforme qui donne au Doodle une impulsion plus forte vers le haut.

Le joueur dispose d'une vie. La partie se termine lorsque le Doodle tombe sous le bas de l'écran. Il est alors possible d'appuyer sur la touche `R` pour recommencer.

Afin de simplifier votre travail, plusieurs éléments sont déjà fournis : l'affichage graphique, le chargement des images, l'écran de fin de partie, le redémarrage du jeu et certaines fonctions utilitaires. Votre travail portera principalement sur la manipulation de dictionnaires, les conditions, les boucles, la génération aléatoire, la physique simple et la détection de collisions.

**Pour lancer le jeu, vous devez exécuter le fichier `main.py`.**

## Installations requises

Ce projet nécessite l'utilisation de la bibliothèque [`pygame`](https://www.pygame.org/wiki/about).

Avant de commencer, assurez-vous que l'environnement conda `INF1007` est activé dans VS Code :

```bash
conda activate INF1007
```

Ensuite, installez Pygame :

```bash
pip install -U pygame==2.6.0
```

## Informations sur le projet

### Structure du projet

Le projet est organisé de la manière suivante :

```plaintext
2026A-PR01/
├── assets/
│   ├── background.png
│   ├── doodle_left.png
│   ├── doodle_right.png
│   ├── platform_green.png
│   ├── platform_blue.png
│   ├── platform_brown.png
│   └── platform_spring.png
├── config.py
├── doodle.py
├── platforms.py
├── window.py
├── game.py
├── main.py
└── README.md
```

### Détails sur les fichiers

- Le dossier `assets/` contient toutes les images utilisées dans le jeu.

- Le fichier `config.py` contient les constantes et variables globales du jeu, notamment :
  - `SCREEN_WIDTH` et `SCREEN_HEIGHT` : dimensions de la fenêtre ;
  - `DOODLE_WIDTH`, `DOODLE_HEIGHT` et `DOODLE_SIZE` : dimensions du Doodle ;
  - `DOODLE_START_X` et `DOODLE_START_Y` : position de départ du Doodle ;
  - `PLATFORM_WIDTH`, `PLATFORM_HEIGHT` et `PLATFORM_SIZE` : dimensions des plateformes ;
  - `MIN_PLATFORM_GAP` et `MAX_PLATFORM_GAP` : distances verticales minimale et maximale entre deux plateformes ;
  - `GRAVITY` : accélération verticale appliquée au Doodle ;
  - `JUMP_VELOCITY` : vitesse verticale appliquée lors d'un rebond normal ;
  - `SPRING_JUMP_VELOCITY` : vitesse verticale appliquée lors d'un rebond sur un ressort ;
  - `DOODLE_SPEED` : vitesse horizontale du Doodle ;
  - `CAMERA_SCROLL_THRESHOLD` : hauteur à partir de laquelle la caméra commence à défiler ;
  - `PLATFORMS` : liste globale contenant les dictionnaires des plateformes ;
  - `doodle_dict` : dictionnaire global contenant l'état du Doodle.

- Le fichier `doodle.py` charge les images du Doodle et initialise son dictionnaire.

- Le fichier `platforms.py` charge les images des quatre types de plateformes et contient la fonction `create_platform()` permettant de créer le dictionnaire d'une plateforme.

- Le fichier `window.py` crée la fenêtre, génère la disposition initiale des plateformes et gère l'affichage du jeu.

- Le fichier `game.py` contient la logique principale du jeu : mouvements, gravité, collisions, rebonds, plateformes mobiles, défilement de caméra et génération de nouvelles plateformes.

- Le fichier `main.py` contient la boucle principale du jeu. **Vous ne devez pas modifier ce fichier.**

### Repère de coordonnées

Dans Pygame, le point `(0, 0)` se trouve dans le coin **supérieur gauche** de la fenêtre :

```plaintext
(0, 0) ───────────────► x
   │
   │
   │        fenêtre de jeu
   │
   ▼
   y
```

Ainsi :

- augmenter `x` déplace un objet vers la droite ;
- diminuer `x` déplace un objet vers la gauche ;
- augmenter `y` déplace un objet vers le bas ;
- diminuer `y` déplace un objet vers le haut.

# Travail à réaliser

Vous devez compléter les sections identifiées par `TODO` dans les fichiers `doodle.py`, `platforms.py`, `window.py` et `game.py`.

> [!IMPORTANT]
> Plusieurs fonctionnalités sont déjà implémentées pour vous. Prenez le temps de lire le code fourni et de comprendre les dictionnaires `doodle_dict` et `PLATFORMS` avant de commencer. Les parties sont conçues pour être réalisées dans l'ordre.

## PARTIE 1 : Le Doodle 🦘

### 1.1 : Position initiale du Doodle

Dans le fichier `doodle.py`, le dictionnaire `doodle_dict` contient toutes les informations nécessaires pour représenter le personnage :

```python
doodle_dict.update({
    "x": 1000,
    "y": 1000,
    "vel_y": 0.0,
    "direction": "right",
    "score": 0,
    "high_score": 0,
    "lives": LIVES,
    "image": doodle_right_img
})
```

Les valeurs `1000` utilisées pour `x` et `y` sont volontairement incorrectes.

Votre première tâche consiste à remplacer ces deux valeurs afin que le Doodle apparaisse à sa position de départ prévue par le jeu.

**Contraintes à respecter :**

- utilisez les variables `DOODLE_START_X` et `DOODLE_START_Y` déjà définies dans `config.py` ;
- ne remplacez pas ces variables par des nombres écrits directement dans le dictionnaire.

À la fin de cette partie, le Doodle doit apparaître au-dessus de la plateforme verte de départ lorsque vous exécutez `main.py`.

### 1.2 : Déplacement horizontal et changement de direction

Dans le fichier `game.py`, complétez la fonction `move_doodle()`.

Le joueur doit pouvoir déplacer le Doodle horizontalement avec :

- `K_LEFT` ou `K_a` : déplacement vers la gauche ;
- `K_RIGHT` ou `K_d` : déplacement vers la droite.

Pour connaître l'état des touches du clavier, utilisez :

```python
keys = pygame.key.get_pressed()
```

**Détails à respecter :**

- la position `x` doit être modifiée de `DOODLE_SPEED` pixels ;
- lorsque le Doodle se déplace vers la gauche :
  - `direction` doit devenir `"left"` ;
  - `image` doit devenir `doodle_left_img` ;
- lorsqu'il se déplace vers la droite :
  - `direction` doit devenir `"right"` ;
  - `image` doit devenir `doodle_right_img`.

#### Passage d'un bord à l'autre de l'écran

Contrairement à Frogger, le Doodle ne doit pas être bloqué aux limites gauche et droite. Il doit réapparaître de l'autre côté de l'écran lorsqu'il dépasse un bord.

Complétez donc également la partie **Screen Wrap** de `move_doodle()` :

- si le Doodle dépasse suffisamment le bord gauche, il doit réapparaître à droite ;
- s'il dépasse suffisamment le bord droit, il doit réapparaître à gauche.

Utilisez `SCREEN_WIDTH` et `DOODLE_WIDTH` pour effectuer les calculs plutôt que des valeurs numériques fixes.

## PARTIE 2 : Les plateformes 🟩🟦

### 2.1 : Propriétés particulières des plateformes

Dans `platforms.py`, la fonction `create_platform(x, y, platform_type)` construit un dictionnaire représentant une plateforme.

La majorité du dictionnaire est déjà fournie. Vous devez compléter deux propriétés : `vx` et `height`.

```python
return {
    "x": float(x),
    "y": float(y),
    "type": platform_type,
    "image": platform_images[platform_type],
    "vx": ...,      # à compléter
    "active": True,
    "width": PLATFORM_SIZE[0],
    "height": ...   # à compléter
}
```

**Contraintes à respecter :**

- une plateforme **bleue** doit avoir une vitesse horizontale de `3.0` ;
- les autres plateformes doivent avoir une vitesse horizontale de `0.0` ;
- une plateforme de type `spring` doit avoir une hauteur de `PLATFORM_SIZE[1] + 10` ;
- les autres plateformes gardent la hauteur normale `PLATFORM_SIZE[1]`.

Vous pouvez utiliser une structure `if/else` ou une expression conditionnelle Python.

### 2.2 : Génération de la disposition initiale

Dans `window.py`, la fonction `generate_initial_platforms()` commence déjà par :

1. vider la liste `PLATFORMS` ;
2. créer une plateforme verte sous le Doodle ;
3. calculer la hauteur de la plateforme suivante.

Vous devez compléter la boucle qui remplit le reste de l'écran avec des plateformes aléatoires.

**Étapes à suivre :**

- Tant que la position verticale `current_y` est supérieure à `30` :
  - choisissez une position `x` aléatoire comprise entre `0` et `SCREEN_WIDTH - PLATFORM_WIDTH` ;
  - choisissez aléatoirement un type de plateforme selon les probabilités suivantes :
    - verte : 65 % ;
    - bleue : 17 % ;
    - ressort : 10 % ;
    - marron : 8 % ;
  - créez la plateforme à l'aide de `create_platform(x, current_y, p_type)` ;
  - ajoutez-la à `PLATFORMS` ;
  - diminuez `current_y` d'une distance aléatoire comprise entre `MIN_PLATFORM_GAP` et `MAX_PLATFORM_GAP`.

**Indice :** `random.random()` retourne un nombre à virgule compris entre `0.0` et `1.0`.

Par exemple :

```python
r = random.random()
if r < 0.65:
    # cas 1
elif r < ...:
    # cas 2
```

### 2.3 : Déplacement des plateformes bleues

Dans `game.py`, complétez la fonction `move_platforms()`.

Cette fonction doit parcourir toutes les plateformes présentes dans `PLATFORMS`.

Pour chaque plateforme :

- vérifiez qu'elle est de type `"blue"` ;
- vérifiez qu'elle est encore active ;
- ajoutez sa vitesse horizontale `vx` à sa position `x` ;
- lorsqu'elle touche le bord gauche ou le bord droit, inversez le signe de sa vitesse.

Pour inverser une vitesse, vous pouvez utiliser :

```python
p["vx"] *= -1
```

## PARTIE 3 : Physique, rebonds et progression 🚀

### 3.1 : Application de la gravité

Dans `game.py`, complétez la fonction `apply_gravity()`.

La variable `doodle_dict["vel_y"]` représente la vitesse verticale du Doodle.

À chaque image du jeu :

1. ajoutez `GRAVITY` à `vel_y` ;
2. ajoutez ensuite la nouvelle valeur de `vel_y` à la position `y` du Doodle.

Rappelez-vous que dans le repère Pygame, une vitesse verticale **positive** fait descendre le Doodle et une vitesse **négative** le fait monter.

### 3.2 : Détection des collisions avec les plateformes

Complétez la fonction `check_platform_collisions()` dans `game.py`.

Le Doodle doit rebondir uniquement lorsqu'il **descend** sur le dessus d'une plateforme. Il ne doit pas rebondir lorsqu'il traverse une plateforme pendant sa montée.

Une fonction utilitaire `rects_collide(r1, r2)` est déjà fournie à la fin du fichier. Elle reçoit deux rectangles sous la forme :

```python
(x, y, largeur, hauteur)
```

**Étapes à suivre :**

1. Si `doodle_dict["vel_y"] <= 0`, quittez immédiatement la fonction.
2. Créez un rectangle pour le Doodle à partir de `x`, `y`, `DOODLE_WIDTH` et `DOODLE_HEIGHT`.
3. Calculez la position verticale des pieds du Doodle.
4. Parcourez toutes les plateformes de `PLATFORMS`.
5. Ignorez les plateformes qui ne sont plus actives.
6. Pour chaque plateforme active :
   - créez son rectangle ;
   - vérifiez si les deux rectangles se chevauchent avec `rects_collide()` ;
   - vérifiez également que les pieds du Doodle arrivent bien sur le dessus de la plateforme.
7. Lorsqu'un atterrissage est détecté, appliquez le rebond approprié :
   - plateforme verte ou bleue : `JUMP_VELOCITY` ;
   - plateforme à ressort : `SPRING_JUMP_VELOCITY` ;
   - plateforme marron : `JUMP_VELOCITY`, puis `active = False`.
8. Une fois le rebond traité, sortez de la boucle.

**Indice pour vérifier que le Doodle arrive par le haut :** le code doit comparer la position actuelle de ses pieds avec leur position approximative à l'image précédente. Une tolérance de quelques pixels est déjà suggérée dans les commentaires du fichier.

### 3.3 : Défilement de la caméra et score

Complétez la fonction `scroll_camera()` dans `game.py`.

Lorsque la position `y` du Doodle devient plus petite que `CAMERA_SCROLL_THRESHOLD`, le personnage ne doit plus continuer à monter visuellement dans la fenêtre. À la place, le monde doit défiler vers le bas.

**Étapes à suivre :**

- calculez la distance `shift_y` nécessaire pour ramener le Doodle à `CAMERA_SCROLL_THRESHOLD` ;
- replacez le Doodle exactement sur ce seuil ;
- ajoutez `shift_y` au score ;
- si le score courant dépasse `high_score`, mettez `high_score` à jour ;
- ajoutez `shift_y` à la coordonnée `y` de toutes les plateformes ;
- supprimez de `PLATFORMS` les plateformes qui sont sorties sous le bas de la fenêtre ;
- appelez `generate_new_platforms()` pour ajouter de nouvelles plateformes en haut.

Pour modifier le contenu d'une liste globale sans remplacer l'objet liste, vous pouvez utiliser une affectation par tranche :

```python
PLATFORMS[:] = [...]
```

### 3.4 : Génération de nouvelles plateformes

Complétez finalement `generate_new_platforms()` dans `game.py`.

Cette fonction doit maintenir un flux continu de plateformes lorsque la caméra défile.

**Étapes à suivre :**

- si `PLATFORMS` est vide, quittez la fonction ;
- trouvez la plateforme la plus haute, c'est-à-dire celle dont la valeur `y` est la plus petite ;
- tant que cette plateforme est encore sous le haut de l'écran (`highest_y > 0`) :
  - calculez une nouvelle position `y` en retirant un espacement aléatoire entre `MIN_PLATFORM_GAP` et `MAX_PLATFORM_GAP` ;
  - choisissez une position `x` aléatoire valide ;
  - choisissez le type de plateforme selon les probabilités suivantes :
    - verte : 55 % ;
    - bleue : 20 % ;
    - ressort : 13 % ;
    - marron : 12 % ;
  - créez et ajoutez la nouvelle plateforme ;
  - mettez `highest_y` à jour.

## Fonctionnalités déjà fournies

Vous n'avez pas à programmer les éléments suivants :

- le chargement et le redimensionnement des images ;
- la création de la fenêtre Pygame ;
- l'affichage du fond, du Doodle, des plateformes et du score ;
- la détection générale du chevauchement de deux rectangles (`rects_collide`) ;
- la détection de la chute sous l'écran (`check_game_over`) ;
- l'écran `GAME OVER` ;
- la touche `R` permettant de recommencer ;
- la boucle principale contenue dans `main.py`.

# Directives pour la remise

Pour remettre votre travail, créez un fichier ZIP nommé `NOM_PRENOM-PR01.zip`, où `NOM` est votre nom de famille et `PRENOM` votre prénom.

Le fichier ZIP doit contenir le dossier `2026A-PR01` complet avec les fichiers Python et le dossier `assets/`.

Ne modifiez pas les noms des fichiers ni la structure du projet.

# Barème de correction

Le barème proposé est le suivant :

| **Partie** | **Tâche** | **Points** |
|---|---|---:|
| **PARTIE 1 : Le Doodle 🦘** |  | **/4** |
| 1.1 | Position initiale correcte avec `DOODLE_START_X` et `DOODLE_START_Y` | 1 |
| 1.2 | Déplacement gauche/droite avec les touches demandées | 1.5 |
| 1.2 | Mise à jour de la direction et de l'image | 0.5 |
| 1.2 | Passage correct d'un bord de l'écran à l'autre | 1 |
| **PARTIE 2 : Les plateformes 🟩🟦** |  | **/6** |
| 2.1 | Propriétés `vx` et `height` correctes selon le type de plateforme | 1 |
| 2.2 | Boucle de génération et positions aléatoires valides | 1.5 |
| 2.2 | Respect des espacements et ajout des plateformes à `PLATFORMS` | 0.75 |
| 2.2 | Sélection des quatre types avec les probabilités demandées | 0.75 |
| 2.3 | Déplacement des plateformes bleues actives | 1 |
| 2.3 | Inversion correcte de la vitesse aux deux bords | 1 |
| **PARTIE 3 : Physique, rebonds et progression 🚀** |  | **/10** |
| 3.1 | Mise à jour correcte de la vitesse verticale et de la position | 1 |
| 3.2 | Collision vérifiée uniquement pendant la descente | 0.5 |
| 3.2 | Construction et vérification correctes des rectangles | 1.5 |
| 3.2 | Détection d'un atterrissage sur le dessus d'une plateforme | 1 |
| 3.2 | Rebond normal sur plateformes vertes et bleues | 0.5 |
| 3.2 | Super-saut sur plateforme à ressort | 0.5 |
| 3.2 | Désactivation d'une plateforme marron après le rebond | 0.5 |
| 3.3 | Calcul du défilement, repositionnement du Doodle et mise à jour du score | 1 |
| 3.3 | Déplacement et suppression des plateformes sorties de l'écran | 1 |
| 3.4 | Génération continue de nouvelles plateformes avec positions, espacements et types aléatoires | 2.5 |
| **Total** |  | **/20** |
