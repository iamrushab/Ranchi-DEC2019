import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client1 = ModbusClient(method = 'rtu', port = '/dev/ttyUSB0', parity='E',stopbits=1,bytesize=8,baudrate = 9600,timeout=1)

def up(start,stop,ramp):
    total = stop-start
    print total
    a = total/ramp #Hz/Second
    print a
    c = 0
    print c
    while c <= total:
        print client1.connect()
        t = client1.write_register(0x2001,start,unit=1)
        l = client1.write_register(0x2001,start,unit=2)
        start += a
        c += a
        print c
        time.sleep(1)
        client1.close()

def down(start,stop,ramp):
    total = stop-start
    print total
    a = total/ramp #Hz/Second
    print a
    c = 0
    print c
    while c <= total:
        print client1.connect()
        t = client1.write_register(0x2001,start,unit=1)
        l = client1.write_register(0x2001,start,unit=2)
        start -= a
        c += a
        print c
        time.sleep(1)
        client1.close()

def main():
    while True:
        #up(0,3000,5)
        down(3000,0,5)

if __name__ == '__main__':
    main()
