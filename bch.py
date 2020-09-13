import hashlib
import datetime

from src import foo

foo.hello()
hashlib.sha256("hola".encode())


class Block:
    def __init__(self, data, previous_hash, timestamp=None):  # constructora
        print("soy un bloque...")
        self.timestamp = timestamp or datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    def __str__(self):  # metodo que es llamado por print by default
        print("estoy en el metodo str")
        return "".join(
            (str(self.timestamp), str(self.data), str(self.previous_hash)) #string
        )
        # return (self.timestamp, self.data, self.previous) -> tupla
        # creamos objeto de la clase Block: bloque = Block(0, hola, 0)
        # >>> str(bloque)
        # '0, hola, 0'
        # >>> print(bloque)
        # 0, hola, 0

    def generate_hash(self):
        print("generando hash")
        inner_hash = hashlib.sha256(str(self).encode()).hexdigest().encode()
        return hashlib.sha256(inner_hash).hexdigest()
        # self.__str__()
        # str(self)

bloque0 = Block(0,0)
hash_bloque0 = bloque0.generate_hash()
# >>> hash_bloque0
# b'b84ee92d6e4d13f33164aef6c734e949c618e57afe9e327187869ad00ac71a6a'
# inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode()
# outer_hash = hashlib.sha256(inner_hash).hexdigest()
# >>> hashlib.sha256(hash_bloque0).hexdigest()
# '7003c2bd8dbbcbe1baf002739dd8521b835c48a2d2d9019edf90cb2da3e3e2ce'

l = []
l = list()

# blockchain.py
num_blocks_to_add = 10

block_chain = [bloque0]

print("The genesis block has been created.")
print("Hash bloque0: %s" % bloque0.hash)
print("Hash primer bloque: ", block_chain[0].hash )
for i in range(1, num_blocks_to_add):
    print(i)
    print("Hash of the previous block: ", i-1, block_chain[i-1].hash)
    bloquen = Block(
            "Block number %d" % i,
            block_chain[i-1].hash,
            datetime.datetime.now()
        )
    block_chain.append(bloquen)
    print("Block #%d created." % i)
    print("Hash of the actual block: ", i, bloquen.hash)
    print("Hash del ultimo bloque: %s" % block_chain[-1].hash)