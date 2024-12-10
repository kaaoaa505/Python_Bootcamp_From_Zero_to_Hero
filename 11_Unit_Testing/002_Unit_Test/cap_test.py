'''
To test cap.py
'''
import unittest
import cap

class TestCap(unittest.TestCase):
    '''
    Using unittest to test capitalize text
    '''
    def test_one_word(self):
        '''
        Assert that a word after applying cap_text becomes capitalized
        '''
        text = 'khaled'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Khaled')

    def test_multiple_words(self):
        '''
        Assert that multiple words after applying cap_text becomes capitalized
        '''
        text = 'khaled allam ahmed'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Khaled Allam Ahmed')

if __name__ == '__main__':
    unittest.main()