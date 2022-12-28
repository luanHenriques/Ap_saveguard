################################################################################
# @file    main.py
# @author  Luan Carlos Florencio Henriques
# @version 
# @date    
# Description
# """
# System enums configurations, modes and types
# """
#################################################################################
import struct

from enum import Enum

#Enum
class positionType(Enum):
    geofence        = 1
    gps             = 2
    geo_gps_blended = 3

#xplane-config
class xp():
    def config() -> list:
        ipTarget     = '192.168.x.x'
        mainPort     = 49000
        listenPort   = 49000
        sendPort     = 49000
        structHeader = struct.pack('5s', b'DATA\0')

        configList = [ipTarget, mainPort, listenPort, sendPort, structHeader]

        return configList
