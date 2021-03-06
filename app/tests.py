import unittest
from .models import Source,Articles

class SourceTest(unittest.TestCase):
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source('cnn','CNN','News as you love','https://newsapi.org/v2/sources?language=en&category={}&apiKey={}','business','ke','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))    

