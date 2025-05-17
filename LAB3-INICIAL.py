# LABORATORIO 3 - Solución Parte 1

# Datos iniciales modificados: lista de clientes como diccionarios con preferencias
lista_clientes = [
    {"nombre": "Ana Pérez",    "preferencia": "pan integral"},
    {"nombre": "Carlos López", "preferencia": "croissants de almendra"},
    {"nombre": "Sofía Gómez",   "preferencia": "magdalenas de chocolate"},
    {"nombre": "Pedro Vargas",  "preferencia": "rollos de canela"}
]
ofertas_semanales = {
    "lunes":    "20% de descuento en todos el pan integral",
    "martes":   "¡Compra 3 croissants de almendra y llévate el cuarto gratis!",
    "miércoles":"Oferta especial en nuestras deliciosas magdalenas de chocolate",
    "jueves":   "Pan de masa madre recién horneado a precio especial",
    "viernes":  "¡No te pierdas nuestros rollos de canela recién horneados!"
}

# Actividad 1. obtener_oferta: solicita día al usuario
def obtener_oferta():
    """
    Pide al usuario el día y retorna la oferta correspondiente.
    """
    dia = input("Ingrese el día de la semana (lunes a viernes): ").strip().lower()
    oferta = ofertas_semanales.get(dia)
    # Evalúa si existe oferta encontrada para el día, si no se encontró oferta sería igual a False
    if oferta:
        # Retorna ambos valores, dia ingresado y la oferta encontrada
        return dia, oferta
    else:
        print(f"No hay oferta disponible para '{dia}'.")
        return dia, None

# Actividad 2. generar_mensaje: recibe dict cliente y oferta
def generar_mensaje(cliente, oferta):
    """
    Crea mensaje personalizado. Si la oferta coincide con la preferencia,
    añade nota especial.
    """
    nombre = cliente["nombre"]
    pref   = cliente["preferencia"]
    mensaje = f"Hola {nombre}, hoy tenemos: {oferta}"
    # Reto: incluir nota si es su favorito
    if pref.lower() in oferta.lower():
        mensaje += " ¡Hoy tenemos su favorito!"
    return mensaje

# Actividad 3. formatear_para_envio
def formatear_para_envio(nombre_cliente, mensaje):
    separador = '-' * 40
    return (
        f"Para: {nombre_cliente}\n"
        "De: Panadería Artesanal Marco\n"
        f"{separador}\n"
        f"{mensaje}\n"
        f"{separador}\n"
    )

# Actividad 4. enviar_mensajes: itera y cuenta envíos
def enviar_mensajes(lista_de_clientes, oferta_del_dia):
    contador = 0
    for cliente in lista_de_clientes:
        msg = generar_mensaje(cliente, oferta_del_dia)
        msg_formateado = formatear_para_envio(cliente["nombre"], msg)
        print(msg_formateado)
        contador += 1
    print(f"Total de mensajes enviados: {contador}")

# Actividad 5. main: orquesta flujo con reto final
def main():
    # Ambos valores son retornados juntos desde la funcion obtener_oferta
    dia, oferta = obtener_oferta()
    if oferta:
        enviar_mensajes(lista_clientes, oferta)
    else:
        print("Termina el programa sin enviar mensajes.")

if __name__ == "__main__":
    main()