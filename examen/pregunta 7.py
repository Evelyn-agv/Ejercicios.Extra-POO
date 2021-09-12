class Ordenar:
    def __init__(self, lista):
        self.lista= lista
        
    def insertarPos(self,pos,valor):
        auxlista=[]
        if len(self.lista)==pos: #"ERROR"--> Deberia ser [==] para ubicar en la posición que queremos y no debe ir [>=]
            self.lista.append(valor)
        else:
            for indice, ele in enumerate(self.lista):
                if indice==pos: 
                   auxlista.append(valor)
                auxlista.append(ele)
            self.lista=auxlista
        return self.lista
lista=[2,3,8,10,3]
ord1= Ordenar(lista)
print(ord1.insertarPos(2,20))