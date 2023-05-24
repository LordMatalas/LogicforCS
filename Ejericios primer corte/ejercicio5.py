class Tree(object):
    def __init__(self, iz, der):
        self.left = iz
        self.right = der

Hoja = Tree(None, None)
Rama = Tree(Hoja, Hoja)
Arbol1 = Tree(Rama, Hoja)
Arbol2 = Tree(Hoja, Rama)
Arbol3 = Tree(Rama, Rama)
ArbolSantiyDani = Tree(Hoja, None)

def num_aristas(A):
    if A.left == None:
        return 0
    else:
        return 2 + num_aristas(A.left) + num_aristas(A.right)


def numHojas(A):
    if A.left == Hoja:
        return 1
    if A.left == Rama:
        return numHojas(A.left) + numHojas (A.right)
    
def num_nodos(A):
    if A.right == None:
        return 1
    else: 
        return 1 + num_nodos(A.left) + num_nodos(A.right)

A = Tree(Tree(Tree(Tree(None, None), Tree(None, None)), Tree(Tree(None, None), Tree(None, None))), Tree(Tree(Tree(None, None), Tree(None, None)), Tree(None, None)))

print(num_nodos(A))
# if Arb.left == None:
#     print("Hoja")
# else:
#     print("Rama")


# def altura(A):
#     if A.right == None:
#         return 0
#     else:
#         return 1 + max(altura(A.left), altura(A.right))

