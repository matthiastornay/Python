"""
Jeu de ShiFuMi très simple sous console
Matthias Tornay
"""

from random import *

partie = 1

while (partie):
	choix = 0
	actions = ["PIERRE", "FEUILLE", "CISEAUX"]
	score = 0
	score_IA = 0

	print(" ")
	print(" **********************")
	print(" *   Jeu du ShiFuMi   *")
	print(" **********************")	
	print(" ")
	print("Comment gagner ? Le but est de choisir une figure plus forte que celle de son adversaire. Le vainqueur sera celui qui gagnera 3 parties.") 
	print(" ")
	print("Choisissez une figure :")
	print(" ")
	print("#1 pour Pierre") 
	print("#2 pour Feuille")
	print("#3 pour Ciseaux")
	print(" ")	

	while (score < 3 and score_IA < 3):
		print(" ")
		choix = int(input("Votre choix : "))-1	
	
		while (choix != 0 and choix != 1 and choix != 2):
        		print("ERREUR !")
			print(" ")
	       		choix = int(input("Votre choix : "))-1
		
		choix_IA = randint(1, 3)-1
	
		print(" ")
		print("Vous avez choisi ", actions[choix], " et l'ordinateur a choisi ", actions[choix_IA], ".")

		if (choix == choix_IA):
			print(" ")
			print("Egalite ! La manche recommence.")
		elif (choix == choix_IA + 1):
			score += 1
			print(" ")
			print("Vous gagnez la manche !")
			print("Scores :")
		   	print("-------> Vous : ", score, " points.")
			print("-------> Ordinateur : ", score_IA, " points.")
		else :
			score_IA += 1
			print(" ")
			print("Vous perdez la manche !")
			print("Scores :")
		   	print("-------> Vous : ", score, " points.")
			print("-------> Ordinateur : ", score_IA, " points.")

	if (score > score_IA):
		print(" ")
		print("Bravo ! Vous gagnez la partie !")
	else :	
		print(" ")
		print("Dommage ! Vous perdez la partie !")
	
	print("Voulez-vous rejouer ? (1/0)")
	partie = input()
