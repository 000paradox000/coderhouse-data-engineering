"""
Escribir un programa que pida al usuario cuántos números quiere introducir.
Luego que lea todos los números y realice una media aritmética.
"""

from decimal import Decimal
from decimal import InvalidOperation


def request_integer_number(msg, greater_than_zero=False):
    while True:
        input_string = input(f"{msg}")

        if not input_string.isdigit():
            print("\tNúmero inválido")
            continue

        n = int(input_string)

        if greater_than_zero and n == 0:
            print("\tNúmero inválido")
            continue

        return n


def request_number(msg):
    while True:
        input_string = input(f"{msg}")

        try:
            return Decimal(input_string)
        except InvalidOperation:
            print("\tNúmero inválido")
            continue


def main():
    n = request_integer_number(
        "¿Cuántos números quieres ingresar?: ",
        greater_than_zero=True
    )

    mean = Decimal(0)

    for i in range(1, n+1):
        item = request_number(f"[{i}] Digite un número: ")
        mean += item

    print(f"La media aritmética es: {mean / Decimal(n)}")


if __name__ == "__main__":
    main()
