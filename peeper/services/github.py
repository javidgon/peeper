import requests
from peeper.decorators import validate_params
from peeper.exceptions import InvalidModeException

class GithubStream:
    """
    Github wrapper. It will manage the requests to the website.
    """
    events = ['show_all_events',
              'show_repo_events',
              'show_repo_issues']
    
    def __init__(self, *args, **kwargs):
        for value in kwargs['credentials']:
            setattr(self, value, kwargs['credentials'][value])
        
        self.session = requests.Session()
        if hasattr(self, 'auth') and self.auth:
            if not hasattr(self, 'password'):
                self.password = None
            self.session.auth = (self.user, self.password)
        
    def dispatcher(self):
        if hasattr(self, 'mode') and self.mode in self.events:
            return getattr(self, self.mode)()
        raise InvalidModeException
    
    @validate_params(required_params=['user'])
    def show_all_events(self):
        response = self.session.get("https://api.github.com/users/%s/events" %
                                    (self.user))

        return response.json()
    
    @validate_params(required_params=['user', 'repository'])
    def show_repo_events(self):
        response = self.session.get("https://api.github.com/repos/%s/%s/events" %
                                    (self.user, self.repository))
        
        return response.json()
        
    @validate_params(required_params=['user', 'repository'])
    def show_repo_issues(self):
        response = self.session.get("https://api.github.com/repos/%s/%s/issues/events" %
                                    (self.user, self.repository))
        
        return response.json()
            