"""
Peeper's decorators
"""
from peeper.exceptions import InvalidParametersException

def validate_params(required_params=None):
    """
    Validate the received parameters.
    :param required_params: Required parameters.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if required_params:
                for param in required_params:
                    if not hasattr(args[0], param):
                        raise InvalidParametersException
            return func(*args, **kwargs)    
        return wrapper
            
    return decorator