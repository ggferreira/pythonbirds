class Pessoa:
    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.comprimentar(p))
    print(f'    {id(p)}')
    print(p.comprimentar())