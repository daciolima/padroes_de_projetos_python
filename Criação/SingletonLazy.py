"""
Implementação de uma Classe Padrão Singleton com Instanciação preguiçosa

"""

class Singleton:
    
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__method called..")
        else:
            print("Instance already created: ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


# Testando
s = Singleton() # Classe é inicializada, mas objeto não é criado.
print("Objeto criado: ", Singleton.getInstance()) # O Objeto é criado quando usado o método getInstance()
s1 = Singleton() # Instância já criada!