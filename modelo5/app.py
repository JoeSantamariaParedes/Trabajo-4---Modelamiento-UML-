import policia
import arma
import os
nombre_policia=os.sys.argv[1]
nro_balassobr=os.sys.argv[2]
nb=arma.Arma("ak-47","roja",2500,2,nro_balassobr)
np=policia.Policia(nombre_policia,nb,28,5,3000)
print("el nombre es:"+np.getNombre())
print("el numero de balas sobrantes:"+nb.getNro_balas())
np.setArma(nb)
print(np.defender())