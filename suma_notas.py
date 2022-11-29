"""""
. De un estudiante conocemos la nota 1, la nota 2, la nota de trabajos y el Examen final.
Calcular la nota definitiva (notaDef initiva) aplicando los porcentajes 20%, 20%, 30% y 30%,
respectivamente. Tenga en cuenta que 20% equivale a 0.2 y 30% es igual a 0.3.


"""""
n=int(input("ingrese la cantidad de nostas apromediar: "))

suma=0
i=1
while(i<=n):
    print("ingrese la nota numero: ",i)
    nota=float(input())
    suma=suma+nota*0.2*0.3
    i+=1
prom=suma/n
print("su nota final es: ",prom)


"""""
test: 

catidad notas: 3

nota1: 1.0

nota2: 4.0

nota3: 2.4

promedio: 0.148
"""""