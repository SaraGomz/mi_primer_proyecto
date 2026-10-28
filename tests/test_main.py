from datetime import date

from src.main import construir_mensaje


def test_mensaje_contiene_nombre_fecha_y_estado():
    mensaje = construir_mensaje("Ana", date(2026, 1, 15))
    assert "Ana" in mensaje
    assert "15/01/2026" in mensaje
    assert "operativo" in mensaje