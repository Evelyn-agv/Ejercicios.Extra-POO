class Cadena:
    def __init__(self, cadena):
        self.cadena= cadena
        self.__listaMinuscula= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
                                "r","s","t","u","v","w","x","y","z"]
        self.__listaMayuscula= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                 "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    def fin_encontrar(self,buscar):
        for i,v in enumerate(self.cadena):
            if v==buscar:
                return i #"ERROR"-->Como busca posición debe ir [i], porque [v] es valor
        return -1
cadena= input("Ingrese un cadena: ")
c=Cadena(cadena)
buscar= input("Ingrese el caracter a buscar: ")
print(c.fin_encontrar(buscar))