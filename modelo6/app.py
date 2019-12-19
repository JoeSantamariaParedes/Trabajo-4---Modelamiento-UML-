import os
import periodista
import camara
nombre_per=os.sys.argv[1]
marca_camara=os.sys.argv[2]
c1=camara.Camara(marca_camara,"12BN",1080,3000,"1kg")
p1=periodista.Periodista(nombre_per,21,2,c1,"m")
print("el periodista:"+p1.getNombre())
print("la camara:"+c1.getMarca())
p1.setCamara(c1)
print(p1.entrevistar())