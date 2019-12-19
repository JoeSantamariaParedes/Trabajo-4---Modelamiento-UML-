import bata
import doctor
import os
nro_talla=os.sys.argv[1]
nombre_doctor=os.sys.argv[2]
t1=bata.Bata(nro_talla,5,150,"A20N","algodon")
d1=doctor.Doctor(nombre_doctor,t1,"masculino",20,2000)
print("talla:"+t1.getTalla())
print("doctor:"+d1.getNombre())
d1.setBata(t1)
print(d1.curar())
