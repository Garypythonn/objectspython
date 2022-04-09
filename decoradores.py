"""
def sumar(a,b):
    return a+b

def resta(a,b):
    return a-b

#operacion=sumar

#print(operacion(2,3))

def ejecuta(operacion,a,b):
    print("Operación genérica")
    print(operacion(a,b))

ejecuta(sumar,23,32)
"""
################################################################
"""
def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print("antes")
        result=funcion_b(*args, **kwargs)
        print("despues")

        return result
    return funcion_c


@funcion_a
def suma(a,b):
    return a+b

print(suma(4,7))
"""
######################################
import time

def tiempo(funcion):
    def envoltura(*args, **kwargs):
        comienzo=time.time()
        result=funcion(*args, **kwargs) 
        print('tiempo:',time.time()-comienzo-0.2)
        return result
    return envoltura

@tiempo
def suma(a,b):
    time.sleep(0.2)
    return a+b

print(suma(10,34))









