class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Gabriel')
    print(Pessoa.comprimentar(p))
    print(f'    {id(p)}')
    print(p.comprimentar())
    print(p.nome)