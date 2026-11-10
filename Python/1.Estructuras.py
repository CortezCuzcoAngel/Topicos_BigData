print("Estructuras condicionales")

#Condicional simple 
nota_TBI = 17
if nota_TBI >= 10.51:
    print("Aprobado")
else:
    print("Reprobado")

#Condicional doble
edad = 18
if edad >=18:
    print("Mayor de edad, puedes tomar alcohol")
else:
    print("No apto para menores")

# Condiconal anidada
nota = 18
if nota > 17 and nota <= 20:
    print("Excelente")

elif nota > 14 and nota <= 17:
    print("Muy bien")

elif nota > 13 and nota <=15:
    print("Bien")

elif nota > 10.5 and nota <= 13:
    print("Aprobado")

else:
    print("Lumno con bajo rendimiento academico, reprobado")


#Condicional multiple

"""
Python 3.9.0 a versiones anteriores mo existe condicional multiple
todo se trabaja con condicionales anidadas
"""

num = 4
match num:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case 4:
        print("Cuatro")
    case _:
        print("No es un numero valido")