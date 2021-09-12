class Cadena:
    def __init__(self, cad=" "):
        self.__cadena= cad
    
    def palindroma(self):
        invertir= self.__cadena[::] #"ERROR"-->Debe abarcar todas las posiciones
        invertir= invertir.replace(" "," ")
        original= self.__cadena.replace(" "," ")
        if original.lower()==invertir.lower(): 
            return "Palindroma"
        else:
            return "No es Palindroma"

eje=Cadena("anita lava la tina")
print(eje.palindroma())