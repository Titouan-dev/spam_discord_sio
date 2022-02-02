
# =========================================
#
#               SpamDiscord
#
# develop by Ssomgrap
# =========================================

import pyautogui as pag
from time import sleep

nbMessage = 1
message = ""
target = ""


# Permet d'envoyer le message à la cible
def sendMessage():
    for i in range(nbMessage):
        sleep(0.5)
        pag.write(message)
        sleep(0.2)
        pag.press("enter")


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
        sendMessage()


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