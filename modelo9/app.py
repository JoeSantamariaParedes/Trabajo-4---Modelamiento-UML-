import conductor
import microfono
import os
nombre_policia=os.sys.argv[1]
nro_balassobr=os.sys.argv[2]
nb=microfono.Microfono("ak-47","inalambrico",2500,2,nro_balassobr)
np=conductor.Conductor(nombre_policia,nb,28,5,3000)
print("el nombre es:"+np.getNombre())
print("microfono:"+nb.getMarca())
np.setMicrofono(nb)
print(np.animar())