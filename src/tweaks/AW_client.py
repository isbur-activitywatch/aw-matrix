import zmq
import json

class AW_client:

    def __init__(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.RCVTIMEO, 30000)
        self.socket.connect("tcp://localhost:5556")
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


AW_client = AW_client()
