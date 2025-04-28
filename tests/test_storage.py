"""
Unit tests for storage functions.
"""

import unittest
import os
import json
from storage import read_json, write_json, read_csv, write_csv
import pandas as pd

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_json_file = 'test_students.json'
        self.test_data = [{'roll_number': 'AB12CD345', 'name': 'John Doe', 'email': 'john@example.com', 'marks': {'Math': 85, 'Science': 90}}]

    def tearDown(self):
        if os.path.exists(self.test_json_file):
            os.remove(self.test_json_file)

    def test_write_read_json(self):
        write_json(self.test_data)
        data = read_json()
        self.assertEqual(data, self.test_data)

    def test_write_read_csv(self):
        # Implement CSV write/read tests
        pass

if __name__ == '__main__':
    unittest.main()
### `tests/test_storage.py` (continued)
    def test_write_read_csv(self):
        df = pd.DataFrame(self.test_data)
        write_csv(df)
        read_data = read_csv()
        pd.testing.assert_frame_equal(df, read_data)

if __name__ == '__main__':
    unittest.main()
