from linda import *

NB_VOIES = 5

def ajoutVoies():
	for i in range (NB_VOIES):
		Out(i, None)
		print("Voie", i, "ajoutée")

def ajoutTrain(train):
	for i in range (NB_VOIES):
		if(Rd_nb(i) == None):
			Out(i, train)
			print("Train ajouté dans la voie", i)
			return
	print("Aucune voie libre")

def departTrain(train):
	for i in range (NB_VOIES):
		if(Rd_nb(i) == train):
			Out(i, None)
			print("Train parti de la voie", i)
			return
	print("Le train n'est pas dans la gare")


ajoutVoies()


ajoutTrain("Train_1")
ajoutTrain("Train_2")
departTrain("Train_2")


printTs()

