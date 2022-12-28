################################################################################
# @file    main.py
# @author  Luan Carlos Florencio Henriques
# @version 
# @date    
# Description
# """
# Connection with X-Plane and get position data;
# """
#################################################################################
import socket
import struct

from settings.config import xp

class xpComm():
    def __init__(self) -> None:
        
        xpConfigList = xp.config()

        self.ipXlane      = xpConfigList[0]
        self.mainPort     = xpConfigList[1]
        self.listenPort   = xpConfigList[2]
        self.sendPort     = xpConfigList[3]
        self.structHeader = xpConfigList[4]
        
        #self.xpConnect(self.ipXlane, self.listenPort, self.mainPort)

    def xpConnect(self, ipXplane, listenPortXplane, udpMainPort):
        udpIp = [(s.connect((ipXplane, listenPortXplane)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
        sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((udpIp, udpMainPort))
        
        self.getData(sock)


    def getData(self,sock):
        data, addr = sock.recvfrom(1024)
        lenData    = len(data)
        dataFormat = str(lenData)+'b'
        dataStruct = struct.unpack_from(dataFormat,data)
        
        return dataStruct
    

    def sendData(self, data): #toReview      
        pass
        
        # header      = struct.pack('5s', b'DATA\0')
        # data_buf    = bytearray(struct.pack('iffffffff', 11, elevator, aileron, rudder, 0, 0, 0, 0, 0))
        # dataToSend  = header + data_buf
        # socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(dataToSend, (self.ipXplane, self.sendPort))
        
