import requests 
from urllib.parse import urljoin


class Site(requests.Session):

    def __init__(self, url):
        requests.Session.__init__(self)
        self.base_url = url
    
    def get(self, appendix = "", **kwargs):        
        my_url = urljoin(self.base_url, appendix)
        return requests.Session.get(self, my_url, **kwargs)
    
    def post(self, appendix = "", **kwargs):
        my_url = urljoin(self.base_url, appendix)
        return requests.Session.post(self, my_url, **kwargs)


local_server = Site("http://localhost:5600")


