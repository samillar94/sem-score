import unittest
from functions import extractData, buildResponse

class TestExtractData(unittest.TestCase):
    extractDataSuites = {
        "valid": [
            [
                {
                    "attendance_1": 0,
                    "attendance_2": 1,
                    "attendance_3": 10,
                    "attendance_4": 55,
                    "availability_1": 33,
                    "availability_2": 22,
                    "availability_3": 44,
                    "availability_4": 55,
                    "unit_1": "hours",
                    "unit_2": "hours",
                    "unit_3": "hours",
                    "unit_4": "hours"     
                },
                {
                    "attendances": [0, 1, 10, 55],
                    "availabilities": [33, 22, 44, 55],
                    "unit": "hours"
                }   
            ],
            # Other valid test cases...
        ],
        "diffCounts": [
            [
                {
                    "attendance_1": 0,
                    "attendance_2": 1,
                    "availability_1": 33,
                    "availability_2": 22,
                    "availability_3": 44,
                    "availability_4": 9,
                    "unit_1": "hours",
                    "unit_2": "hours",
                    "unit_3": "hours",
                    "unit_4": "hours"     
                }   
            ],
            # Other diffCounts test cases...
        ]
    }

    def test_valid_extractData(self):
        for index, (input_data, expected_output) in enumerate(self.extractDataSuites["valid"], start=1):
            with self.subTest(msg=f'Test case {index}'):
                self.assertDictEqual(extractData(input_data), expected_output)

    def test_diffCounts_extractData(self):
        for index, input_data in enumerate(self.extractDataSuites["diffCounts"], start=1):
            with self.subTest(msg=f'Test case {index}'):
                with self.assertRaises(Exception):
                    extractData(input_data)
