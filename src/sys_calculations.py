import struct


class calculations:
    def __init__(self) -> None:
        pass

    #convert the bytearray to integer
    def bytesToFloat(dataBytes):
        x = dataBytes
        return round(struct.unpack('<f', struct.pack('4b', *x))[0],4)