from dotenv import load_dotenv
import os
import psycopg2

class Conexion:
    load_dotenv()
    _DB = os.getenv('DB')
    _USER = os.getenv('USER')
    _PSW = os.getenv('PSW')
    _PORT = os.getenv('PORT')
    _HOST = os.getenv('HOST')
    _conn = None
    _curs = None

    @classmethod
    def get_conn(cls):
        if cls._conn is None:
            try:
                cls._conn = psycopg2.connect(host=cls._HOST,
                                             user=cls._USER,
                                             password=cls._PSW,
                                             port=cls._PORT,
                                             database=cls._DB)
                return cls._conn
            except Exception as e:
                return e
        else:
            return cls._conn
        
    def get_curs(cls):
        if cls._curs is None:
            try:
                cls._curs = cls.get_conn().cursor()
                return cls._curs
            except Exception as e:
                return e
        else:
            return cls._curs
        
if __name__ == '__main__':
    conn = Conexion()
    conn.get_curs() 
