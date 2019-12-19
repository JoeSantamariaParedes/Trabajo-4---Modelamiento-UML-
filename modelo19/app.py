import radio
import parlante
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=parlante.Parlante(zapato_marca,42,"cuero","deportivo",1200)
z1=radio.Radio(marca_zapatera,zap1,"madera",20,"americano")
print("radio:"+z1.getMarca())
print("parlante:"+zap1.getMarca())
z1.setParlante(zap1)
print(z1.reproducir())