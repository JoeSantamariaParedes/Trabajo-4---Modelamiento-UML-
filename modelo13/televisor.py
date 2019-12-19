class Televisor():
        def __init__(self, marca, pantalla, material, capacidad, estilo):
            self.marca = marca
            self.pantalla = pantalla
            self.material = material
            self.capacidad = capacidad
            self.estilo = estilo

        def distraer(self):
            return ("al televisor " + self.marca + " se le rompio la pantalla de " + self.pantalla.getMarca())

        def getPantalla(self):
            return self.pantalla

        def setPantalla(self, pantalla):
            self.pantalla = pantalla

        def getMarca(self):
            return self.marca

        def setMarca(self, marca):
            self.marca = marca