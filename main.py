import serial
import time

# Replace 'COM4' with the appropriate port name for your system (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
ard = serial.Serial('COM4', 9600, timeout = 1)

string = "h"
command = '<' + string + '>'

try:
    # Try to perform an operation on the port
    print("sending out command", command)
    ard.write(bytes(b"'<' + command + '>'"))

    time.sleep(0.5)

    confirmation = ard.read()
    print("Confirmation: ", confirmation)

except serial.SerialException:
    print("Port is closed")

finally:
    ard.close()