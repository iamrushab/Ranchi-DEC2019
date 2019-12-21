import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client1 = ModbusClient(method = 'rtu', port = '/dev/ttyUSB0', parity='E',stopbits=1,bytesize=8,baudrate = 9600,timeout=1)

def up(start,stop,ramp,unit11):
    total = stop-start
    print total
    a = total/ramp #Hz/Second
    print a
    c = 0
    print c
    while c <= total:
        print client1.connect()
        t = client1.write_register(0x2001,start,unit=unit11)
        #l = client1.write_register(0x2001,start,unit=2)
        start += a
        c += a
        print c
        time.sleep(1)
        client1.close()

def down(start,stop,ramp,unit21):
    total = start-stop
    print total
    a = total/ramp #Hz/Second
    print a
    c = 0
    print c
    while c <= total:
        print client1.connect()
        t = client1.write_register(0x2001,start,unit=unit21)
        #l = client1.write_register(0x2001,start,unit=2)
        start -= a
        c += a
        print c
        time.sleep(1)
        client1.close()

def main():
    while True:
        up(0,4000,5,1)
        down(4000,0,5,2)

if __name__ == '__main__':
    main()
