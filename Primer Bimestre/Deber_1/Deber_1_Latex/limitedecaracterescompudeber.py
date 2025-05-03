import sys

print("Máximo float que resiste mi computador", sys.float_info.max)
print("Mínimo float que resiste mi computador", sys.float_info.min)

a = sys.float_info.max *2
print ("Al operar con los valores de desbordamiento el resultado que obtenemos es:",a)
b= a-a
print ("Ahora veamos que pasa si hago operaciones con el valor que me da infinito como respuesta osea a obtenemos:",b)
c = sys.maxsize
print ("El valor entero antes de agotar la memoria es:",c)
d=c*2
print ("Esto sucede cuando se supera el valor maximo de memoria",d)
e=d*2
print ("Esto sucede cuando se supera el valor maximo de memoria X2",e)
f=e*2
print ("Esto sucede cuando se supera el valor maximo de memoria X3",f)
