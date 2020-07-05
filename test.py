import unittest
import start

class TestPolarityMethods(unittest.TestCase):

    def test_polarity_tag(self):
        polarities = [
            {'value': 0.01,"expected": "positive"},
            {'value': 0,"expected": "neutral"},
            {'value': -0.01,"expected": "negative"}
        ]

        for p in polarities:
            self.assertEqual(start.__polarity_tag(p['value']), p['expected'])
    
    def test_polarity_extended_tag(self):
        polarities = [
            {'value': 0.6,"expected": "extremly positive"},
            {'value': 0.2,"expected": "positive"},
            {'value': -0.2,"expected": "neutral"},
            {'value': -0.6,"expected": "negative"},
            {'value': -0.601,"expected": "extremly negative"}
        ]

        for p in polarities:
            self.assertEqual(start.polarity_extended_tag(p['value']), p['expected'])

    def test_configure_log_level(self):
        levels = [
            {'value': 'INFO', 'expected': start.logging.INFO},
            {'value': 'WARN', 'expected': start.logging.WARN},
            {'value': 'DEBUG', 'expected': start.logging.DEBUG}
        ]
        
        for l in levels:
            self.assertEqual(start.configure_log_level(l['value']), l['expected'])

if __name__ == '__main__':
    unittest.main()