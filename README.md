# pokemon-duels

Download the option files and script and execute it.

The following modules are required and the script is set to run in *Python3*.
Create the Virtualenv and install the packages

On linux:
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

On windows:
```
python3 -m venv .\venv
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Make sure the sprites directory exists with the desired sprites

### Running the code

- Update the files options.xls and options2.xls with the list of pokemons owned by each player.
- run the script with the syntax `python ./pokemon.py player1 player2`

    **Note: player1 and player2 data will be read from options.xls and options2.xls respectively**

Activate the virtualenv
Linux
```
> source venv/bin/activate
```
Windows
```
.\venv\Scripts\activate
```

Run the script:
```
> python .\pokemon.py Klonoa Red
Battle Type: single

Team Klonoa: 
----------  -----------
Garchomp    Joffrey
Heatran     Heatran
Haxorus     Bela
Drapion     Drapion
Volcarona   Brabuleta
Galvantula  Dona Aranha
----------  -----------
Team Red: 
---------  -----------
Machamp    Machamp
Charizard  Rengoku
-          Jean Grey
Cinderace  The Tsubasa
Flapple    Forbidden
Necrozma   The Necro
---------  -----------
[?] Who won the fight?: Team 1                                                                                                                                                                                                                                                               
 > Team 1
   Team 2

Current Score:
Klonoa: 1
Red: 0

Have Fun.
>
```
