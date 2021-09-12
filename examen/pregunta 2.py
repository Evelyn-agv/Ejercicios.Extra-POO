class Examen:
    def __init__(self, lista=[]):
        self.lista= lista
        
    def invertirCadena(self,cadena):
        invertida= " "
        cont= len(cadena)
        indice=-1
        while cont>=1:
            invertida+= cadena[indice]
            indice-=1 #"ERROR"--> El signo deberia ser [-] para que recorra de atras para adelante
            cont-=1
        return invertida
lista=[]
exa= Examen(lista)
print(exa.invertirCadena("daniel"))