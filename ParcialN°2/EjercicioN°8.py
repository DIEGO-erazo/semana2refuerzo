multiLine = """Es porque un pajarito de la montaña ha hecho
en el hueco de un árbol, su nido matinal,
que el árbol amanece con música en el pecho,
como que si tuviera corazón musical.

Si el dulce pajarito por entre el hueco asoma,
para beber rocío, para beber aroma,
el árbol de la sierra me da la sensación
de que se le ha salido, cantando, el corazón"""

resultado1 = multiLine.count("a")
print("El número de veces que aparece la letra 'a' es:", resultado1)

resultado2 = multiLine.splitlines()
print("El mensaje dividido queda de la siguiente manera :", resultado2)
