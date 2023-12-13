"""
Escribir un programa que lea un número impar por teclado. Si el usuario no
introduce un número impar, debe repetirse el proceso hasta que lo introduzca
correctamente.
"""


def main():
    while True:
        input_string = input("Digite un número impar: ")

        if not input_string.isdigit():
            print("\tNúmero inválido")
            continue

        n = int(input_string)

        if n % 2 == 0:
            print("\tNúmero inválido")
            continue

        print("\tNúmero válido")
        break


if __name__ == "__main__":
    main()
