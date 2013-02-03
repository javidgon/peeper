import unittest

from peeper.model import Peeper
from peeper.exceptions import (InvalidModeException,
                               InvalidParametersException,
                               UnsupportedServiceException)

class TestSuitePeeper(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_show_all_events_github_service(self):
        """
        Check if 'show_all_events' fetches from github.
        """
        self.peeper = Peeper(github={'mode': 'show_all_events',
                                     'user': 'javidgon',
                                     'auth': False})
        self.service = 'github'
        
        self.assertTrue(len(self.peeper.get_stream_from_service(self.service)) > 1)
        
    def test_show_repo_events_github_service(self):
        """
        Check if 'show_repo_events' fetches from github.
        """
        self.service = 'github'
        self.user = 'javidgon'
        self.repository = 'endpoint'
        
        self.peeper = Peeper(github={'mode': 'show_repo_events',
                                     'user': self.user,
                                     'repository': self.repository,
                                     'auth': False})

        for i in self.peeper.get_stream_from_service(self.service):
            self.assertTrue(i['repo']['name'] == ('%s/%s' % (self.user, self.repository)))

    def test_show_repo_issues_github_service(self):
        """
        Check if 'show_repo_issues' fetches from github.
        """
        self.service = 'github'
        self.user = 'javidgon'
        self.repository = 'endpoint'
        
        self.peeper = Peeper(github={'mode': 'show_repo_issues',
                                     'user': self.user,
                                     'repository': self.repository,
                                     'auth': False})

        self.assertIn('issue', self.peeper.get_stream_from_service(self.service)[0])
        
    def test_invalid_parameters_exception(self):
        """
        Check if 'invalid_parameters_exception' is raised.
        """
        self.peeper = Peeper(github={'mode':'show_repo_issues'})

        self.assertRaises(InvalidParametersException)
        
    def test_invalid_mode_exception(self):
        """
        Check if 'invalid_mode_exception' is raised.
        """
        self.peeper = Peeper(github={'user':'javidgon'})

        self.assertRaises(InvalidModeException)
        
    def test_unsupported_service_exception(self):
        """
        Check if 'unsupported_service_exception' is raised.
        """
        self.peeper = Peeper(friendfeed={'user':'javidgon'})

        self.assertRaises(UnsupportedServiceException)
        
if __name__ == '__main__':
    unittest.main()
         
