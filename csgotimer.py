import gamestate
import information
import payloadparser
import server
import winsound
from server import GSIServer
from information import Player, Bomb
import time
import os
import shutil
import sys

def restart():
    print("Restarting Server...")
    os.execv(sys.executable, ['python'] + sys.argv)

server = GSIServer(("127.0.0.1", 3000), "S8RL9Z6Y22TYQK45JB4V8PHRJJMD9DS9")
server.start_server()

parar = False
while not parar:
    p = server.get_info("round","bomb")
    i = server.get_info("round","phase")
    if p == "planted":
        time.sleep(2.5)
        p = server.get_info("round","bomb")
        i = server.get_info("round", "phase")
        if i == "over":
            restart()
        elif p == "planted":
            time.sleep(5)
            p = server.get_info("round","bomb")
            i = server.get_info("round", "phase")
            if i == "over":
                restart()
            elif p == "planted":
                time.sleep(5)   
                p = server.get_info("round","bomb")
                i = server.get_info("round", "phase")
                if i == "over":
                    restart()
                elif p == "planted":
                    time.sleep(4.5)
                    winsound.Beep(300,500)
                    p = server.get_info("round","bomb")
                    i = server.get_info("round", "phase")
                    if i == "over":
                        restart()
                    elif p == "planted":
                        time.sleep(4.5)
                        winsound.Beep(350,500)
                        p = server.get_info("round","bomb")
                        i = server.get_info("round", "phase")
                        if i == "over":
                            restart()
                        elif p == "planted":
                            time.sleep(4.5)
                            winsound.Beep(400,500)
                            p = server.get_info("round","bomb")
                            i = server.get_info("round", "phase")
                            if i == "over":
                                restart()
                            elif p == "planted":
                                time.sleep(4.5)
                                winsound.Beep(450,500)
                                p = server.get_info("round","bomb")
                                i = server.get_info("round", "phase")
                                if i == "over":
                                    restart()
                                elif p == "planted":
                                    time.sleep(5)
                                    time.sleep(9)
                                    restart()
                                    
