
import sys
import zmq


class Subscriber:
    
    def __init__(self, addr, port, lookup_type):
        self.addr = addr
        self.port = port
        self.configSubscriber()
    
    def configSubscriber(self):
        #  Socket to talk to server
        self.context = zmq.Context()
        
        self.xpubsocket = self.context.socket(zmq.SUB)
        self.xpubsocket.connect("tcp://{self.addr}:{self.port}")
        
    def createTopic(self, topic):
        # sub must use SUBSCRIBE to set subscription
        self.xpubsocket.setsockopt_string(zmq.SUBSCRIBE, topic)
    
    def processTopic(self):
        string = self.xpubsocket.recv()
        topic,vals = string.split() #TODO-MXM - evaluate msg & update
        print(topic, vals)
        #self.subsocket.subscribe("topic")

if __name__ == "__main__":
    
    substart = Subscriber("localhost", "5560")
    substart.createTopic("dist_topic") #TODO-MXM - grab sys.argv?
    substart.processTopic()
    
# Subscribe to zipcode, default is NYC, 10001
# zip_filter = sys.argv[2] if len(sys.argv) > 2 else "10001"


# Process 5 updates
# total_temp = 0
# for update_nbr in range(5):
#     string = socket.recv_string()
#     zipcode, temperature, relhumidity = string.split()
#     total_temp += int(temperature)

# print("Average temperature for zipcode '%s' was %dF" % (
#       zip_filter, total_temp / (update_nbr+1))
# )
