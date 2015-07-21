from XBeeConnector import XBeeConnector
from XBeeReciever import XBeeReciever
from DatabaseConnector import DatabaseConnector;
import serial;
import struct;
import binascii;
import time;


PORT = 'COM4'
BAUD_RATE = 9600
HOST = '127.0.0.1';
USER = 'root';
PASSWORD = 'P8701239089r1';
DB = 'homemaster';


xbee_reciever = XBeeReciever(PORT,BAUD_RATE)
db = DatabaseConnector(USER,PASSWORD,HOST,DB)
# Continuously read and print packets
while True:
    try:
        response_data = xbee_reciever.get_response()
        data = response_data['rf_data']
        data_length = response_data['data_length']
        source_address = response_data['source_address']

        if data_length == 22:
           temperature = xbee_reciever.get_temperature(data)
           hummidity = xbee_reciever.get_hummidity(data)

           date_and_time = time.strftime("%Y-%m-%d %H:%M:%S");
           
           query = ("INSERT INTO sensorsdata "
                    "(Temperature,Hummidity,DateTime,NodeCode) "
                    "VALUES(%s,%s,%s,%s)");

           data_query = (temperature,hummidity,date_and_time,source_address);
           
           db.initiateQuery(query,data_query);
           
        # if it is not two floats show me what I received
        else:
            print (source_address,' ',data)
    except KeyboardInterrupt:
        break
         
ser.close()
