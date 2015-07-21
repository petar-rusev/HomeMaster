from XBeeConnector import XBeeConnector

class XBeeReciever(XBeeConnector):
    def __init__(self,port_number,baud_rate):
        self.port = self.open_serial(port_number,baud_rate)
        self.xbee = self.create_api_object(self.port)
        
    def get_response(self):
        response_attr = {}
        response_data = self.xbee.wait_read_frame()
        response_attr['source_address'] = self.hex(response_data['source_addr_long'][4:])
        response_attr['rf_data'] = self.hex(response_data['rf_data'])
        response_attr['data_length'] = len(response_attr['rf_data'])
        
        return response_attr

    def get_temperature(self,data):
        stringData = self.ascii(data)
        data = []

        for i in range(0,5,1):
            data.append(stringData[i])
            temperature = ''.join(data)

        return temperature
    
    def get_hummidity(self,data):
        stringData = self.ascii(data)
        data = []

        for i in range(6,11,1):
            data.append(stringData[i])
            hummidity = ''.join(data)

        return hummidity
            


