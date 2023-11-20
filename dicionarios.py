# dicionários(dict) é um estrutura de dados, indexadas por keys
# as keys podem ser de qualquer tipo imutável
# chave:valor

# o principal uso de dicts é armazenar e recuperar valores a partir de chaves

agenda = {"Thiago": 33394, "Said": 94333}

print(list(agenda)) # mostra todas as chaves do dict

print(agenda) # retorna todos elementos do dict

print(agenda["Said"]) # deu acesso por meio da chave ao valor 94333


#construtor dict
#pode ser usado para criação de dicts

pets = dict([('Cachorro', 'dog'),('gato','diguidos')])
print(pets)
print(pets["Cachorro"])



