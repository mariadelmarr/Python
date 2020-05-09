cantPizzas = int(input("Cuantas pizzas desea?"))
tamPizzas = int(input("Que tamaño de pizza desea?"))
cantPersonas = int(input("Cuantas personas van a comer pizza?"))

porcionPersona = (cantPizzas * tamPizzas) / cantPersonas
sobran = (cantPizzas * tamPizzas) - cantPersonas

print("Le toca: "+str(int(porcionPersona))+ " slide(s) a cada persona y sobra: "+str(int(sobran))+" slide(s)")
