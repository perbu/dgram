
import uselect
import usocket
import uasyncio

MAX_PACKET_SIZE = const(1024)

# UDP server
class UDPServer:
    def __init__(self, timeout=1):
        self.timeout = timeout
    
    def close(self):
        self.sock.close()
        self.task.cancel()

    async def serve(self, cb, host, port, backlog=5):
        print('Init')
        ai = usocket.getaddrinfo(host, port)[0]  # Todo: blocking!
        s = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
        self.sock = s
        s.setblocking(False)
        s.bind(ai[-1])

        p = uselect.poll()
        p.register(s,uselect.POLLIN)
        to = self.timeout
        while True:
            if p.poll(to):
                buf, addr = s.recvfrom(MAX_PACKET_SIZE)
                cb(buf,addr)
            await uasyncio.sleep(0)
            
            

