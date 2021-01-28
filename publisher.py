

import zmq
#from random import randrange

print("Current libzmq version is %s" % zmq.zmq_version())
print("Current  pyzmq version is %s" % zmq.__version__)

class Publisher:
    #lookup_type = distributed lookup type (centralized (c), flooding (f), empty (n))
    def __init__(self, addr, port, lookup_type):
        #TODO-MXM - do we need some sort of identifier?
        self.addr = addr
        self.port = port

        #TODO-MXM - for build-out of diff. distr. lookup types
        if lookup_type == "centralized":
            self.dist_type = "c"
        elif lookup_type == "flooding":
            self.dist_type = "f"
        else:
            self.dist_type = "n"
            
        self.configPublisher()

    def configPublisher(self):
        #TODO-MXM - some examples bind and connect to different ports
        #TODO-MXM - bind to *:port, connect to proxy frontend
        self.context = zmq.Context()
        self.xsubsocket = self.context.socket(zmq.PUB)
        #connect to proxy 
        self.xsubsocket.connect("tcp://addr:port") #TODO-MXM - update addr/port

# keep publishing 
while True:
    zipcode = randrange(1, 100000)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))
