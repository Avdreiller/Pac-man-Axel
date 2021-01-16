class Nodo(object):
    def __init__(self):
        self.id = None
        self.tipo = None
        self.imagen = None
        self.x = None
        self.y = None

    def __init__(self, id, tipo, imagen, x ,y):
        self.id = id
        self.tipo = tipo
        self.imagen = imagen
        self.x = x
        self.y = y