import soldado
import ejercito
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=soldado.Soldado(zapato_marca,42,"cuero","deportivo",1200)
z1=ejercito.Ejercito(marca_zapatera,zap1,"madera",20,"americano")
print("ejercito:"+z1.getNombre())
print("soldado:"+zap1.getNombre())
z1.setSoldado(zap1)
print(z1.planificar())