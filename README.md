# Azzouz le chasseur

This is a bot for resolving the hunts in Dofus.
It's using Tesseract (from Manheim University) for text image recognition, and Selenium with a chrome driver to search for the hints on the Dofus Map website.

Simple PyAutoGUI to manage the dofus window, organic clics and everything (still need to randomize the delays, but the client/server connexion already adds buffer due to latency so it won't be urgent as it's not really detectable by Ankama), openCV for taking sc and managing images/getting positions etc

The bot doesn't use your mouse, it's sending input to the Dofus window, no socket/sniffing (using win32) so it's quite hard to detect unless a mod comes to talk to you directly.

You'll need the autopilot (using a potion or digging into the game files, there are threads in cadernis on how to do this (at your own risk, it might have been patched by Ankama))
I'm working on a map changing function but some maps are "special" (going down brings you one case down and one case left in Bonta for eg) and i'm don't really want to spend much time parsing the whole dofus map and doing some A* search for shortest path (it will need a lot of ressources if you add this to the already process hungry libraries i use)

IMPORTANT: 
    - Change 'targets/spell.png' by your spell icon.
    - DO NOT minimize the chrome or Dofus window, you can keep it running in the background but if you minimize it, the bot will peter un câble (it will just pause and do nothing as no window will be screenshotable or usable)

Dofus options:
    - Limite de passage en mode creature = 0
    - Afficher les personnages en transparence
    - ne pas afficher les coordonnées de la carte
    - interface clasique
    - havre sac classique
    - si vous avez la motive 7 screens de votre perso en mode creature (a placer dans target/personnageX) (not usefull de ouf quoi)
    - etre en canal general (etoile blanche, chatbox vide, Information activé sur le canal pour pouvoir recup ID maps)
    - optionel mode solo
    - Minimiser la fenêtre de fin de combat (important sinon ne boucle pas les chasses)

Requirements : 

Install all dependencies:
```
    pip install -r requirements.txt
```

    you need to dl: https://github.com/UB-Mannheim/tesseract/wiki
    if you change the path in the installer, change it in 'ImageManager.py' too:
```
pytesseract.pytesseract.tesseract_cmd = r'NEW_PATH'
```

    You also need to add the french trained data if you're using the game in french, or the bot will have a hard time to differentiate between "Crâne de licorne" and "Corne de licorne" for eg, search for the github repo, ez. I'll add a link here when I can

    You need chrome and chromedriver download to use it with selenium.
    Download the file of the same version as your google chrome, and place it in the folder where bot.py is.
    https://chromedriver.chromium.org/downloads

    Launch dofus on and select a character, then change the name of the game window in config.json to yours 'Name Dofus x.xx.xxx'.

    Before you start, make sure that your zaap.js on file only contains your character's zaaps (zaap_all.json contains all the zaaps if you ever delete any one)
    The list needs to be updated as some zaap have changed names, so if you can do it, it would be perfect, otherwise you'll have to wait for a next update on this :D
    You NEED the "Champs de Cania" zaap (oui quand meme baguette)
    For the rest, the bot will TP you to the closest zaap you have, then do the rest of the road by autopalotti

Then, start the bot by typing ```python bot.py```

Not having a hunt is easier, as it will start the loop from the beginning
Otherwise, the bot will ask you for an input "HunterxHunter or ...":
Type 1 if you are on the map of the start of the hunt, or type anything else so the bot gets you to the starting map.
Note: If you are in the middle of a hunt, you MUST go to the last hint map, then input 1 to the question otherwise the bot will tp you at the first hint pos and it will get "stuck" (it'll quit your current hunt and get a new one)

# Error
"pywintypes.error: (1400, 'GetWindowRect', 'Handle de fenêtre non valide.')"
Name of the Dofus window is not correct.