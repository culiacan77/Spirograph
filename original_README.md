# Spirograph

Ce programme dessine des figures géométriques sur l'écran du PicoMo. Il
simule un spirograph en dessinant des cercles de différentes tailles et
couleurs.

## Installation de Circuit Python


1. Connectez votre PiCoMo tout en gardant votre doigt pressé sur le bouton S7 (en haut à droite).
   
   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/picomo_board_fr.jpg)

2. Un disque "RPI-RP2" devrait apparaître sur votre ordinateur.
   
   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/screen1.png)

3. Téléchargez le fichier [flash_nuke.uf2](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2).

4. Glissez-déposez le fichier `flash_nuke.uf2` sur le disque "RPI-RP2".
   
   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/screen2.png)

5. Votre PiCoMo devrait redémarrer et le disque "RPI-RP2" devrait réapparaître.
 
7. Rendez-vous sur le site de CircuitPython et téléchargez le code dans la langue de votre choix:
    - [PiCoMo Version 2.0](https://circuitpython.org/board/picomo_v2/)
    - [PiCoMo Version 3.0](https://circuitpython.org/board/picomo_v3/)
8. Glissez-déposez le fichier téléchargé sur le disque "RPI-RP2".
   
   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/screen3.png)

9. Votre PiCoMo devrait redémarrer en affichant du texte sur l'écran
   et le disque "RPI-RP2" devrait être remplacé par un disque "CIRCUITPY".
   
   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/screen4.png)

## Installation de l'application

1. Téléchargez ce dépôt (https://github.com/heia-picomo/spirograph-circuitpython) sous la forme de [fichier
   zip](https://github.com/heia-picomo/spirograph-circuitpython/archive/refs/heads/main.zip).
   
   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/spirograph/screen5.png)

2. Double-cliquez sur le fichier téléchargé pour le décompresser.

   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/spirograph/screen6.png)

3. Ouvrez le dossier `spirograph-circuitpython-main`.

4. Glissez-déposez le contenu du dossier `spirograph-circuitpython-main` sur
   le disque "CIRCUITPY".
   
 
   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/spirograph/screen7.png)

5. L'ordinateur vous demande de remplacer certains fichiers. Acceptez de
   remplacer ces fichiers en cliquant sur "Replace the files in the
   destination" ("Remplacer les fichiers dans la destination" en
   français).

   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/spirograph/screen8.png)

## Mofiication du programme

1. Ouvrez le programme _VS Code_. en cliquant tout d'abord sur l'icône _Windows_ en bas à gauche de votre écran, puis sur l'icône _VS Code_.
   
   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/screen10.png)


2. Dès que le programme est ouvert, cliquez sur _File_ puis sur _Open Folder..._

   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/screen11.png)


3. Choisissez le disque _CIRCUITPY (E:)_ puis cliquez sur _Select Folder_

   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/screen12.png)

4. Le système vous demande si vous faites confiance à l'auteur de ce programme. Cliquez sur _Yes, I trust the authors_

   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/spirograph/screen13.png)

5. Vous pouvez maintenant modifier le programme en cliquant sur le fichier _code.py_. Si le système vous demande d'installer une extension, cliquez simplement sur la croix pour fermer la fenêtre.

   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/spirograph/screen14.png)

6. Sauvez le fichier avec vos modifications en cliquant sur _File_ puis sur _Save_.

   ![](https://raw.githubusercontent.com/heia-picomo/web-assets/main/spirograph/screen15.png)

7. Votre PiCoMo redémarre automatiquement avec le nouveau programme.
