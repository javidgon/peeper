from peeper.services.github import GithubStream
from peeper.exceptions import UnsupportedServiceException

class Peeper:
    """
    Peeper model
    """
    def __init__(self, *args, **kwargs):
        self.supported_services = ['github']
        self.services = {}
        for name in kwargs:
            self.services[name] = {}
            for value in kwargs[name]:
                self.services[name][value] = kwargs[name][value]

    def get_stream_from_service(self, service=None):
        """
        Get the stream from the different services.
        :param service: Target service.
        :rtype: JSON Object
        """
        if service and service in self.supported_services:
            if service == 'github':
                return GithubStream(credentials=self.services['github']).dispatcher()
        else:
            raise UnsupportedServiceException

    