# pokemon-duels

Download the option files and script and execute it.

The following modules are required and the script is set to run in *Python3*.
Create the Virtualenv and install the packages

on linux:
```
python3 -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install -r requirements.txt
```

on windows:
```
python3 -m venv .\venv
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

create the following directories in the same as the script.
- team
- sprites

### Example:
```
pokemon-duels % ./pokemon.py Klonoa Red
========================
Battle Type:  single
========================
Klonoa:
Stonejourner,Rock
Drilbur,Ground
========================
Red:
Galarian Farfetch’d,Fighting
Bonsly,Rock
========================
Have Fun.
========================
pokemon-duels %
```
