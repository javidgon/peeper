"""
Peeper Exceptions
"""

class PeeperException(Exception):
    
    code = None
    description = None
    
    def __init__(self):
        Exception.__init__(self, '%d %s' % (self.code, self.description))

class InvalidParametersException(PeeperException):
    
    code = 501
    description = 'Invalid or missing parameters in the call.'
        
class InvalidModeException(PeeperException):
    
    code = 502
    description = 'Invalid mode.'

class UnsupportedServiceException(PeeperException):
    
    code = 503
    description = 'Unsupported service.'