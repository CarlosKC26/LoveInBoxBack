class Orden:

    def __init__(
        self, email_cliente, id_producto, codigo_origen, estado_entrega,
        cantidad_producto, horario_entrega, papel_regalo, cinta, mensaje
    ):
        self.email_cliente = email_cliente
        self.id_producto = id_producto
        self.codigo_origen = codigo_origen
        self.estado_entrega = estado_entrega
        self.cantidad_producto = cantidad_producto
        self.horario_entrega = horario_entrega
        self.papel_regalo = papel_regalo
        self.cinta = cinta
        self.mensaje = mensaje