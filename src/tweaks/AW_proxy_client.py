import zmq

class AW_proxy_client:

    def __init__(self, RCVTIMEO = 30000):

        self.RCVTIMEO = RCVTIMEO

        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.RCVTIMEO, RCVTIMEO)
        self.socket.setsockopt(zmq.REQ_RELAXED, 1)
        self.socket.connect("tcp://localhost:5557")

        self.ping()
        
        # Some check whether corresponding server is running?
        self.buckets = self.get_buckets_quickly()
    
    def get(self, appendix="", **kwargs):
        r = ["get", appendix, kwargs]
        self.socket.send_json(r)
        return self.socket.recv_json()
    
    def post(self, appendix="", **kwargs):
        r = ["post", appendix, kwargs]
        self.socket.send_json(r)
        return self.socket.recv_json()
    
    def get_buckets(self):
        return self.buckets
    
    def get_buckets_quickly(self):
        """
        While initializing AW_proxy fetches buckets metadata and number of events in each one
        It's rather tim consuming to perform this action every AW_client initialization
        So here we are just fetching a copy of .buckets from AW_proxy
        """
        r = ["get_buckets_quickly", {}]
        self.socket.send_json(r)
        return self.socket.recv_json()
    
    def get_event_count_from_(self, bucket_id):

        if type(bucket_id) != type(""):
            raise TypeError("must be str")
        
        r = ["get_event_count_from_", bucket_id, {}]
        self.socket.send_json(r)
        return self.socket.recv_json()
    
    def ping(self):
        self.socket.setsockopt(zmq.RCVTIMEO, 2000)
        self.socket.send_json(["ping", {}])
        try:
            a = self.socket.recv_json()
        except:
            self.socket.close()
            raise
        
        self.socket.setsockopt(zmq.RCVTIMEO, self.RCVTIMEO)



AW_proxy_client = AW_proxy_client()
