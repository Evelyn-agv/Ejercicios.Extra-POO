class Ejercicios:

    def decimalBinario(self, decimal):
        binario= " "
        while decimal//2!=0:
            binario= str(decimal % 2)+binario
            decimal= decimal//2 
        return "{}".format(decimal) + binario   #"ERROR"--> Un int no debe estar unido a un string por lo tanto se convierte a string el int

ejer= Ejercicios()
print(ejer.decimalBinario(5))