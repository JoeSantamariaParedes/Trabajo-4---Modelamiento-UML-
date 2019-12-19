import rey
import corona
import os
nombre_policia=os.sys.argv[1]
nro_balassobr=os.sys.argv[2]
nb=corona.Corona("ak-47","pintada",2500,2,nro_balassobr)
np=rey.Rey(nombre_policia,nb,28,5,3000)
print("el nombre es:"+np.getNombre())
print("material:"+nb.getMaterial())
np.setCorona(nb)
print(np.gobernar())