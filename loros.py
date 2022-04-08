class Parrot:
    species = "bird" #Atributo de clase que va a estar fijo para cualquier instancia de la clase
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Saludos desde la clase padre!")
    def cantar(self,cancion):
        return "{} canta {}".format(self.name,cancion)
    
    def nadar(self):
        return "Voy a nadar!"

class Perico(Parrot):
    def __init__(self,name,age):
        super().__init__(name,age) # alternativamente funciona: Parrot.__init__(self,name,age)
        print("Soy el hijo periquito")


""""
blu=Parrot("Blu",10)
woo=Parrot("woo",15)

print("blu is a {}".format(blu.species))
print("woo es un {}".format(woo.species))

print("{} es un {}".format(blu.name,blu.species))
print("{} tiene {} años de edad".format(blu.name,blu.age))

print(blu.cantar("merengue"))
"""

#Herencia
ronald=Perico("ronald",2)
print(ronald.nadar())