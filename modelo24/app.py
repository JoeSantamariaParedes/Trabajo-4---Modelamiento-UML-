import restaurant
import mesero
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=mesero.Mesero(zapato_marca,42,"cuero","deportivo",1200)
z1=restaurant.Restaurant(marca_zapatera,zap1,"madera",20,"americano")
print("restaurant:"+z1.getNombre())
print("mesero:"+zap1.getNombre())
z1.setMesero(zap1)
print(z1.cocinar())