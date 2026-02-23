class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def subtotal(self):
        return self.precio * self.cantidad
    def mostrar(self, indice):
        print(f"{indice}. {self.nombre} | precio: ${self.precio:.2f} | cantidad: {self.cantidad} | subtotal: ${self.subtotal():.2f}")
class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"producto {producto.nombre} agregado.\n")
    def calcular_total(self):
        return sum(p.subtotal() for p in self.productos)
    def mostrar_factura(self):
        print("\n factura detallada")
        print(f"cliente: {self.cliente}")
        print("------------------------------")
        for i, producto in enumerate(self.productos, start=1):
            producto.mostrar(i)
        print("------------------------------")
        print(f"total a pagar: ${self.calcular_total():.2f}\n")
def menu():
    print("sistema de facturacion")
    cliente = input("ingrese nombre del cliente: ")
    factura = Factura(cliente)
    while True:
        print("\nopciones:")
        print("1. agregar producto")
        print("2. mostrar factura")
        print("3. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            nombre = input("nombre del producto: ")
            try:
                precio = float(input("precio del producto: "))
                cantidad = int(input("cantidad: "))
                producto = Producto(nombre, precio, cantidad)
                factura.agregar_producto(producto)
            except ValueError:
                print("precio o cantidad invalidos.\n")
        elif opcion == "2":
            factura.mostrar_factura()
        elif opcion == "3":
            print("saliendo del sistema...")
            break
        else:
            print("opcion invalida.\n")
menu()