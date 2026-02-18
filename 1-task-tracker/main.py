import sys


def saludar(nombre=None):
    if nombre:
        print(f"Hola {nombre}")
    else:
        print("Hola, que tal?")


def main():

    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        saludar(nombre)
    else:
        saludar()


if __name__ == "__main__":
    main()
