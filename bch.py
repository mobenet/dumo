import hashlib
import datetime

hashlib.sha256("hola")


class Block:
    def __init__(self, data, previous_hash, timestamp=None):  # constructora
        print("soy un bloque...")
        self.timestamp = timestamp or datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash

    def __str__(self):  # metodo que es llamado por print by default
        print("estoy en el metodo str")
        return "".join(
            (str(self.timestamp), str(self.data), str(self.previous_hash))
        )
        # creamos objeto de la clase Block: bloque = Block(0, hola, 0)
        # >>> str(bloque)
        # '0, hola, 0'
        # >>> print(bloque)
        # 0, hola, 0

    def generate_hash(self):
        print("generando hash")
        return hashlib.sha256(str(self).encode()).hexdigest().encode()
        # self.__str__()
        # str(self)
