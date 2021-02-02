import random as r
import math as m


def err(base_number):
    return(base_number - m.pi )

def monte_carlo(numbers_simulations):
    cont = 0
    for i in range(0, numbers_simulations):
        x = r.random()**2
        y = r.random()**2
        if m.sqrt(x + y) < 1.0:
            cont += 1
    pi = (float(cont) / numbers_simulations) * 4
    return pi
    
    
for i in [50, 100, 1000, 100000 ]:
    pi_aprox = monte_carlo(i)
    print("{} Simulações -> \t ".format(i) + "PI APROXIMADO: " +str(pi_aprox)+ "\t  ERRO: "+ str(err(pi_aprox)) )