from linda import *
from train import *
import time
from tkinter import * 

compteurTrain = 0

def ajoutClic():
	global compteurTrain
	ajoutTrain(compteurTrain)
	majAffichage()
	compteurTrain += 1

def supprimeClic():
	s = entry.get()
	In_nb(int(s))
	majAffichage()


def majAffichage():
	s = ""
	for i in range(0,NB_VOIES):
		if(Rd_nb(i) == None):
			s += "Voie " + str(i) + " libre " + "\n"
		else:
			s += "Voie " + str(i) + " occupée par le train " + str(Rd_nb(i))  + "\n"
	listeVoies.set( s )

fenetre = Tk()

#label1 = Label(fenetre, text="		Voies:			")
#label1.pack()

tabs = Label(fenetre, text="					")
tabs.pack()

listeVoies = StringVar()
label2 = Label(fenetre, textvariable=listeVoies)
label2.pack()

boutonAjoutTrain=Button(fenetre, text="Ajouter un train", command=ajoutClic)
boutonAjoutTrain.pack()

boutonDepartTrain=Button(fenetre, text="Libérer la voie", command=supprimeClic)
boutonDepartTrain.pack()

entry = Entry(fenetre)
entry.pack()
entry.delete(0, END)

majAffichage()

fenetre.wm_title("Bienvenue à la gare de Chambéry")
fenetre.mainloop()