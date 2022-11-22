class Producto:

    def __init__(
        self, id_producto, nombre, imagen, descripcion, precio, nit_empresa, inventario, descuento
    ):
        self.id_producto = id_producto
        self.nombre = nombre
        self.imagen = imagen
        self.descripcion = descripcion
        self.precio = precio
        self.nit_empresa = nit_empresa
        self.inventario = inventario
        self.descuento = descuento