from linda import *
import time

NB_VOIES = 5



def initVoies():
	Out("noeud", True)
	for i in range (NB_VOIES):
		Out(i, None)
		print("Voie", i, "ajoutée")

def ajoutTrain(train):
	for i in range (NB_VOIES):
		if(Rd_nb(i) == None):
			attendreNoeud()
			Out(i, train)
			print("Train ajouté dans la voie", i)
			return
	print("Aucune voie libre")

def attendreNoeud():
	time.sleep(0)

def departTrain(train):
	for i in range (NB_VOIES):
		if(Rd_nb(i) == train):
			attendreNoeud()
			Out(i, None)
			print("Train parti de la voie", i)
			return
	print("Le train n'est pas dans la gare")



initVoies()

#ajoutTrain("Train_1")

printTs()

