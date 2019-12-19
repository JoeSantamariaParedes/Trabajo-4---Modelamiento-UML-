import os
import arquitecto
import plano
nomb_arq=os.sys.argv[1]
modelo_plano=os.sys.argv[2]
p1=plano.Plano(modelo_plano,5,1200,"A","hd")
a1=arquitecto.Arquitecto(nomb_arq,23,3,p1,"m")
print("arquitecto:"+a1.getNombre())
print("plano:"+p1.getModelo())
a1.setPlano(p1)
print(a1.proyectar())