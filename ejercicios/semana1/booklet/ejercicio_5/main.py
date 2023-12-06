"""
Escribir un programa que sume todos los números enteros impares desde el 0
hasta el 100
"""


def main():
    print(sum(filter(lambda item: item % 2 != 0, range(0, 3))))


if __name__ == "__main__":
    main()
