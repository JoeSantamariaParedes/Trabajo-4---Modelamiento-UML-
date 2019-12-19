import bosque
import arbol
import os
nombre_policia=os.sys.argv[1]
nro_balassobr=os.sys.argv[2]
nb=arbol.Arbol("ak-47","roja",2500,2,nro_balassobr)
np=bosque.Bosque(nombre_policia,nb,28,5,3000)
print("el nombre es:"+np.getNombre())
print("las ramas:"+nb.getRamas())
np.setArbol(nb)
print(np.defender())