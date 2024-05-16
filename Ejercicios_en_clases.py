'''
crea una clase llamada personaje, y acontinuación
crea un objeto a partir de ella, por ejemplo Harry_potter
'''

# class Personaje:
#     def __init__(self, protagonista):
#         self.protagonista = protagonista
    
# el_prota = Personaje('Harry_potter')
# print("El protagonista es:", el_prota.protagonista)


'''
Crea una clase llamada Dinosaurio 
y tres instancias a partir de ella:
velociraptor, tiranosaurio_rex, branquisaurio
'''
# class Dinosaurio:
#     def __init__(self,dinosaurio1,dinosaurio2,dinosaurio3):
#         self.dinosaurio1 = dinosaurio1
#         self.dinosaurio2 = dinosaurio2
#         self.dinosaurio3= dinosaurio3
# dinosaurios = Dinosaurio('velociraptor','tiranosaurio_rex','brancosaurio')
# print("El dinosaurio mas veloz es el", dinosaurios.dinosaurio1)
# print("El Mayor carnivoro que exitio entre los dinasurios es el:",dinosaurios.dinosaurio2)
# print("Este dinosaurio se le conocia como reptil del trueno y es el:",dinosaurios.dinosaurio3)

'''
Crea una clase llamada plataformastreaming y crea los siguientes
objetos a partir de ella: netflix, hbo_max, amazon_prime_video
'''
# class Plataformastreaming:
#     def __init__(self,Plataforma1,plataforma2,plataforma3):
#         self.plataforma1 = Plataforma1
#         self.plataforma2 = plataforma2
#         self.plataforma3 = plataforma3

# Plataformas = Plataformastreaming('netflix','hbo_max','amazon_prime_video')
# print(f"las plataformas mas populares de estriming son: {Plataformas.plataforma1}, {Plataformas.plataforma2}, {Plataformas.plataforma3}")

'''
Crea una clase llamada Casa, y asigna atributos color, cantidad_pisos,
crea una instancia de Casa llamada casa_blanca, de color blanco y cantidad de pisos igual a 4 
'''
# class Casa:
#     def __init__(self,color,cantida_pisos):
#         self.color = color
#         self.cantidad_pisos = cantida_pisos
# casa_blanca = Casa("blanca",4)
# print(f"La casa es {casa_blanca.color} con {casa_blanca.cantidad_pisos} pisos")

'''
Crea una clase llamada Cubo, y asiganale el atributo de clase
caras = 6
y el atributo de instancia color
crea una instancia cubo_rojo de dicho color
'''
# class Cubo:
#     def __init__(self,caras,color):
#         self.caras = caras
#         self.color = color

# cubo_rojo = Cubo(6,'rojo')

# print(f"El cubo tiene {cubo_rojo.caras} caras y es de color {cubo_rojo.color}")

'''
Crea una clase llamada Personaje, y asignale el siguiente atributo de clase:
real = False
Crea una instancia llamada harry_potter con los siguientes atributos de instancia
especie = humano
magico = True
edad = 17
'''
# class Personaje:
#     def __init__(self,real):
#         self.real = real
               
# real1 = Personaje(False)
# print(real1.real)

# class Personaje:
#     def __init__(self,especie,magico,edad):
#         self.especie = especie
#         self.magico = magico
#         self.edad = edad

# harry_potter = Personaje('humano',True,20)
# print(harry_potter.especie)
# print(harry_potter.magico)
# print(harry_potter.edad)


'''
Crea una clase perro dicho perro debe poder ladrar
crea el metodo ladrar() y ejecutalo en una instancia de perro, cada ves que ladre 
debera mostrar en pantalla "Guau!"
'''
# class Perro:
#     def __init__(self,nombre):
#         self.nombre = nombre
#     def ladrar(self):

#         if self.nombre == "Dog":
#             print("Guau!")
# perro = Perro('Dog')

# perro.ladrar()

'''
Crea una clase llamada Mago, y crea un metod lanzar_hechizo()
debera imprimir ¡abracadabra!
crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo
'''
# class Mago:
#     def __init__(self,nombre):
#         self.nombre = nombre

#     def lanzar_hechizo(self):
#         if self.nombre == "Merlin":
#             print("¡abracadabra!")
# mago1 = Mago("Merlin")
# print("Merlin te lanza un hechizo")
# mago1.lanzar_hechizo()

'''
Crea una instancia de la clase alarma, que tenga un meteodo llamado postergar(cantidad minutos)
El metodo debe imprimir en pantalla el mensaje 
"La alarma ha sido pospuesta {cantida_minutos} minutos
'''
# class Alarma:
#     def __init__(self,hora):
#         self.hora = hora

#     def postergar(self,cantidad_minutos):
#         self.hora += int(cantidad_minutos)
#         print(f"se postergo {cantidad_minutos} minutos")

# hora_de_sonar = Alarma(7)
# print(f"la alarma sono a las {hora_de_sonar.hora} de la mañana")
# hora_de_sonar.postergar(10)

'''
Crea una clase llamada persona, que tenga los siguientes atributos de instancia
nombre, edad. crea otra clase Alumno, que herede de la primera estos atributos
'''

# class Persona:
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad

# class Estudiante(Persona):

#     def __init__(self, nombre, edad):
#         super().__init__(nombre, edad)

# estudiante1 = Estudiante('rigo',22)

# estudiante1.nombre
# estudiante1.edad

# print(f"mi nombre es {estudiante1.nombre} y tengo {estudiante1.edad} años")


'''
Crea una clase llamada Mascota, que tenga los siguienetes atributos de instancia
edad, nombre, cantidad_patas, Crea otra clase Perro que herede la primera de sus atributos
'''
# class Mascota:
#     def __init__(self,edad,nombre,cantidad_patas):
#         self.edad = edad
#         self.nombre = nombre
#         self.cantidad_patas = cantidad_patas

# class Perro(Mascota):
#     def __init__(self, edad, nombre, cantidad_patas):
#         super().__init__(edad, nombre, cantidad_patas)
    
# mi_mascota = Perro(2,"firulais",4) 
# mi_mascota.edad
# mi_mascota.nombre
# mi_mascota.cantidad_patas

# print(f"mi mascota se llama {mi_mascota.nombre}, tiene {mi_mascota.edad} años de edad, y tiene {mi_mascota.cantidad_patas} patas")

   
'''
Crea una clase llamada Vehiculo, que contenga los metodos acelerar() y
(puedes dejar el codigo de metodos en blanco con pass)
frenar() crea una clase llamada Automovil1 que herede estos metedos de vehiculo
'''
# class Vehiculo:
#     def __init__(self,automovil):
#         self.automovil = automovil

#     def acelerar(self,):
#         pass
#     def frenar(self,):
#         pass

# class Automovil1(Vehiculo):
#     def __init__(self, automovil):
#         super().__init__(automovil)

# moto = Automovil1("pulsar")
# print(moto.automovil)