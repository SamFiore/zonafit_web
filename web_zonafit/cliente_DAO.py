from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    _SELECT = 'SELECT * FROM clientes ORDER BY id'
    _SELECT_FOR_ID = 'SELECT * FROM clientes WHERE id=%s'
    _INSERT = 'INSERT INTO clientes(nombre,apellido,membresia) VALUES(%s,%s,%s)'
    _UPDATE = 'UPDATE clientes SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    _DELETE = 'DELETE FROM clientes WHERE id=%s'

    @classmethod
    def select(cls):
        curs = Conexion.get_curs(Conexion)
        curs.execute(cls._SELECT)
        records = curs.fetchall()
        clientes = []
        for record in records:
            cliente = Cliente(record[1],record[2],record[3],record[0])
            clientes.append(cliente)
        return clientes

    @classmethod
    def select_for_id(cls,id):
        conn = None
        try:
            conn = Conexion.get_conn()
            curs = conn.cursor()
            valores = (id,)
            curs.execute(cls._SELECT_FOR_ID,valores)
            record = curs.fetchone()
            cliente = Cliente(record[1],record[2],record[3],record[0])
            return cliente
        except Exception as e:
            raise ValueError(f'Excepción al seleccionar cliente por id: {e}')

    @classmethod
    def update(cls,cliente):
        with Conexion.get_conn() as conn:
            with conn.cursor() as curs:
                curs = Conexion.get_curs(Conexion)
                values = (cliente.nombre,cliente.apellido,cliente.membresia,cliente.id)
                curs.execute(cls._UPDATE,values)
        
    @classmethod
    def insert(cls,cliente):
        with Conexion.get_conn() as conn:
            with conn.cursor() as cursor:
                values = (cliente.nombre,cliente.apellido,cliente.membresia)
                cursor.execute(cls._INSERT,values)

    @classmethod
    def delete(cls,cliente):
        with Conexion.get_conn() as conn:
            with conn.cursor() as curs:
                values = (cliente.id,)
                curs.execute(cls._DELETE,values)

if __name__ == '__main__':
    cliente_dao = ClienteDAO()
    # cliente_insertado = cliente_dao.insert(Cliente('Alejo','Ateo',100))
    cliente_actualizado = cliente_dao.delete(Cliente(id_cliente=6))

    clientes = cliente_dao.select()
    for cliente in clientes:
        print(cliente.nombre)
