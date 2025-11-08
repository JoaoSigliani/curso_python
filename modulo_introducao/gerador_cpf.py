import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

primeiro_digito = 0
indice_multiplica_1 = 10
soma_digitos_1 = 0

for digito in nove_digitos:
    soma_digitos_1 += indice_multiplica_1 * int(digito)
    indice_multiplica_1 -= 1

verificador = (soma_digitos_1 * 10) % 11
primeiro_digito = verificador if verificador <= 9 else 0

segundo_dígito = 0
dez_digitos = nove_digitos + str(primeiro_digito)
indice_multiplica_2 = 11
soma_digitos_2 = 0

for digito in dez_digitos:
    soma_digitos_2 += indice_multiplica_2 * int(digito)
    indice_multiplica_2 -= 1

verificador = (soma_digitos_2 * 10) % 11
segundo_dígito = verificador if verificador <= 9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_dígito}'
print(cpf_gerado)