#!/usr/bin/ python-
# -*- coding: utf-8 -*-
import os
import random
elettori = 40
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
def invio():
	raw_input("Premi invio per continuare")
def start():
	print"""
/////////////////////////////////-..........-/////////////////////----////
///////////////////////////////--....-........-///////////////////----////
/////////////////////////////-...-/////////---.-//////////////////----////
////////////////////////////-..--//////////////--//////////////////---////
////////////////////////////...-----///////////-.-/////////////////----///
///////////////////////////-..---------///---///-./////////////////----///
///////////////////////-----..-----///-////-////-./////////////////----///
//////////////////////------..--//////--////////--//////////////////---///
///////////////////////----------////---////////////////////////////---///
////////////////////////----------///----///////////////////////////----//
/////////////////////////----------//----///////----////////////////----//
/////////////////////////-----------///////////------////////////////---//
//////////////////////////--/----------//////-///////////////////////---//
/////////-.......--///////---.-//--...-...-------////////////////////---//
////////-.--------..-/----.....-/*//-------///----///////////////////----/
////////-.---//---.............../****//---/**----///////////////////----/
////////-.-......................./***/-....-*-...---////////////////----/
/////////-........................./****-...//*-......---////////////----/
////////-..........................-/***-....-*/-.........---////////----/
////////-...........................-/**-.....-*/...........-////////-----
///////-............................../*/......//-..........-////////-----
///////-...............................//-.....-*/-.........-////////-----
//////-................................-/-.....-*/-..........-///////-----

Benvenuto nel simulatore di Matteo Renzi"""
	invio()
	giuoco()

def giuoco():
	clear()
	global elettori
	jlm = random.randint(-5,5)
	if jlm > 0:
		print "Tanti nuovi elettori ci hanno scelto"
	else:
		print "I cattivoni della LN ci hanno tolto voti"
	print "*"*45
	print "Elettori", elettori
	print """Che vuoi fare?
1) Inciucio
2) Presenta candidato inpresentabile in qualche città italiana
3) Vai contro alle richieste autonomiste in Lombardia e in Veneto
4) Modifica la Costituzione
5) Difendi ministro che ha fatto gaffe
6) Parla in una lingua straniera
7) Invita all'astensione
8) Ice Bucket Challenge
9) Talk su Facebook
"""
	l = input(">")
	if l == 1:
		k = random.randint(-4,2)
		elettori = elettori + k
		if k > 0:
			print "Inciucio riuscito"
		else:
			print "Inciucio fallito"
	elif l == 2:
		print "Presenti candidati indecenti in città italiane"
		k = random.randint(-5,4)
		elettori = elettori + k
		if k > 0:
			print "E vincono"
		else:
			print "Sconfitta clamorosa"
		
	elif l == 3:
		print "L'Autonomia non è accettabile: O a tutti o a nessuno (la seconda)"
		k = random.randint(-6,3)
		elettori = elettori + k
		if k > 0:
			print "Il popolo tollera"
		else:
			print "I lombardi vogliono scacciarti come Radetzky"
	elif l == 4:
		k = random.randint(-15,10)
		elettori = elettori + k
		if k > 0:
			print "Modifichi la Costituzione in modo centralista e autoritario"
		else:
			print "Perdi clamorosamente il referendum!"
	elif l == 5:
		k = random.randint(-6,2)
		elettori = elettori + k
		print "Difendi ministro che fa una gaffe al giorno"
	elif l == 6:
		print "De de de rasalta not gud è il nuovo tormentone. Meglio evitare"
		k = random.randint(-4,2)
		elettori = elettori + k
	elif l == 7:
		print "Questo referendum non s'ha da fare"
		k = random.randint(-7,6)
		elettori = elettori + k
		if k > 0:
			print "Il popolo va al mare contento"
		else:
			print "Il popolo ti ritiene fascista"
		
	elif l == 8:
		print "Ti tiri una secchiata d'acqua in testa"
		k = random.randint(-3,3)
		elettori = elettori + k
	elif l == 9:
		print "Parli con i tuoi fans su facebook"
		k = random.randint(-4,3) 
		elettori = elettori + k

	invio()
	if elettori < 25:
		print "Hai pochi elettori: Non puoi più governare il paese"
		exit()
	if elettori > 100:
		print "Riesci a diventare Duce d'Italia"
		print "Hai vinto"
		exit()
	giuoco()

start()
