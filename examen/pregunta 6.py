def fact_1(n):
    factorial_total=1
    while n>1:
        factorial_total*=n
        n-=1 #"ERROR"-->El espacio estaba mal colocado
    return factorial_total

print(fact_1(4))