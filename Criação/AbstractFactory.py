from abc import ABCMeta, abstractmethod


# Parte 1
# Classe Abstract
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_vegana(self):
        pass

    @abstractmethod
    def criar_pizza_nao_vegana(self):
        pass


# Parte 2
# Pizzaria Indiana  (Concrete Factory)
class PizzaIndianaFactory(PizzaFactory):

    def criar_pizza_vegana(self):
        return PizzaDeluxVegana()

    def criar_pizza_nao_vegana(self):
        return PizzaFrango()


# Pizzaria Americana  (Concrete Factory)
class PizzaAmericanaFactory(PizzaFactory):

    def criar_pizza_vegana(self):
        return PizzaVeganaMexicana()

    def criar_pizza_nao_vegana(self):
        return PizzaPresunto()


# Parte 3
class PizzaVegana(metaclass=ABCMeta):  # (Abstract Product)

    @abstractmethod
    def preparar(self, PizzaVegana):  # Pizzas Veganas serão preparadas com ingredientes vegetarianos
        pass


class PizzaNaoVegana(metaclass=ABCMeta):  # (Abstract Product)

    @abstractmethod
    def servir(self, PizzaVegana):  # Pizzas Não Veganas serão preparadas sobre pizza vegetarianas
        pass


# Preparação e servir as pizzas da Pizzaria Indiana Factory
class PizzaDeluxVegana(PizzaVegana):  # Concrete Product 1

    def preparar(self):
        print("Prepara ", type(self).__name__)


class PizzaFrango(PizzaNaoVegana):  # Another Concrete Product 1

    def servir(self, PizzaVegana):
        print(type(self).__name__, "é servida Frango sobre a", type(PizzaVegana).__name__)


# Preparação e servir as pizzas da Pizzaria Americana Factory
class PizzaVeganaMexicana(PizzaVegana):  # Concrete Product 2

    def preparar(self):
        print("Prepara ", type(self).__name__ )


class PizzaPresunto(PizzaNaoVegana):  # Another Concrete Product 2

    def servir(self, PizzaVegana):
        print(type(self).__name__, "é servido presunto sobre a", type(PizzaVegana).__name__)



# Store das Pizzas
class LojaPizza:

    def __init__(self):
        pass

    def criar_pizzas(self):
        for factory in [PizzaIndianaFactory(), PizzaAmericanaFactory()]:
            print(type(factory).__name__)
            self.factory = factory
            self.PizzaNaoVegana = self.factory.criar_pizza_nao_vegana()
            self.PizzaVegana = self.factory.criar_pizza_vegana()
            self.PizzaVegana.preparar()
            self.PizzaNaoVegana.servir(self.PizzaVegana)
            print('---------------------------------------')


# Testando
pizza = LojaPizza()
pizza.criar_pizzas()

