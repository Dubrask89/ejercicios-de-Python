#Calcular los dias vividos de una persona desde su nacimiento

import datetime
a =int (input ("Año de nacimiento: "))
m =int (input ("Mes de nacimiento: "))
d =int (input ("Dia de nacimiento: "))
fecha_nacimiento= datetime.datetime(a,m,d)
fecha_actual=datetime.datetime.now()
dif= fecha_actual-fecha_nacimiento
print ("Dias vividos: ", dif.days)