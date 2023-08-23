import unittest
from functions import extractData, buildResults

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
                    "weight_1": 0.3,
                    "weight_2": 0.4,
                    "weight_3": 0.15,
                    "weight_4": 0.15     
                },
                {
                    "attendances": [0.0, 1.0, 10.0, 55.0],
                    "availabilities": [33.0, 22.0, 44.0, 55.0],
                    "weights": [0.3, 0.4, 0.15, 0.15]
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
                    "weight_1": 0.25,
                    "weight_2": 0.25,
                    "weight_3": 0.25,
                    "weight_4": 0.25     
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
