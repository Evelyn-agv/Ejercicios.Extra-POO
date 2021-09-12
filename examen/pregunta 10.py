class Examen:
    def __init__(self, lista=[]):
        self.lista= lista
        
    def listaMultiplo(self,numero):
        lista=[] 
        for num in self.lista:
            if not(num%numero!=0):  
                lista.append(num) #"ERROR"-->no es "numero" sino "num" porque no se desea el numero sino los multiplos del mismo
        return lista

exa= Examen([2,5,8,10,20])
print(exa.listaMultiplo(5))