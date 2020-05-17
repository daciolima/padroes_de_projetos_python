"""
Implementação de uma Classe Padrão Singleton Monostate 

"""
class Borg:
    
    __shared_state = {"1":"2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


# Testando
b = Borg()
b1 = Borg()
b.x = 4

print("Borg Objeto 'b': ", b) # b e b1 são objetos distintos
print("Borg Objeto 'b1': ", b1)
print("Estado do Objeto 'b': ", b.__dict__) # b e b1 compartilham o mesmo estado
print("Estado do Objeto 'b1': ", b1.__dict__)

