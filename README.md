# Azzouz le chasseur

Merci au poto Azzary big up pour le Selenium bot qui gère le dofus-map et pour l'astuce tesseract

The bot don't use your mouse is sending input to window  Dofus, no socket/sniffing (using win32).

You need the autopilot (using a potion or digging into the game files, there are thread in cadernis to do this (at your own risk, 
it may have been patched by Ankama))


IMPORTANT: change 'targets/spell.png' by your spell icon.

Dofus option:
- Limite de passage en mode creature = 0
- Afficher les personnages en transparence
- ne pas afficher les coordonnées de la carte
- interface clasique
- havre sac classique
- si vous avez la motive 7 screens de votre perso en mode creature (a placer dans target/personnageX) (not usefull de ouf quoi)
- etre en canal general (etoile blanche, chatbox vide, Information activé sur le canal pour pouvoir recup ID maps)
- optionel mode solo
- Minimiser la fenêtre de fin de combat (important sinon ne boucle pas les chasses)

Install all dependencies
```
pip install -r requirements.txt
```

you need to dl: https://github.com/UB-Mannheim/tesseract/wiki
if you change the path change it in 'ImageManaget.py' to.
pytesseract.pytesseract.tesseract_cmd = r'NEW_PATH'

You also need to add the french trained data if you're using the game in french, or the bot will have a hard time to differentiate between "Crâne de licorne" and "Corne de licorne" for eg

You need chrome and chromedriver download to use it with selenium.
Download the file of the same version as your google chrome, and place it in the folder where bot.py is.
https://chromedriver.chromium.org/downloads

Launch dofus on and select a character, then change the name of the game window in config.json to yours 'Name Dofus x.xx.xxx'.

before you start, make sure that your zaap.json file only contains your character's zaaps (zaap_all.json contains all the zaaps if you ever delete any one).
The list needs to be updated as some zaap have changed names, so if you can do it, it would be perfect, otherwise you'll wait for a next
update on this :D
You NEED the "Champs de Cania" zaap (oui quand meme baguette)
For the rest, the bot will TP you to the closest zaap you have, then do the rest of the road by autopalotte

Not having a hunt is easier, as it will start the loop from the beginning
Otherwise, the bot will ask you an input "HunterxHunter or ...":
Type 1 if you are on the map of the start of the hunt, or type anything else so the bot gets you to the starting map.
Note: If you are in the middle of a hunt, you MUST go to the last hint map, then input 1 to the question otherwise the bot will tp you at the first hint pos and it will get "stuck" (it'll quit your current hunt and get a new one)

# Error
"pywintypes.error: (1400, 'GetWindowRect', 'Handle de fenêtre non valide.')"
Name of the Dofus window is not correct.