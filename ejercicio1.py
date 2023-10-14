# Definir una excepción personalizada para manejar problemas relacionados con la venta de productos
class VentaException(Exception):
    pass

# Definir la clase Articulo
class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_a_vender):
        try:
            if cantidad_a_vender <= 0:
                raise VentaException("La cantidad a vender debe ser mayor que cero.")
            if cantidad_a_vender > self.cantidad:
                raise VentaException("No hay suficientes unidades disponibles para la venta.")
            self.cantidad -= cantidad_a_vender
            return cantidad_a_vender * self.precio
        except VentaException as ve:
            return str(ve)

# Ejemplo de uso
if __name__ == '__main__':
    articulo1 = Articulo("Playstation 5", 10, 2000)
    
    try:
        cantidad_vendida = 11
        total_venta = articulo1.vender(cantidad_vendida)
        if isinstance(total_venta, str):
            print("Error:", total_venta)
        else:
            print(f"Venta exitosa: {cantidad_vendida} unidades de {articulo1.nombre} por un total de ${total_venta:.2f}")
    except VentaException as ve:
        print("Error durante la venta:", ve)
