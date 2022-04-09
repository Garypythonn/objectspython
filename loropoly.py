class Parrot:
    
    def volar(self):
        print("Parrot puede volar")
    
    def swim(self):
        print("Parrot no puede nadar")

class Pingu:

    def volar(self):
        print("Pingu no puede volar")
    
    def swim(self):
        print("Pingu puede nadar")

# common interface.... es una función que recibe como parámetro un objeto y ejecuta el método... si es que existe
def volaring_test(pajarito):
    pajarito.volar()
    pajarito.swim()
    

#instantiate objects
blu = Parrot()
peggy = Pingu()

# passing the object
volaring_test(blu)
volaring_test(peggy)