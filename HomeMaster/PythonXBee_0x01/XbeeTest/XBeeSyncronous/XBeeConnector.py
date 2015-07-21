from xbee import ZigBee;
import serial;
import struct;
import binascii;

class XBeeConnector:
    
    def open_serial(self,port,baud_rate):
        serial_port = serial.Serial(port,baud_rate)
        return serial_port
    
    def create_api_object(self,serial_port):
        xbee = ZigBee(serial_port,escaped=True)
        return xbee

    def hex(self,bindata):
        return ''.join('%02x' % byte for byte in bindata)

    def ascii(self,hexData):
        return ''.join(chr(int(hexData[i:i+2], 16)) for i in range(0, len(hexData), 2))