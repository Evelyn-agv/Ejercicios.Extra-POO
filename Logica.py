import os
def expresiones(a,b,c,d,e):
    re= a-b*c/d+e*c
    ex=(a*b+(d//e-a))**c
    mo= e % a-d/e*c+b
    return "El resultado de la división es: {}, el exponente es: {} y la división con modulo es: {}".format(re,round(ex,2),round(mo,2))

def insertarParentesis(a,b,c,d,e,f,g,h,i,j):
    m= (a // b)*((c%e)-(f*g))
    r= (a-b*c)/(d+e*f)
    z= (a*(b+c))+(abs(d*e/f)-g*(h+i/j))
    return "El resultado de la multiplicación es: {}, división es: {} y la suma es: {}".format(round(m,2),round(r,2),round(z,2))
    
def parentesis(a,b,c,d,e,f,g,h):
    m= (a % b /c)*(d+e)
    r= (a/b)*c-d
    z= (a+b*(c+d))-(e+f/g*h)
    return "El resultado de la multiplicación con modulo es: {}, la multiplicación es: {} y la resta es: {}".format(round(m,2),round(r,2),round(z,2))

def expresionesCondicionales(a,b,c,d,e,f,g,h,i):
    di= (a/b*c-d)/(g//d%e)
    ma= (f//c)>(c/g)**h*(h+i%a)
    cal= i<=c+g-h
    return "El resultado de la igualdad es: {}, la diferencia con exponente es: {} y la diferencia es: {}".format(round(di,2),round(ma,2),round(cal,2))

def expresionesOperadores(a,b,c,d,e,f,g,h,i,j):
    x= not(a>=b**c) or (d-e*c//f != g*c//c)
    y= (h>=b*g**c and e>g and a>h)or not(b*g<i+j*c/g**c)
    z= not((b*g//c*f<j)or(a>c*b<=a*c/a))
    return "El resultado del operador or es: {}, los operadores or 2: {} y operadores negación: {}".format(round(x,2),round(y,2),round(z,2))


def menu():
    print("1. Expresiones\n2. Insertar Parentesis\n3. Parentesis\n4. Expresiones condionales\n5. Expresiones con operadores")
    op= input("--> ")
    return op

op=" "
while op != 6:
    opcion=menu()
    os.system("cls")
    a= float(input("Ingrese el valor de a: "))
    b= float(input("Ingrese el valor de b: "))
    c= float(input("Ingrese el valor de c: "))
    d= float(input("Ingrese el valor de d: "))
    e= float(input("Ingrese el valor de e: "))
    f= float(input("Ingrese el valor de f: "))
    g= float(input("Ingrese el valor de g: "))
    h= float(input("Ingrese el valor de h: "))
    i= float(input("Ingrese el valor de i: "))
    j= float(input("Ingrese el valor de j: "))
    if opcion=="1":
       resultado= expresiones(a,b,c,d,e)
    elif opcion=="2":
       resultado= insertarParentesis(a,b,c,d,e,f,g,h,i,j)
    elif opcion=="3":
       resultado= parentesis(a,b,c,d,e,f,g,h)
    elif opcion=="4":
       resultado= expresionesCondicionales(a,b,c,d,e,f,g,h,i)
    else:
       resultado= expresionesOperadores(a,b,c,d,e,f,g,h,i,j)
    os.system("cls")
    print(resultado)


