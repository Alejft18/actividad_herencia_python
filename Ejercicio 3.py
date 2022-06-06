#Elabore un programa POO, en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular con estos dos valores la suma, resta, multiplicación y división. Utilizar un método para cada una de las operaciones e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

from ast import Div, Num


class calculadora:

    def __init__(self):
        self.num1=int (input("Ingrese un numero: "))
        self.num2=int (input("Ingrese otro numero: "))

    def mostrar(self):
        print("Numero 1 es igual a ",self.num1)
        print("Numero 2 es igual a ",self.num2)


    def suma(self):
        suma=self.num1 + self.num2
        print("La suma de los numeros es: ",suma)

    def resta(self):
        resta=self.num1 - self.num2
        print("La resta de los numeros es: ",resta)

    def mult(self):
        mult=self.num1 * self.num2
        print("La multiplicacion de los numeros es: ",mult)

    def div (self):
        div=self.num1 / self.num2
        print("La division de los numeros es: ",div)

resultado=calculadora()
resultado.mostrar()
resultado.suma()
resultado.resta()
resultado.mult()
resultado.div()

   

