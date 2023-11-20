# Aula 1 - Conjuntos
# conjuntos são elementos mutáveis

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

# outro método para juntar os conjuntos é o uso da operação OU "|", vai funcionar como um extends


usuarios_excel = {15, 65, 21, 68}
usuarios_powerbi = {50, 65, 21, 70}

usuarios_que_assistiram = usuarios_excel | usuarios_powerbi

print("esses são os usuarios que assistiram: {} " . format(usuarios_que_assistiram))

# trabalhando com conjuntos podemos usar vários tipos de operação, dentre elas o OU: ( | )

#operação &: Intersecção dos dois conjuntos
# usuários que estão nos dois conjuntos

fizeram_os_dois_cursos = usuarios_excel & usuarios_powerbi

print(fizeram_os_dois_cursos)

#operação ^ ou exclusivo: vai capturar os que estão em um ou outro, mas não nos dois

fizeram_curso_mas_n_os_dois = usuarios_excel ^ usuarios_powerbi

print(fizeram_curso_mas_n_os_dois)

#operação - : retira os elementos que estão num conjunto mas não estão no outro

fizeram_excel_mas_n_powerbi =  usuarios_excel - usuarios_powerbi

print(fizeram_excel_mas_n_powerbi)

# Adicionar elementos no conjunto
# O método append não existe no conjunto, pois o mesmo não lida com ordem. Para isso usa o método "add.(numero)"


usuarios_excel.add(33394)

print(usuarios_excel)

#Frozenset - é a nomenclatura e atributo dado ao conjunto que caracteriza-se como imutável
usuarios_sql = {1,3,5,6}
usuarios_sql = frozenset(usuarios_sql)

print(usuarios_sql)

#com isso ele perde os métodos de um set mutável

#usuarios_sql.add(55)

print(usuarios_sql) #AttributeError: 'frozenset' object has no attribute 'add'

#Também é possível ter conjuntos de outros valores como objetos e outros tipos de valores como até mesmo strings:

texto = "EU SOU GROOT"

texto = (texto.split())

print(texto)



