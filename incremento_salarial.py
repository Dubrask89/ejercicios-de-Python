#Calcule el incremento salarial de una persona: si su salario es 15 mil sera del 20% y si es mayor a 15 mil
#el incremento sera del 15%

salario=int(input("Ingrese su salario en números: "))
if salario<15000:
    incremento=salario*0.20
    salario=salario+incremento
    print("El incrementos es: ",incremento)
    print("Su salario total es de: ", salario)
else: 
    incremento=salario*0.15
    salario=salario+incremento
    print("El incrementos es: ",incremento)
    print("Su salario total es de: ", salario)