from abc import ABCMeta, abstractmethod


# Parte 1
# Abstract Class
class Sessao(metaclass=ABCMeta):

    @abstractmethod
    def descricao(self):
        pass


# Concrete Class
class SessaoPessoal(Sessao):

    def descricao(self):
        print('Sessao Pessoal')


# Concrete Class
class SessaoAlbum(Sessao):

    def descricao(self):
        print('Sessão Album')


# Concrete Class
class SessaoPatente(Sessao):

    def descricao(self):
        print('Sessao Patente')


# Concrete Class
class SessaoPublicacao(Sessao):

    def descricao(self):
        print('Sessao Publicacao')


# Parte 2
# Creator Class
class Perfil(metaclass=ABCMeta):

    def __init__(self):
        self.sessoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_sessoes(self):
        return self.sessoes

    def add_sessoes(self, sessao):
        self.sessoes.append(sessao)


# Concrete Creator
class Linkedin(Perfil):

    def criar_perfil(self):
        self.add_sessoes(SessaoPessoal())
        self.add_sessoes(SessaoPatente())
        self.add_sessoes(SessaoPublicacao())


# Concrete Creator
class Facebook(Perfil):

    def criar_perfil(self):
        self.add_sessoes(SessaoPessoal())
        self.add_sessoes(SessaoAlbum())


# Testando
if __name__ == '__main__':
    tipo_perfil = input('Qual perfil você deseja criar, Linkedin ou Facebook?')
    perfil = eval(tipo_perfil.capitalize())()
    print('Criando perfil...', type(perfil).__name__)
    print("Perfil contem as sessões -- ", perfil.get_sessoes())