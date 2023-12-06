"""
Contar cuantas veces aparece un elemento en una lista.
"""

from collections import Counter


def main():
    e = "a"
    l = [1, 4.5, "ab", "a", 546546, "a"]
    print(l.count(e))

    c = Counter(l)
    print(c["a"])


if __name__ == "__main__":
    main()
