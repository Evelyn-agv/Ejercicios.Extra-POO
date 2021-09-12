def numero_abundante(n):
    count=1
    suma=0
    while count < n:
        if n % count==0:
            suma+= count
        count+=1
    if suma > n:
        return True
    else:
        return False
print(numero_abundante(30))