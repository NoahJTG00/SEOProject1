import unittest
from unittest.mock import patch
from main import askLanguages, practice_phrases

class TestMainFunction(unittest.TestCase):
    
    def test_askLanguages(self):
        
        user_phrases, visiting_phrases, user_language, visiting_language = askLanguages()
        self.assertIsInstance(user_phrases, tuple)
        self.assertIsInstance(visiting_phrases, tuple)
        self.assertIsInstance(user_language, str)
        self.assertIsInstance(visiting_language, str)
    
    
    def test_practice_phrases(self):
        
        user_phrases = ['Hello', 'How are you']
        visiting_phrases = ['Bonjour', 'Comment ça va ?']
        user_language = 'English'
        visiting_language = 'French'
        result = practice_phrases(user_phrases, visiting_phrases, user_language, visiting_language)
        
        #self.assertEqual(result, str)
        self.assertIsNone(result)
        
        #return string instead of api call
        
if __name__ == '__main__':
    unittest.main()