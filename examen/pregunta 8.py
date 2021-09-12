class Cadena:
    def __init__(self, cadena):
        self.cadena= cadena
        self.Minuscula= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
                                "r","s","t","u","v","w","x","y","z"]
        self.Mayuscula= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                 "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    def mayMin(self):
        cmay,cmin=0,0
        for i,v in enumerate(self.cadena):
            if v in self.Mayuscula: #"ERROR"-->Como busca cantidad debe ir [v], porque [i] es la posición
                cmay+=1
            elif v in self.Minuscula: #"ERROR"-->Como busca cantidad debe ir [v], porque [i] es la posición
                cmin+=1  
        return cmay,cmin

tarea=Cadena("Examen de POO")
print(tarea.mayMin())