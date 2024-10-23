import unittest
from unittest.mock import patch, call

from frankenzork.geneva import Geneva

import json

class TestMainRoom(unittest.TestCase):
    geneva = Geneva()
    with open('geneva.json', 'r') as f:
        script = json.load(f)
    @patch('builtins.input', side_effect=["Options"])
    @patch('builtins.print')
    def test_options(self, mock_print, mock_input):
        self.geneva.play()
        mock_print.assert_any_call(self.script['main']['init']['options'])


if __name__ == "__main__":
    unittest.main()
