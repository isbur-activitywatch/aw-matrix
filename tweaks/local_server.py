import requests 


class Site(requests.Session):

    def __init__(self, url):
        requests.Session.__init__(self)
        self.url = url
    
    def get(self, **kwargs):
        return requests.Session.get(self, self.url, **kwargs)
    
    def post(self, **kwargs):
        return requests.Session.post(self, self.url, **kwargs)


local_server = Site("http://localhost:5600")

class Test:
    """
    Now let us test server availability

    >>> a = local_server.get()
    >>> a.status_code
    200
    """
    pass
