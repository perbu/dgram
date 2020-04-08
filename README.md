# Simple UDP listening service for uasyncio

Super simple UDP-listener for the new (April 2020) uasyncio library.

Usage:

```
import uselect
import usocket
import uasyncio
(..)


async def main():
    s = dgram.UDPServer()
    l = uasyncio.get_event_loop()
    l.run_until_complete(s.serve(cb, '127.0.0.1', port))
```

Caveat: If you wanna respond to the incomming packet you need to do this yourself. Maybe I'll add it later.
