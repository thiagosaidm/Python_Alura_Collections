# Aula 1 - Conjuntos

#querendo juntar os usuários que assistiram os cursos em uma só lista

usuarios_excel = [15, 65, 21, 68]
usuarios_powerbi = [50, 65, 21, 70]

lista_assistiram = []
lista_assistiram = usuarios_excel.copy() # método nativo que permite fazer uma cópia rasa (referencia)
lista_assistiram.extend(usuarios_powerbi) # método que junta duas listas


print("esses usuários assistiram ->> {}".format(lista_assistiram))

# porém nesse resultado, existem usuários nas duas listas, algo que não queremos
# logo existe outro método para se fazer isso, que é o uso de conjutos

for usuario in set(lista_assistiram):# set define o conjunto
    print(usuario)

# outro método para juntar os conjuntos é o uso do OU "|", vai funcionar como um extends


usuarios_excel = {15, 65, 21, 68}
usuarios_powerbi = {50, 65, 21, 70}

usuarios_que_assistiram = usuarios_excel | usuarios_powerbi

print("esses são os usuarios que assistiram: {} " . format(usuarios_que_assistiram))

# trabalhando com conjuntos podemos usar vários tipos de operação, dentre elas o OU: ( | )