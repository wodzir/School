#prvni poradna prednaska 
#Beránek má rád Jacka bez příchutě 
#státnice - 1 otázka z matematického softwaru (60 minut) 
# - NumPy, SciPi, Matplotlib, interpolace a aproximace fce 1 proměnné, derivace a integrace funkce 1 proměnné, řešení dif rov 
#naučit se github
#na zápočet - intergent, naše kody z disků atd ... ale rozhodně ne genAI a sdílení mezi sebou - budou monitorované PC 
# v githubu je zombie, ne SIR 

#Beránek naprogramuje SIR, my SIS a SIRD, přidáme nějaký model (roušky, méně socializace...), interpretovat model, 
# https://tinyurl.com/blamswble

#pozor na podmínky S + I + R = N 
#může být vylepšení dle knihoven scipy, numpy, pandas, seaborn 
#udělat na zápočet github s nějakými ukázkami metod a implementací 
#poté okecat u zápočtu - co se jak a proč chová, kde mohou být chyby a odchylky (nemusí být ošetřené ale vědět o nich)
#klíčové na zápočet - graf, popsaný (title, xlabel, ylabel, další parametry )
#snižování gamy o každé období, a další změny takové 
#udělat grafy a porovnat (konst. gama vs dynamická gama) 
#důležité je hrát si s matematikou 
#k započtu - lorka-volterra, lorentz attractor, 

#máme reálná data z covidu v čr - dá se určovat beta a gamma 


import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def SIR():
	Nt = 30
	N = 91_342 #podtrzitko oddeluje řády 	
	beta = 2 
	gama = 1 
	# Ro = beta/gama = 2 
	
	S = [N-1]
	I = [1] 
	R = [0]
	t = [0] 
	dt = 1 # 1 den 
	
	for it in range(Nt): 
		dS = -beta/N * I[-1] * S[-1] * dt
		dR = gama * I[-1] * dt
		dI = (-dS - dR) * dt
		S.append(S[-1] + dS)
		R.append(R[-1] + dR)
		I.append(I[-1] + dI)
		t.append(t[-1] + dt)
		
			  
	plt.plot(t,S,label = 'S')
	plt.plot(t,I,label = 'I')
	plt.plot(t,R,label = 'R')
	plt.legend()
	plt.show()
  
def SIRD(): 
	Nt = 100
	N = 91_342 #podtrzitko oddeluje řády 	
	beta = 0.4 
	gama = 0.035
	my = 0.005  
	# Ro = beta/gama = 2 
	
	S = [N-1]
	I = [2] 
	R = [0]
	D = [0] 
	t = [0] 
	dt = 1 # 1 den 
	
	betaChange = False
	
	for it in range(Nt): 
	
		#každý pátek párty 
		#prvni den simulace je pátek 
		if t[it] % 7 == 0:	
			beta = beta * 2 
			betaChange = True			
	
		dS = int(round(-beta/N * I[-1] * S[-1] * dt))
		dR = int(round(gama * I[-1] * dt))
		dD = int(round(my * I[-1] * dt))
		dI = int(round((-dS - dR - dD) * dt))
		S.append(S[-1] + dS)
		R.append(R[-1] + dR)
		I.append(I[-1] + dI)
		D.append(D[-1] + dD)
		t.append(t[-1] + dt)
		
		print(gama)
		
		if betaChange: 
			betaChange = False 
			beta = beta / 2 
			
		
			  
	plt.plot(t,S,label = 'S')
	plt.plot(t,I,label = 'I')
	plt.plot(t,R,label = 'R')
	plt.plot(t,D,label = 'D')
	plt.legend()
	plt.show()

#zadání na zápočet - zkusmo 
#Lotka-Volterra model (2 rovnice) 
# x = počet kořisti - zajíci 
# y = počet lovců - vlci
# alfa = rychlost množení kořisti 
# beta = rychlost umírání kořisti 
# gama = rychlost umírání lovců (čím víc jich je tím rychleji jim umírá jídlo)
# delta = rychlost množení lovců 

#naprogramovat 
#vizualizovat 
#přesvědčit se že dává smysl 
#2 otázky 
#provedte měření hledající odpovědi 

#porodnost koristi se zvýší pokud je počet lovců malý 

def LotVol(): 
	Nt = 300
	kor = 100 
	lov = 20
	alfa = 0.8
	beta = 0.03
	gama = 0.55
	delta = 0.01
	
	X = [kor]
	Y = [lov]
	t = [0]
	dt = 0.1 
	
	for i in range(Nt): 
	
		dx = int(round((alfa * X[-1] - beta * X[-1] * Y[-1]) * dt))
		dy = int(round((-gama * Y[-1] + delta * X[-1] * Y[-1]) * dt))
		
		X.append(max(0, X[-1] + dx)) #max vybere větší z těch dvou, nejdeme pod 0
		Y.append(max(0, Y[-1] + dy)) 
		t.append(t[-1] + dt)
		
		print(dx)
		print(dy)
		
	plt.plot(t,X,label = 'Zajici')
	plt.plot(t,Y,label = 'Lovci')
	plt.title("Vyvoj koristi a lovcu")
	plt.xlabel("Cas")
	plt.ylabel("Zajici a vlci")
	plt.legend()
	plt.show()
	
def Lorentz():	
	Nt = 10000
	sigma = 10
	ro = 28
	beta = 8/3 
	
	X=[1]
	Y=[1]
	Z=[1]
	t=[0]
	dt=0.01 
	
	for i in range(Nt): 
		dx = (Y[-1] - X[-1]) *  sigma * dt 
		dy = (X[-1] * (ro - Z[-1]) - Y[-1]) *dt
		dz = (X[-1] * Y[-1] - beta * Z[-1]) * dt
		
		X.append(X[-1] + dx)
		Y.append(Y[-1] + dy)
		Z.append(Z[-1] + dz)
		
	# 2D grafy, 3 grafy 	
	#fig, axs = plt.subplots(1, 3, figsize=(12,4))
	#axs[0].plot(X,Y)
	#axs[0].set_title('X,Y')
	#axs[1].plot(Y,Z)
	#axs[1].set_title('Y,Z')
	#axs[2].plot(X,Z)
	#axs[2].set_title('X,Z')
	#plt.tight_layout()
	#plt.show()
	
	# 3D graf
	fig = plt.figure(figsize=(8,6))
	ax = fig.add_subplot(111, projection='3d')
	ax.plot(X, Y, Z, lw = 0.5)
	ax.set_title("Lorenzův atraktor (3D)")
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Z")
	plt.show()
	
Lorentz()