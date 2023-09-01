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
            [
                {
                    "attendance_1": 0,
                    "attendance_2": 0,
                    "attendance_3": 0,
                    "attendance_4": 0,
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
                    "attendances": [0.0, 0.0, 0.0, 0.0],
                    "availabilities": [33.0, 22.0, 44.0, 55.0],
                    "weights": [0.3, 0.4, 0.15, 0.15]
                }   
            ],
            [
                {
                    "attendance_1": 33,
                    "attendance_2": 22,
                    "attendance_3": 44,
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
                    "attendances": [33.0, 22.0, 44.0, 55.0],
                    "availabilities": [33.0, 22.0, 44.0, 55.0],
                    "weights": [0.3, 0.4, 0.15, 0.15]
                }   
            ],
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

    buildResultsSuites = {
        "valid": [
            [
                {
                    "attendances": [0.0, 1.0, 10.0, 55.0],
                    "availabilities": [33.0, 22.0, 44.0, 55.0],
                    "weights": [0.3, 0.4, 0.15, 0.15]
                },
                {
                    "error": False,
                    "data": {
                        "score": 0.20227272727272727
                    },
                    "lines": [
                        "Engagement Score: 20%"
                    ]
                }   
            ],
            [
                {
                    "attendances": [5.0, 6.0, 7.0, 8.0],
                    "availabilities": [33.0, 22.0, 44.0, 55.0],
                    "weights": [0.3, 0.4, 0.15, 0.15]
                },
                {
                    "error": False,
                    "data": {
                        "score": 0.20022727272727275
                    },
                    "lines": [
                        "Engagement Score: 20%"
                    ]
                }   
            ],
            [
                {
                    "attendances": [0.0, 0.0, 0.0, 0.0],
                    "availabilities": [33.0, 22.0, 44.0, 55.0],
                    "weights": [0.3, 0.4, 0.15, 0.15]
                },
                                {
                    "error": False,
                    "data": {
                        "score": 0.0
                    },
                    "lines": [
                        "Engagement Score: 0%"
                    ]
                }   
            ],
            [
                {
                    "attendances": [33.0, 22.0, 44.0, 55.0],
                    "availabilities": [33.0, 22.0, 44.0, 55.0],
                    "weights": [0.3, 0.4, 0.15, 0.15]
                },
                                {
                    "error": False,
                    "data": {
                        "score": 0.0
                    },
                    "lines": [
                        "Engagement Score: 0%"
                    ]
                }   
            ],
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

    def test_valid_buildResults(self):
        for index, (input_data, expected_output) in enumerate(self.buildResultsSuites["valid"], start=1):
            with self.subTest(msg=f'Test case {index}'):
                self.assertDictEqual(buildResults(input_data), expected_output)
