import motor
import barco
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=motor.Motor(zapato_marca,42,"cuero","deportivo",1200)
z1=barco.Barco(marca_zapatera,zap1,"madera",20,"americano")
print("marca:"+zap1.getMarca())
print("el barco:"+z1.getMarca())
z1.setMotor(zap1)
print(z1.navegar())
