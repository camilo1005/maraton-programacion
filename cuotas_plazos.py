"""""
Dado el monto de un credito, el plazo y tasa de interes anual, calcular la cuota fija mensual
que se debe cancelar a una entidad financiera.



"""""

monto =int(input("ingrese el monto del prestamo: "))
meses =int(input("cantidad de meses: "))
intereses=(monto*(meses*0.01))
total=monto+intereses

print("intereses : {:.1f} ".format(intereses))
print("total apagar por mes:  ",total)



"""""
test: 

monto: 1000

meses: 6

resultado:

intereses:60.0

total apagar: 1060.0

"""""