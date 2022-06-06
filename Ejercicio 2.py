#Realizar un programa POO que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Ingresar por teclado. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la calificación y si ha aprobado o no. Nota >=3 aprobó

class estudiante:
   
    def __init__(self):
        self.nombre= input("Escriba su nombre ")
        self.nota=int(input("Escribe tu nota "))
 
   
    def mostrar(self):
        print("Nombre:",self.nombre)
        print("Nota: ",self.nota)
 
    def aprobacion(self):
        if self.nota>= 3:
            print("Su nota es ",self.nota, ", Usted Aprobó")
        else:
            print("Su nota es ",self.nota, ", Usted Reprobó")
            
estudiante1=estudiante()
estudiante1.mostrar()
estudiante1.aprobacion()


