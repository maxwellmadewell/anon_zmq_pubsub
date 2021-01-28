# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:13:22 2021

@author: mxmco
"""



import zmq
import threading

class MessageBroker:
    
    def __init__(self):
        #TODO - MXM - need persistent storage of list?
        self.topics = {}#gather list of topics from pub/subs
        self.runBrokerThread() #run broker in seperate thread
        
#
    def configBroker(self):
        """connects, binds, and configure sockets"""
        #https://zguide.zeromq.org/docs/chapter2/#The-Dynamic-Discovery-Problem
        
        self.context = zmq.Context()
        
        #TODO - MXM-Set up try/catch for except then shut down sockets
        
        
        #proxy is long-lived - so bind sockets
        # https://stackoverflow.com/questions/16109139/zmq-when-to-use-zmq-bind-or-zmq-connect
        
        #Socket facing multiple subscribers
        frontend = self.context.socket(zmq.XSUB)
        
        #TODO-MXM - abstract out address?
        frontend.bind("tcp:*:5559")
        
        #Socket facing multiple publishers
        backend = self.context.socket(zmq.XPUB)
        
        #TODO-MXM - abstract out address?
        backend.bind("tcp:*:5560")
        
        #built-in pub/sub fowarder
        zmq.proxy(frontend, backend)
        
        #Shouldn't get here
        frontend.close()
        backend.close()
        self.context.term()
    
    #https://docs.python.org/3/library/threading.html
    def runBrokerThread(self):
        #create message broker thread with configured broker func. target
        self.brokerThread = threading.thread(target=self.configBroker)
        self.brokerThread.start()
        
if __name__ == "__main__":
    #main()
    MessageBroker()