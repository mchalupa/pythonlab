#!/usr/bin/env python
# -*- coding: utf-8 -*-

#~ pokud je vrsek hirearchie dedi se od object
#~ 
#~ class T(object):
	#~ def metoda(self, args):
		#~ ...
		#~ ...
#~ 
#~ prvni argument je vzdy self. jmeno nemusi byt self, ale melo by byt (this v C++)
#~ pri volani se neuvadi
#~ 
#~ a = T()
#~ a.metoda()

#~ class nazev(predek)
#~ dedeni:
	#~ class U(T):
#~ pretezovani trid
#~ 
#~ konstruktory:
#~ metoda __init__(self, argumenty)
#~ 				inicializece....
#~ pokud inicializujeme bez init rovnou v class, tak vytvorime tridni atributy (spolecne pro VSECHNY instance tridy
#~ destruktor: __del__, pokud pouzijeme, musime sebe sami smazat!! protoze sme premazali default destr. to udelama pomoci: del self
#~ U.__dict__ je interni slovnik tridy U. Je tam vse. instance.__dict__ obsahuje atributy. trida.__dict__ obsahuje metody

#~ instance.__class__ je odkaz na tridu instance
 #~ nema ochranu zapouzdreni, prom = verejne, _prom = protected __prom = private (konvence, nic vic)
