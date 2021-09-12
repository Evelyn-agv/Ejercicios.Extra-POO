import math
class Datos:
    def __init__(self,nom):
        self.nombre= nom
    
    def edad(self):
        ed= int(input("Ingrese la edad: "))
        if ed<13:
            return "{} es un niño porque tiene la edad de {}".format(self.nombre, ed)
        else:
            return "{} es un adolescente porque tiene la edad de {}".format(self.nombre, ed)
    
    def nombre(self):
        return "El nombre de la persona es: " .format(self.nombre)
    
    def hijos(self):
        hijos= input("Tiene hijos [S/N]: ").lower()
        if hijos=="s":
            cant= int(input("Cuántos hijos tiene: "))
            return "{} tiene {} hijos".format(self.nombre, cant)
        else:
            return "{} no tiene hijos".format(self.nombre)
    
    def apartamento(self):
        letra= input("Uds tiene un apartamento asignado [S/N]: ").lower()
        if letra=="s":
            habitacion= input("Ingrese su letra de su apartamento: ").lower()
            return "{} pertenece al apartamento {}".format(self.nombre, habitacion)
        else:
            lis=["h","i","j","k","l","n","o","p"]
            hab= input("Tenemos los apartamentos [h,i,j,k,l,n,o,p]: ").lower()
            if hab in lis:
                return "{} tendra el apartamento {}".format(self.nombre, hab)
            else:
                return ("Ya existe un apartamento con la misma letra")
    
    def edificio(self):
        base= float(input("Cuanto mide aproxidamente su base: "))
        angulo= float(input("Cuanto de angulo aproximadamente tiene: "))
        altura= (math.tan(angulo)*base)
        aux= round(altura,2)
        return "Las medidas del edificio son {} de altura y base {} con un angulo aproximado a {} grados".format(aux,base,angulo)





nom= input("Ingrese un nombre: ")
c= Datos(nom)
#print(c.edad())
#print(c.nombre())
#print(c.hijos())
#print(c.apartamento())
print(c.edificio())
