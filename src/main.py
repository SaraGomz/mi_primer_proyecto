"""Programa inicial del proyecto integrador."""
from datetime import date

NOMBRE_ALUMNO = "Sara Gómez"

def construir_mensaje(nombre, fecha):
    """Devuelve el mensaje de bienvenida con nombre y fecha."""
    return (
        f"Alumno: {nombre}\n"
        f"Fecha: {fecha.strftime('%d/%m/%Y')}\n"
        "El entorno está operativo."
    )


def main():
    print(construir_mensaje(NOMBRE_ALUMNO, date.today()))


if __name__ == "__main__":
    main()