# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:19:12 2015

@author: wykys
"""

import pylab

T = []
U = []
I = []
P = []

def dopocitej_hodnoty(x, y, div):
	len_x = len(x)
	
	if len_x < len(y):
		print "Problém funkce není na tomto intervalu definovaná"
		return False
	elif len_x < 2:
		print "Problém funkce má málo hodnot"
		return False
	
	X = []
	Y = []	
	
	for i in range(len_x):
		x[i] = float(x[i])
		y[i] = float(y[i])
	
	for i in range(len_x - 1):
		a = ( y[i+1] - y[i] ) * (-1)  
		b = x[i+1] - x[i]

		c = ( a*x[i] + b*y[i] ) * (-1)
		
		k = ( a/b ) * (-1)		
		q = ( c/b ) * (-1)
				
		t = x[i]
		s = b / (div+1)
		
		while t < x[i+1]:
			v = k*t + q
			X += [t]
			Y += [v]
			t += s
			
	X += [x[len_x-1]]
	Y += [y[len_x-1]]

	return (X, Y)
		
def integral(x, y):	
	plocha = 0
		
	if len(x) < len(y):
		print "Problém funkce není na tomto intervalu definovaná"
		return False
	elif len(x) < 2:
		print "Problém funkce má málo hodnot"
		return False
	
	x, y = dopocitej_hodnoty(x, y, 1000)
		
	for i in range(len(x)-1):
		plocha += (x[i+1] - x[i]) * y[i]
		
	return plocha
		

def stredni_hodnota(x, y):
	return integral(x, y)/x[-1]		
	

def nacti_soubor(file_name):
	global T, U, I, P	
	
	fr = open(file_name)
	print "Soubor", file_name, "otevřen."
	
	vstup = fr.readlines()
	
	hlavicka = vstup.pop(0)
	hlavicka = hlavicka.strip().split(',')
	
	for s in vstup:
		s = s.strip().split(',')
		
		t = float(s[0].strip())
		u = float(s[1].strip())
		i = float(s[2].strip())
		p = u * i
		
		T += [t]
		U += [u]
		I += [i]
		P += [p]


nacti_soubor("Elvykon.csv")

Ps = stredni_hodnota(T, P)


print "Střední hodnota:", Ps
	
pylab.plot(T, U)
pylab.plot(T, I)
pylab.plot(T, P, 'k-')
pylab.plot([T[0], T[-1]], [Ps, Ps], 'b-')
pylab.show()	
