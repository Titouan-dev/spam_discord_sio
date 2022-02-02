
# =========================================
#
#               SpamDiscord
#
# develop by Ssomgrap
# =========================================

import pyautogui as pag
from time import sleep
import ctypes

nbMessage = 1
message = ""
target = ""

#Traduit le message en code decimal
def tradMsg(msg):
    fMsg = []
    for char in list(msg):
        if char.isupper():
            fMsg.append(1)
            fMsg.append(int(hex(ord(char.lower())),0) - 32)
            fMsg.append(0)
        else:
            fMsg.append(int(hex(ord(char)),0) - 32)
    return fMsg

# Permet d'envoyer le message à la cible
def sendMessage(msg):
    print(msg)
    for i in range(nbMessage):
        for f in msg:
            if f == 1:
                ctypes.windll.user32.keybd_event(20, 0, 0, 0)
                ctypes.windll.user32.keybd_event(20, 0, 2, 0)
            if f == 0:
                ctypes.windll.user32.keybd_event(20, 0, 0, 0)
                ctypes.windll.user32.keybd_event(20, 0, 2, 0)
            else:
                ctypes.windll.user32.keybd_event(f, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)


# Permet de trouver la cible
def goToTarget(targ):
    pag.hotkey("ctrl", "k")
    sleep(0.5)
    pag.write(targ)
    sleep(0.2)
    pag.press("enter")
    sleep(0.1)
    try:
        pag.click("assets/images/targetNotFound.png")
        print("La cible n'a pas été trouvé!")
    except TypeError:
        msg = tradMsg(message)
        sendMessage(msg)


# Permet d'ouvrir discord
def openDiscord():
    try:
        pag.click("assets/images/discordOpen.png")
    except TypeError:
        try:
            pag.click("assets/images/discordOpenSelect.png")
            pag.moveTo(10, 10)
            sleep(0.2)
            pag.click("assets/images/discordOpen.png")
        except TypeError:
            pag.press("win")
            sleep(0.2)
            pag.write("discord")
            pag.press("enter")
            sleep(0.2)
            try:
                pag.click("assets/images/errorNoDiscord.png")
                print("Le bot n'a pas pu se lancé car il n'a pas trouvé discord!")
                exit
            except TypeError:
                sleep(9)
    goToTarget(target)



if __name__ == "__main__":
    # Interroge l'utilisateur sur la config du spam
    target = input("Entrez la cible :\n")
    if target == "":
        print("Veuillez mentionner la cible!")
    else:
        message = input("Entrez le message :\n")
        if message == "":
            print("Veuillez indiquer le message!")
        else:
            try:
                nbMessage = int(input("Entrez le nombre de message à envoyer :\n"))
                openDiscord()
                print("Mission terminer chef!")
            except ValueError:
                pag.alert("Veuillez entrer une valeur valide (nombre).\nValeur par defaut : 1")