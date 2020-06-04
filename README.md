![2](https://i.imgur.com/Q02Jiaf.jpg)

# [Download Recommended](https://github.com/MajorHype/CSGO-Timer/archive/master.zip)
## [Last Release](https://github.com/MajorHype/CSGO-Timer/releases/latest)
## [All Versions](https://github.com/MajorHype/CSGO-Timer/releases)

---

# CSGO TIMER

CSGO TIMER is a project/program created to give csgo players info about the bomb state.
With CSGO TIMER you can get info like how much time remains until the bomb explode, giving you the ability to judge if you should or should not try to defuse it maybe try to win the round or simply walk away.

# Disclaimer

You will not get VAC ban using this, because it uses Valve's public gamestate integration. The program simply uses the information from the CFG file and transforming it into sounds and external visuals that cannot be visually overlayed on top of the fullscreen game.
It is a tool made available by VALVE.

Explained in VALVE´S words:

"The game client by default can expose all game state, and send an update notification as soon as the client game state changes, to any local or remote HTTP POST endpoint using JSON as the game state structure. It just needs to know where the player wants to submit game state and what notifications to relay. This document will help third parties develop their tools and processes integrating with CS: GO game state. " - [Valve Developer Blog](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration)

## Getting Started

These instructions will get you setup with the project and get you ready to run the CSGO TIMER in your computer for the first time.

### Prerequisites

For now you can only use the program if your operating system is windows. Later versions will be available to all operating systems.

### Installation

* 1º Run the "Installer.exe"
* 2º After running the "Installer.exe" type the Driver letter (ex: C) that you have your CSGO game installed (what this will to is copy   the "gamestate_integration_GSI.cfg" to you game CFG folder so the game and the program can interact with each other) and press ENTER
* 3º The CFG file is now inside your CFG folder and is ready to start sending informtion to the CSGO TIMER
* 4º After you run the Program installer you will not need the "Installer.exe" anymore, so you can delete "Installer.exe" and             "gamestate_integration_GSI.cfg" if you want. (You will only need These two files if you at any time reinstall CSGO, and they are          available to download again)
* 5º From now on you only need to run "BombTime.exe" to start the program.

### How it works ?

* In the current version of the program, you will hear a sound when left 20, 15, 10, 5, seconds to defuse the bomb. 
* So you will hear a total of 4 beeps, if you dont have defuser you sould start defusing slightly after the 3 beep and if you have         defuser you sould start defunsing slightly after the 4 beep

## Built With

* [Python](https://www.python.org/) - The web framework used
* [Csgo-gsi-python](https://github.com/Erlendeikeland/csgo-gsi-python) - Github CS:GO Game State Integration
* [Valve Developer Blog](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration) - Valve Guide of CS:GO Game State Integration

## Credits

This program designed and developed by:

https://steamcommunity.com/profiles/76561199044328033

https://steamcommunity.com/id/FlashbangOFCL/
