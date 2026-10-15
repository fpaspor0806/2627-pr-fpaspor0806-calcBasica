def sumar(num1: float, num2: float) -> float:
    """Suma el primer numero con el segundo.

    :param num1: el numero al que se le va a sumar.
    :param num2: el numero que va a ser sumado.
    :return: el resultado de la suma de los dos numeros
    """
    return num1 + num2

def restar(num1: float, num2: float) -> float:
    """resta el segundo numero al primero.
    
        :param num1: el numero al que se le va a restar.
        :param num2: el numero que va a restar.
        :return: el resultado de la resta de los dos numeros
        """
    return num1 - num2

def multiplicar(num1: float, num2: float) -> float:
    """multiplica el primer numero con el segundo.
    
        :param num1: el numero al que se le va a multiplicar.
        :param num2: el numero que va a multiplicar.
        :return: el resultado de la multiplicación de los dos numeros
        """
    return num1 * num2

def dividir(num1: float, num2: float) -> float:
    """Divide el primer numero con el segundo.
    
        :param num1: el numero al que se le aplica la división.
        :param num2: el numero que va a dividir.
        :return: el resultado de la division de los dos numeros
        """
    return num1 / num2

def main():
    num1 = float(input("Introduce el 1º numero"))
    num2 = float(input("Introduce un 2º numero"))
    if num2 == 0:
        print("No se puede realizar la operacion")
    else:
        suma = sumar(num1, num2)
        resta = restar(num1, num2)
        mult = multiplicar(num1, num2)
        div = dividir(num1, num2)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {mult}")
    print(f"División: {div}")
if __name__ == "__main__":
    main()