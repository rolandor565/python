#/usr/bin/python3

class operaciones():

    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        sum = self.n1 + self.n2
        print("el resultado de la suma es: {}".title() .format(sum))

    def resta(self):
        rest = self.n1 - self.n2
        print("el resultado de la resta es: {}".title() .format(rest))

    def multi(self):
        mult = self.n1 * self.n2
        print("el resultado de la multiplicacion es: {}".title() .format(mult))

    def division(self):
        div = self.n1 / self.n2
        return "el resultado de la division es: {}".format(div)
try:
    op = int(input("Selecciona la opcion \n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division"))

    num1 = int(input("Teclea el primer numero \t"))

    num2 = int(input("Teclea el segundo numero \t"))

    if op == 1:
        operacion = print(operaciones(num1,num2).suma())
    elif op == 2:
        operacion = print(operaciones(num1,num2).resta())
    elif op == 3:
        operacion = print(operaciones(num1,num2).multi())
    else:
        operacion = print(operaciones(num1,num2).division())
except:
    print("Se deve seleccionar una opcion del menu")