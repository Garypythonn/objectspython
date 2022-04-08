class Visitante():
    def blast(self, local):
        print("Hola soy turista")
        local.saludado() ####################


class Local():
    def saludado(self):
        print("Gracias por visitar")

tur = Visitante()
host = Local()
tur.blast(host)