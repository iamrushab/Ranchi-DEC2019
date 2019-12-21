import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client1 = ModbusClient(method = 'rtu', port = '/dev/ttyUSB0', parity='E',stopbits=1,bytesize=8,baudrate = 9600,timeout=1)

def mode(start,stop,ramp):
    total = stop-start
    print total
    a = total/ramp #Hz/Second
    print a
    c = 0
    print c
    while c <= total:
        print client1.connect()
        t = client1.write_register(0x2001,start)
        start += a
        c += a
        print c
        client1.close()

def main():
    while True:
        mode(0,1000,2)
        mode(2000,3000,2)
        mode(3000,4000,2)
        mode(4000,5000,2)
        mode(5000,6000,2)

if __name__ == '__main__':
    main()
