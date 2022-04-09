#Encapsulamiento
class Computer:
    def __init__(self):
        self.__maximo=9000 #Valor por defecto pero modificable
    
    def venta(self): # Registra el máximo actual
        print("El precio de venta es {}".format(self.__maximo))
    
    #Setter
    def setMaximo(self,precio):
        self.__maximo=precio

c=Computer()
c.venta()  #Sigue saliendo 9000 porque es una variable privada


c.__maximo=1000
c.venta()
print(c.__maximo)