"""
Dadas dos listas (las que se quiera crear), generar una tercera con los
elementos que estén presentes en AMBAS listas. Retornar esta nueva lista pero
sin elementos duplicados.
"""


def main():
    l1 = [1, 5.6, 90, 67, 67, 10]
    l2 = [67, 6, 9.078, 10, 3466]

    l3 = list(set(l1).intersection(set(l2)))
    print(l3)

    l3 = list(set([item for item in l1 if item in l2]))
    print(l3)


if __name__ == "__main__":
    main()
