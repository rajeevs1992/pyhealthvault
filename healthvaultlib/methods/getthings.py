from methodbase import RequestBase, ResponseBase

class GetThingsRequest(RequestBase):
    
    def __init__(self):
        self.name = 'GetThings'
        self.version = 3

class GetThingsResponse(ResponseBase):
    
    def __init__(self):
        self.name = 'GetThings'
        self.version = 3
