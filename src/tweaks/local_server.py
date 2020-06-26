import requests 
from urllib.parse import urljoin


class Site(requests.Session):

    def __init__(self, url):
        requests.Session.__init__(self)
        self.base_url = url
    
    def get(self, appendix = "", **kwargs):
        # print("#"*40)
        # print(self.base_url)
        # print(appendix)
        
        my_url = urljoin(self.base_url, appendix)
        # print(my_url)
        # print("#"*40)
        return requests.Session.get(self, my_url, **kwargs)


local_server = Site("http://localhost:5600")


class Test:
    """
    Now let us test server availability

    >>> local_server = Site("http://localhost:5600")
    >>> a = local_server.get()
    >>> a.status_code
    200
    """
    pass
