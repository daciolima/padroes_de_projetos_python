"""
Implementação de uma Classe Padrão Singleton
"""
# Classe Singleton Clássica
class Singleton:
    
    # Método new é um método especial para instanciar objetos
    def __new__(cls):
        # Método hasattr verifica se se um objeto tem determinada 
        # propriedade
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# Testando
s = Singleton()
print("Objeto criado: ", s)

s1 = Singleton()
print("Objeto criado: ", s1)

