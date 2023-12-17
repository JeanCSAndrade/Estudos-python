lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]
def zipper(lista1, lista2):
    inter = min(len(lista1), len(lista2))
    return[
         (lista1[i] + lista2[i]) for i in range(inter)
    ]

print(zipper(lista1, lista2))