import sys

def es_id(cadena):
    if len(cadena) == 0:
        return False
    
    # Estado q0 → primera letra
    if not cadena[0].isalpha():
        return False
    
    i = 1
    # Estado q1 → ([a-z][0-9])*
    while i < len(cadena):
        if i+1 < len(cadena) and cadena[i].islower() and cadena[i+1].isdigit():
            i += 2
        else:
            return False
    
    return True


def es_suma(cadena):
    return cadena == "+"


def es_incremento(cadena):
    return cadena == "++"


def es_entero(cadena):
    return len(cadena) == 1 and cadena.isdigit()


def evaluar_cadena(cadena):
    if es_incremento(cadena):
        return "ACEPTA (Incremento)"
    elif es_suma(cadena):
        return "ACEPTA (Suma)"
    elif es_entero(cadena):
        return "ACEPTA (Entero)"
    elif es_id(cadena):
        return "ACEPTA (Id)"
    else:
        return "NO ACEPTA"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python AFD.py entrada.txt")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        with open(archivo, 'r') as f:
            for linea in f:
                cadena = linea.strip()
                if cadena:  # evitar líneas vacías
                    print(f"{cadena} -> {evaluar_cadena(cadena)}")
    except FileNotFoundError:
        print("El archivo no existe.")

