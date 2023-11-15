from ppadb.client import Client as AdbClient
import time

class ADBTest:
    
    def __init__(self) :
        print('ADBTest ready')

    def connect(self):
        client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
        devices = client.devices()

        if len(devices) == 0: # devices == NULL
            print('No devices')
            quit()

        device = devices[0]
        print(f'device: {device}')
        print(f'client: {client}')
        return device, client
                
    def device_screen_capture(self, device):
        result = device.screencap()
        with open('screen.png', 'wb') as fp:
            fp.write(result)
        
    def work_start(self):
        device, client = self.connect()
        self.device_screen_capture(device)
        

if __name__ == "__main__":
    
    ADBbot = ADBTest()
    ADBbot.work_start()