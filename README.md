# Simple UDP listening service for uasyncio

Super simple UDP-listener for the new (April 2020) uasyncio library. It invokes a callback. The return value of the callback (if any) is sent as a response to the client.

Sending is sync.

Not sure if I should have a zero timeout on the poll. I've defaulted to 1ms which is good enough for me. Opinions welcome.

Usage:

```
from dgram import UDPServer
import uasyncio
(..)

def cb(msg, adr):
    print('Got:', msg)
    return 'ack'.encode('ascii')

def main():
    s = dgram.UDPServer()
    l = uasyncio.get_event_loop()
    l.run_until_complete(s.serve(cb, '127.0.0.1', port))
```

