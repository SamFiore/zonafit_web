class Cliente:
    def __init__(self,nombre=None,apellido=None,membresia:int=None,id_cliente=None):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = membresia

    def __str__(self) -> str:
        return f'Id:{self.id} | Nombre:{self._nombre} | Apellido:{self._apellido} | Membresia:{self._membresia}'
    
    @property
    def id(self):
        return self._id_cliente
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def membresia(self):
        return self._membresia
    
    @id.setter
    def id(self,id):
        self._id_cliente = id

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @membresia.setter
    def membresia(self,membresia):
        self._membresia = membresia

        