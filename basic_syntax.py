#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# http://msivak.fedorapeople.org/python/
# sphinx - generator dokumentace

# v interpretu: >>> import this

# help(obj) a dir(obj)



########################################################################
#		STRINGY
########################################################################

print "%d ahoj %d %c" % (1,2,'a')
#~ '1 ahoj 2 a'

print "vec: %(item)s" % {"item": "joj"}
#~ 'vec: joj'

# v pythonu 3 je misto % metoda format

# u"string" --> unicode string
# r"string" --> raw string (nevyhodnocuji se escape sekvence a pod. hodi
#				se u regularnich vyrazu

# str.split() --> bez parametru rozdeli podle bilych znaku, parametry
#					muzou byt oddelovace a max. pocet deleni

# str.upper()
# str.lower()


#muzeme scitat retezce (slozitost linearni, lepsi je pres join() )
    #~ S.join(iterable) -> string
    #~ 
    #~ Return a string which is the concatenation of the strings in the
    #~ iterable.  The separator between elements is S.

#~ vyrezy stringu (i ostatnich iterrable veci - tuple, slovniky, listy)
#~ 	str[od:do:o_kolik]
#~  od muze byt zaporne (bere se od konce)
#   str[5:] od 5 do konce
#~ str[:9] od zacatku do 9
#  str[-5:] poslednich 5 znaku
#~ str[:] --> kopie retezce
#~ str[::-1] --> nejkratsi zpusob, jak obratit retezec


########################################################################
#		TUPLES
########################################################################
# immutable

# (1) == 1
# (1,) == tuple s jednim prvkem

########################################################################
#		DICT
########################################################################
# asociativni pole
# skoro vse je interne v pythonu slovnik (__dict__)

#v pythonu2 metody: items (vrati list dvojic (key, val) ), values, keys
#					iteritems, itervalues, iterkeys !! (pokud je velky 
#					slovnik, tak se to da iterovat ve foru)

# klicove slovo in --> if "k" in slovnik:

# setdefault, get
# a.get(2, "default") --> vrat hodnotu prvku k nebo default
# setdefault --> pokud existuje, tak nic, jinak nastav default

########################################################################
#		FUNKCE
########################################################################

# muze mit defaultni hodnoty argumentu, ty musi byt zapsany az na konec
# def foo(a,b,c=4, d=8)

# pri volani muzu pouzit prirazeni, pokud nechci vypisovat vsechny arg
# foo(1,2,d=2)

# muzeme pouzit promenny pocet argumentu (uplne na konec)
# *args
# **kvargs
#def f(a,b,*args, **kvargs)
# f(1,2,3,4,k=7)
# --> args = [3,4]; kvargs = {'k': 7}

# pokud se nepouzije return, tak navratova hodnota je None
# operator is --> if item is None:

### predava se odkazem!!
# pokud do funkce predam mutable argument
#~ foo(list) --> list ve funkci zmenim, tak se zmeni i mimo ni

#pr: def f(a=[]), do a se vytvori objekt a pri volani se vzdy pouzije
#~   resi se a=None a na zacatku funkce if a is None: ... 

# pokud chci kopii misto odkazu, tak pouziji obj[:] (vytvori se kopie
# obj a preda se odkaz na ni)

# __name__ --> nazev modulu, ktery se zrovna vykonava
