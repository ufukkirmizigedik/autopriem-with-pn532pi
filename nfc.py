import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

i2c = busio.I2C(board.SCL,board.SDA)
reset_pin = DigitalInOut(board.D6)
req_pin = DigitalInOut(board.D12)
pn532 = PN532_I2C(i2c,debug=False,reset = reset_pin,req=req_pin)

ic,ver,rev,support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver,rev))

pn532.SAM_configuration()

print("waiting for NFC card...")

def nfc():

    while True:
        
        uid = pn532.read_passive_target(timeout=0.5)
        print(".", end="")
        if uid is None:
            continue
        else:
            print("Found card with UID:",[hex(i) for i in uid])
        if uid == bytearray(b'\x93\xe3\xb6\t'):
            print('привет уфук')
            break

