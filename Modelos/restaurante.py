class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praca', 'Gourmet')
#restaurante_praca.nome = 'Praca'
#restaurante_praca.categoria = 'Gourmet'
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

Restaurante.listar_restaurantes()

#restanrantes = [restaurante_praca, restaurante_pizza]

##print(restanrantes)

##print(dir(restaurante_praca))

#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))

#print(restaurante_praca)
#print(restaurante_pizza)