dia = input('Digite o seu dia de nascimento: ')
mes = input('Digite o seu mês de nascimento: ')
ano = input('Digite o seu ano de nascimento: ')

mes_por_extenso = {'01': 'Janeiro'}

mes_atualizado = str(mes_por_extenso)
print(dia + mes_atualizado + ano)
