class Ordenar:
    def __init__(self, lista):
        self.lista= lista
        
    def top(self):
        auxlista=[]
        for pos in range(1,len(self.lista)): 
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return self.lista #"FALSO" -->Debe retonar la lista, eliminando el primer valor, por lo tanto no debe ir [0]
lista=[2,3,8,10,3]
ord1= Ordenar(lista)
print(ord1.top())