from lisp import car, cdr, cons

# soma todos os itens de uma lista
def sum(lista):
    if lista == []:
        return 0
    else:
        return car(lista) + sum(cdr(lista))
print(sum([1,2]))

# retorna o tamanho da lista
def size(lista):
    if lista == []:
        return 0
    else:
        return 1 + size(cdr(lista))

# retorna ultimo item da lista
def ultimo(lista):
    if cdr(lista) == []:
        return car(lista)
    else:
        return ultimo(cdr(lista))

# remove item da lista
def remove(x, lista):
    if lista == []:
        return []
    else:
        if car(lista) == x:
            return cdr(lista)
        else:
            return cons(x, remove(x, cdr(lista)))

# lista[:-1]
def remove_ultimo(lista):
    if cdr(lista) == []:
        return []
    else:
        return cons(car(lista), remove_ultimo(cdr(lista)))

# lista[::-1]
def inverte(lista):
    if lista == []:
        return []
    else:
        return cons(ultimo(lista), inverte(remove_ultimo(lista)))
