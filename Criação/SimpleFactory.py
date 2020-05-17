from abc import ABCMeta, abstractmethod


# Metaclass ABCMeta é um parametro especial para criação de classes Abstract
class Animal(metaclass=ABCMeta):
    
    @abstractmethod
    def falar(self):
        pass
    

class Cachorro(Animal):
    
    def falar(self):
        print('Uau! Uau')
        
    
class Gato(Animal):
    
    def falar(self):
        print('Miau, Miau')


# Fábrica Forest definida
class FlorestaFactory(object):

    def criar_som(self, object_type):
        return eval(object_type)().falar()


# Testando
if __name__ == '__main__':
    bicho = FlorestaFactory()
    animal = input('De qual animal deseja ouvir o som, Cachorro ou Gato')
    bicho.criar_som(animal)




