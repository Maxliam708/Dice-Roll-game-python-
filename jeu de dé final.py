from random import randint
import time as ti
from tkinter import *
from datetime import *


# fonctions ######
def meilleurscore(record):
    """
    crée un fichier qui contient le meilleur score
    entrée: n un nombre int
    sortie: fichier txt qui contient le meilleur score du lancer de dé
    """

    t = datetime.now()
    f = open('Meilleur_Score.txt', 'w')
    f.write("Date: {}\n".format(t))
    f.write("Meilleur score: {}".format(record))
    return


def historiquedeparties(nom):
    """
    crée un fichier qui contient l'historique des lancés
    entrée: nom est un string qui est le nom de l'utilisateur
    sortie: fichier txt qui contient l'historique des lancés
    """

    t = datetime.now()
    f = open('lancer_dé_{}.txt'.format(nom), 'a')
    f.write("\n")
    f.write("Date: {}\n".format(t))
    f.write("Historique de parties:\n")
    f.write(historique)
    f.write("\n")
    return


def create(point : (int), record : (int)):
    """entrée : les point (int) et le record (int)
      sortie : crée une fenetre tkinter avec les points actuel et le record de la partie  """

    fenetre = Tk()
    fenetre.title('score')
    fenetre.geometry("500x250")
    L = Label(fenetre, text=("Vous avez donc obtenu {} points avant d’obtenir un 6".format(point)), fg='orange')
    L.pack()
    M = Label(fenetre, text=("Le record est {}.".format(record)), fg='orange')
    M.pack()
    B = Button(fenetre, text='supr', command=fenetre.destroy, fg='red')
    B.pack()
    fenetre.mainloop()


def face1():
    """entrée : rien
        sortie : une fentre tkinter avec la face 1 d'un dé"""

    fenetre = Tk()
    fenetre.geometry("1000x550")
    can1 = Canvas(fenetre, width=1000, height=500, bg="white")
    can1.pack()
    xc = 400
    yc = 150
    a = 250
    can1.create_rectangle(xc, yc, xc + a, yc + a, fill="cyan")
    xo = 410
    yo = 160
    b = 60
    can1.create_oval(xo + 90, yo+80, xo + b + 90, yo + b+80, fill="white")
    can1.focus_set()
    B = Button(fenetre, text='reroll', command=fenetre.destroy, fg='red')
    B.pack()
    fenetre.mainloop()
    return


def face2():
    """entrée : rien
        sortie : une fentre tkinter avec la face 2 d'un dé"""
    fenetre = Tk()
    fenetre.geometry("1000x550")
    can1 = Canvas(fenetre, width=1000, height=500, bg="white")
    can1.pack()
    xc = 400
    yc = 150
    a = 250
    can1.create_rectangle(xc, yc, xc + a, yc + a, fill="cyan")
    xo = 410
    yo = 160
    b = 60
    can1.create_oval(xo + 10, yo, xo + b + 10, yo + b, fill="white")
    can1.create_oval(xo + 160, yo + 160, xo + b + 160, yo + b + 160, fill="white")
    can1.focus_set()
    B = Button(fenetre, text='reroll', command=fenetre.destroy, fg='red')
    B.pack()
    fenetre.mainloop()
    return


def face3():
    """entrée : rien
        sortie : une fentre tkinter avec la face 3 d'un dé"""

    fenetre = Tk()
    fenetre.geometry("1000x550")
    can1 = Canvas(fenetre, width=1000, height=500, bg="white")
    can1.pack()
    xc = 400
    yc = 150
    a = 250
    can1.create_rectangle(xc, yc, xc + a, yc + a, fill="cyan")
    xo = 410
    yo = 160
    b = 60
    can1.create_oval(xo + 10, yo, xo + b + 10, yo + b, fill="white")
    can1.create_oval(xo + 160, yo + 160, xo + b + 160, yo + b + 160, fill="white")
    can1.create_oval(xo + 90, yo + 80, xo + b + 90, yo + b + 80, fill="white")
    can1.focus_set()
    B = Button(fenetre, text='reroll', command=fenetre.destroy, fg='red')
    B.pack()
    fenetre.mainloop()
    return


