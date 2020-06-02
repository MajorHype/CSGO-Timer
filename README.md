# CSGO TIMER

CSGO TIMER is a project/program created to give a csgo player info about the bomb state.
With CSGO TIMER you can get info like how many time is left to the bomb until it explode, so you can judge if you should or not try to defuse it, try to win the round, you simply walk away.

# Disclaimer

You will not get vaced using this, because it uses Valve's public gamestate integration. The program is simply using the information from the CFG file and transforming it into sounds and external visuals that cannot be visually overlayed on top of the fullscreen game.
It is a tool made available by VALVE.

# How it works ?

Explained in VALVE´S words:

"The game client by default can expose all game state, and send an update notification as soon as the client game state changes, to any local or remote HTTP POST endpoint using JSON as the game state structure. It just needs to know where the player wants to submit game state and what notifications to relay. This document will help third parties develop their tools and processes integrating with CS: GO game state. " - [Valve Developer Blog](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration)

## Getting Started

These instructions will get you setup with the project and get you ready to run the CSGO TIMER in your computer for the first time.

### Prerequisites

For the time being there is no knowned prerequistes to use CSGO TIMER

### Installation

* 1º You will need to [download](https://github.com/diogofrancosilva/csgotimer/archive/master.zip) the .exe file 
* 2º Run the "Installer.exe"
* 3º After running the "Installer.exe" type the Driver letter (ex: C) that you have your CSGO game installed (what this will to is copy   the "gamestate_integration_GSI.cfg" to you game CFG folder so the game and the program can interact with each other) and press ENTER
* 4º The CFG file is now inside your CFG folder and is ready to start sending informtion to the CSGO TIMER
* 5º After you run the Program installer you will not need the "Installer.exe" anymore, so you can delete "Installer.exe" and             "gamestate_integration_GSI.cfg" if you want. (You will only need These two files if you at any time reinstall CSGO, and they are          available to download again)
* 6º From now on you only need to run "BombTime.exe" to start the program.

## Built With

* [Python](https://www.python.org/) - The web framework used
* [Csgo-gsi-python](https://github.com/Erlendeikeland/csgo-gsi-python) - Github CS:GO Game State Integration
* [Valve Developer Blog](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration) - Valve Guide of CS:GO Game State Integration

## Credits

This program disgned and developed by:

https://steamcommunity.com/profiles/76561199044328033

https://steamcommunity.com/id/FlashbangOFCL/
