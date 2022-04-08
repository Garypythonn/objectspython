from importlib.util import spec_from_file_location


class Parrot:
    species = "bird" #Atributo de clase que va a estar fijo para cualquier instancia de la clase
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def cantar(self,cancion):
        return "{} canta {}".format(self.name,cancion)



blu=Parrot("Blu",10)
woo=Parrot("woo",15)

print("blu is a {}".format(blu.species))
print("woo es un {}".format(woo.species))

print("{} es un {}".format(blu.name,blu.species))
print("{} tiene {} años de edad".format(blu.name,blu.age))

print(blu.cantar("merengue"))