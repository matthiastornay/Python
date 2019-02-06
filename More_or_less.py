#coding: utf-8

"""
The game is in French.
"""

import random, string

print(" ")
print("###################")
print("#  PLUS OU MOINS  #")
print("###################")
print(" ")

n_tries = 0

user_number = None

choix = None

condition = True

while condition:
	print(" ")
	print("Générer un nombre compris entre...")
	mini = int(input())
	print("et...")
	maxi = int(input())

	if mini < maxi:
		mystery_number = random.randint(mini, maxi)

	else :
		print("Erreur.")
		continue

	print(" ")
	print("L'ordinateur vient de générer un nombre mystère compris entre ", mini, " et ", maxi, ".")
	print("Vous pensez être capable de le deviner ? Tentez votre chance :")
	print(" ")	
	
	while condition:
		while True:
			try:
				user_number = int(input("Votre choix : "))

			except:
				print("Erreur.")
				continue

			break

		if user_number == mystery_number:
			n_tries += 1

			print("Bravo ! Vous avez retrouvé le nombre mystère en ", n_tries, " coups.")
			print(" ")

			condition = False

		elif user_number < mystery_number:
			print("C'est plus grand !")
			print(" ")

			n_tries += 1

		else :
			print("C'est plus petit !")
			print(" ")

			n_tries += 1
