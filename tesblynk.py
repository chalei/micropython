import network
import socket
from time import sleep



sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("RAHARJA", " ")

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
	
	
http_get('http://188.166.206.43/[authtokenblynk]/update/d4?value=1')
sleep(4)
http_get('http://188.166.206.43/[authtokenblynk]/update/d4?value=0')