def face4():
    """entrée : rien
        sortie : une fentre tkinter avec la face 4 d'un dé"""

    fenetre = Tk()
    fenetre.geometry("1000x550")
    can1 = Canvas(fenetre, width=1000, height=500, bg="white")
    can1.pack()
    xc = 400
    yc = 150
    a = 250
    can1.create_rectangle(xc, yc, xc + a, yc + a, fill="cyan")
    xo = 410
    yo = 160
    b = 60
    can1.create_oval(xo + 10, yo, xo + b + 10, yo + b, fill="white")
    can1.create_oval(xo + 10, yo + 160, xo + b + 10, yo + b + 160, fill="white")
    can1.create_oval(xo + 160, yo, xo + b + 160, yo + b, fill="white")
    can1.create_oval(xo + 160, yo + 160, xo + b + 160, yo + b + 160, fill="white")
    can1.focus_set()
    B = Button(fenetre, text='reroll', command=fenetre.destroy, fg='red')
    B.pack()
    fenetre.mainloop()
    return


def face5():
    """entrée : rien
        sortie : une fentre tkinter avec la face 5 d'un dé"""

    fenetre = Tk()
    fenetre.geometry("1000x550")
    can1 = Canvas(fenetre, width=1000, height=500, bg="white")
    can1.pack()
    xc = 400
    yc = 150
    a = 250
    can1.create_rectangle(xc, yc, xc + a, yc + a, fill="cyan")
    xo = 410
    yo = 160
    b = 60
    can1.create_oval(xo + 10, yo, xo + b + 10, yo + b, fill="white")
    can1.create_oval(xo + 10, yo + 160, xo + b + 10, yo + b + 160, fill="white")
    can1.create_oval(xo + 160, yo, xo + b + 160, yo + b, fill="white")
    can1.create_oval(xo + 160, yo + 160, xo + b + 160, yo + b + 160, fill="white")
    can1.create_oval(xo + 90, yo + 80, xo + b + 90, yo + b + 80, fill="white")
    can1.focus_set()
    B = Button(fenetre, text='reroll', command=fenetre.destroy, fg='red')
    B.pack()
    fenetre.mainloop()
    return


def face6():
    """entrée : rien
        sortie : une fentre tkinter avec la face 1 d'un dé"""
    fenetre = Tk()
    fenetre.geometry("1000x550")
    can1 = Canvas(fenetre, width=1000, height=500, bg="white")
    can1.pack()
    xc = 400
    yc = 150
    a = 250
    can1.create_rectangle(xc, yc, xc + a, yc + a, fill="cyan")
    xo = 410
    yo = 160
    b = 60
    can1.create_oval(xo+10, yo, xo + b+10, yo + b, fill="white")
    can1.create_oval(xo+10, yo+80, xo + b+10, yo + b + 80, fill="white")
    can1.create_oval(xo+10, yo + 160, xo + b+10, yo + b + 160, fill="white")
    can1.create_oval(xo + 160, yo, xo + b + 160, yo + b, fill="white")
    can1.create_oval(xo + 160, yo + 80, xo + b + 160, yo + b + 80, fill="white")
    can1.create_oval(xo + 160, yo + 160, xo + b + 160, yo + b + 160, fill="white")
    can1.focus_set()
    B = Button(fenetre, text='fin', command=fenetre.destroy, fg='red')
    B.pack()
    fenetre.mainloop()
    return


def animation(valeur):
    '''entrée : la valeure du lanc" de dé (int)
    sortie : une fenetre tkinter de la face lié a la valeure '''
    assert type(valeur) == int
    if valeur == 1:
        face1()
    elif valeur == 2:
        face2()
    elif valeur == 3:
        face3()
    elif valeur == 4:
        face4()
    elif valeur == 5:
        face5()
    elif valeur == 6:
        face6()
    else:
        print("y'a un bug au niveau du dé")
    return

def meilleur_record():
    try:
        f = open('Meilleur_Score.txt', 'r')
        contenu = f.read()
        return int(contenu.split(" ")[-1])
    except:
        return 0

def lancement(record):
    '''entrée : record
    sortie : le lancement de dé avec la compil des scores et highscores dans une fenetre tkinter'''
    point = 0
    lancer = 1
    record_actuel = 0
    global historique
    historique = ''
    while True:
        valeur = randint(1, 6)
        resultat = "Lancer n°{0} : le dé donne {1}".format(lancer, valeur)
        print(resultat)
        historique = historique + "\n" + resultat
        animation(valeur)
        if valeur == 6:
            print("Vous avez donc obtenu {} points avant d’obtenir un 6".format(point))
            record_actuel = point
            if record_actuel > meilleur_record():
                record = record_actuel
                meilleurscore(record)
            print("Le record est ", record_actuel, ".")
            create(point, record)
            break
        lancer = lancer+1
        point = point+valeur
    return


def boucledejeu():
    while True :
        if input("voulez vous jouer ? oui/non") == "oui":
            lancement(record)
            historiquedeparties("Maxliam")
        else:
            print("au revoir")
            ti.sleep(1)
            break
    return


# corps du programme #####
record = 0
boucledejeu()
