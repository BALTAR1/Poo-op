from datetime import datetime, timedelta


def obtener_fechas_mes(year, month):
    fechas = []
    fecha_actual = datetime(year, month, 1)
    ultimo_dia_mes = datetime.now()

    while fecha_actual <= ultimo_dia_mes:
        fechas.append(fecha_actual.date())
        fecha_actual += timedelta(days=1)

    fechas_hechas = [fecha.strftime("%Y/%m/%d") for fecha in fechas]
    return fechas_hechas
