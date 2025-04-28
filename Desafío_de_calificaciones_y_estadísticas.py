repetir = 0
print("n Calcular el promedio")
#promedio de notas
while(repetir==0):

    # Solicitar al usuario que ingrese las calificaciones
    entrada = input("\nIngrese las calificaciones separadas por comas: ")

    # Separar la cadena de entrada en una lista
    lista_entrada = entrada.split(",")

    calificaciones = []
    notas_promedio=0
    nota_final=0
    # Recorrer cada valor ingresado
    for i, valor in enumerate(lista_entrada):
        valor = valor.strip()
        valos=valor.replace('.', '', 1).isdigit()  # permite un solo punto decimal
        
        if valor==" " or valor=="":
            print(f"Error: La calificación número {i + 1} ('{valor}') no es un número válido.")
            valor = input(f"Por favor, ingrese nuevamente la calificación {i + 1}: ").strip()
            
        calificacion=float(valor)
        
        if calificacion < 0 or calificacion > 100:
            print(f"Error: La calificación número {i + 1} ('{calificacion}') no es un número válido.")
            valor = input(f"Por favor, ingrese nuevamente la calificación {i + 1}: ").strip()
        
        calificaciones.append(float(valor))
        
   
    
    n_calificaciones=len(calificaciones)
    for i  in range(n_calificaciones):
        notas_promedio=notas_promedio+calificaciones[i]
        nota_final=notas_promedio/n_calificaciones
    
    print(f"Nota promedio: {nota_final}") 
      
                        
    repetir=int(input("\nDeseas repetir?(si=0, no=cualquier numero)"))


repetir = 0
print("\nDeterminar el estado de aprobación")
#Determinar el estado de aprobación:
while(repetir==0): 
       
    calficacion_1=float(input("\nIngresar una nota de 1 al 100: "))

    while calficacion_1<0 and calficacion_1<100:
        calficacion_1=float(input("Error!! ingresar una nota de 1 al 100: "))
        
    if calficacion_1>=60: 
        print("Aprobo la materia.")
    else: 
        print("Reprobo la materia.")
        
    repetir=int(input("\nDeseas repetir?(si=0, no=cualquier numero)"))
    
#contar calificaciones mayores
print("Contar calificaciones mayores")
repetir = 0
while(repetir==0):

# Solicitar al usuario que ingrese las calificaciones
    entrada = input("\nIngrese las calificaciones separadas por comas: ")

    # Separar la cadena de entrada en una lista
    lista_entrada = entrada.split(",")

    notas_promedio=0
    calificacion=0
    contador=0
    calificaciones = []
    indices=[]
    Nota=[]
    
    # Recorrer cada valor ingresado
    for i, valor in enumerate(lista_entrada):
        valor = valor.strip()
        valos=valor.replace('.', '', 1).isdigit()  # permite un solo punto decimal
        
        if valor==" " or valor=="":
            print(f"Error: La calificación número {i + 1} ('{valor}') no es un número válido.")
            valor = input(f"Por favor, ingrese nuevamente la calificación {i + 1}: ").strip()
            
        calificacion=float(valor)
        
        if calificacion < 0 or calificacion > 100:
            print(f"Error: La calificación número {i + 1} ('{calificacion}') no es un número válido.")
            valor = input(f"Por favor, ingrese nuevamente la calificación {i + 1}: ").strip()
        
        calificaciones.append(float(valor))
    
    n_limite=float(input("Ingrese el valor limite: "))
    
    n_calificaciones=len(calificaciones)
    
    for i in range(n_calificaciones):
        if calificaciones[i]>n_limite:
            contador=contador+1
            indice=i
            indices.append(indice)
            calificacion=calificaciones[i]
            Nota.append(calificacion)
                 
    print(f"La cantidad de notas que hay por encima del limite({n_limite}) son: {contador}")
    for i in range(len(indices)):
        print(f"Nota{indices[i]+1}= {Nota[i]}")
    repetir=int(input("\nDeseas repetir?(si=0, no=cualquier numero)"))
    

#
