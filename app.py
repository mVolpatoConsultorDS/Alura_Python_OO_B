from Modelos.restaurante import Restaurante
valido = False
restaurante_praca = Restaurante('praca', 'Gourmet')
valido = restaurante_praca.receber_avaliacao('Gui', 10)
##Metodo retornando si pudo agregar la nota o no
print(f'{valido} \n')
restaurante_praca.receber_avaliacao('Lais', 8)
valido = restaurante_praca.receber_avaliacao('Emy', 2)
print(f'{valido} \n')
restaurante_mexina = Restaurante('mexican food', 'Mexicana')
restaurante_mexina.alternar_estado()
restaurante_japones = Restaurante('Japa', 'Japonesa')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()



#restaurante_praca = Restaurante('praca', 'Gourmet')
#restaurante_praca.nome = 'Praca'
#restaurante_praca.categoria = 'Gourmet'
#restaurante_pizza = Restaurante('pizza Express', 'Italiano')

#restaurante_praca.alternar_estado()

#Restaurante.listar_restaurantes()

#restanrantes = [restaurante_praca, restaurante_pizza]

##print(restanrantes)

##print(dir(restaurante_praca))

#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))

#print(restaurante_praca)
#print(restaurante_pizza)