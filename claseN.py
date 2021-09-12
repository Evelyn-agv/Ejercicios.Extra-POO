class Notas():

    def __init__(self, asignatura,nota):
        self.asignatura= asignatura
        self.nota= nota

    def adicionarN(self, asignatura,nota):
        n= int(input("Cuantas notas desea agregar: "))
        for i in range(n):
            no= float(input("Nota: "))
            nota.append(no)
            i+= 1
        txt = "Se han agregado las suiguientes notas{0}, a la asignatura {1}".format(nota,asignatura)
        print(txt)

    def modificarN(self, nota):
        print(nota)
        m=int(input("Ingrese el parametro que quiere modificar: "))
        ed= float(input("Ingrese la cantidad modificada: "))
        nota[m-1] = ed
        txt = "La nota {},ha sido modificada".format(nota)
        print(txt)

    def eliminarN(self, asignatura,nota):
        print(nota)
        e=int(input("Ingrese la nota que quiere eliminar: "))
        nota.remove(e)
        print(nota)
        txt = "Se han eliminado la siguiente nota,{0}, en la asignatura {1}".format(nota,asignatura)
        print(txt)

    def media(self,asignatura):
        c = 0
        suma = 0
        for i in self.nota:
            suma += i
            c += 1
        media = suma/(c)
        txt = "El promedio de las notas es {0}, en la asignatura {1}".format(media,asignatura)
        print(txt)
        return media

    def imprimir(self,media):
        self.media = media
        txt = "La nota del estudiante en la asignatura {0} es de {1}".format(self.asignatura, media)
        print(txt)

def run():
    r= "si"
    media = 0
    asignatura= input("Ingrese la asignatura que se encuentra el estudiante: ")
    nota=[]
    Notas(asignatura, nota)
    while r == "si":
        print("Quiere adicionar, modificar, eliminar la nota o imprimir[A/M/E/D/I]: ")
        print("A = adicionar")
        print("M = modificar")
        print("E = eliminar")
        print("D= media")
        print("I = imprimir")
        accion= input()
        accion= accion.capitalize()
        instancia = Notas(asignatura,nota)
        if accion == "A":
            instancia.adicionarN(asignatura,nota)
        elif accion == "M":
            instancia.modificarN(nota)
        elif accion == "E":
            instancia.eliminarN(asignatura,nota)
        elif accion == "D":
            media = instancia.media(asignatura)
        else:
            instancia.imprimir(media)
        r = str(input("Desea continuar (si/no): "))
        r = r.lower()

if __name__ == "__main__":
    run()