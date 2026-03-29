from pydoc import describe


def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio_t = input()
    descuento_t = input()
    cantidad_t = input()

    precio = int(precio_t)
    descuento = float(descuento_t)
    cantidad = int(cantidad_t)

    oferta = precio - descuento
    total = oferta * cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {oferta}")
    print(f"Total: {total}")



