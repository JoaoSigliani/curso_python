def n_plica(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = n_plica(2)
triplicar = n_plica(3)
quadruplicar = n_plica(4)

print(duplicar(3))