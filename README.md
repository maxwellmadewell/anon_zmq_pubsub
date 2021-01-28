# Publisher/Subscriber (pub/sub) with proxy in Python

Basic xpub/xsub model supported by ZeroMQ (zmq) and mininet with 
proxy/broker to make pub/sub communication anonymous to each other

publisher.py - publishes topics to broker for consumption
subscriber.py - connects to broker to receive subscribed topics
broker.py - binds frontend/backend, xsubsocket/xpubsocket with zmq.proxy  
