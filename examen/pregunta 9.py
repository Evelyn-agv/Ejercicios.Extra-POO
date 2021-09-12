class Examen:
    def __init__(self, lista=[]):
        self.lista= lista
        
    def ListaMenor(self,num):
        listaMenor=[] #"ERROR"-->Es una lista no una tupla
        for menor in self.lista:
            if num > menor:  #"ERROR"-->Se busca los numeros menores, no mayores
                listaMenor.append(menor)
        return listaMenor

exa= Examen([2,5,20,16])
print(exa.ListaMenor(13))