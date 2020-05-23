# coding: utf-8

"""
    speechapi

    Speech APIs enable you to recognize speech and convert it to text using advanced machine learning, and also to convert text to speech.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_voicerecognition_api_client
from cloudmersive_voicerecognition_api_client.api.speak_api import SpeakApi  # noqa: E501
from cloudmersive_voicerecognition_api_client.rest import ApiException


class TestSpeakApi(unittest.TestCase):
    """SpeakApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_voicerecognition_api_client.api.speak_api.SpeakApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_speak_post(self):
        """Test case for speak_post

        Perform text-to-speech on a string  # noqa: E501
        """
        pass

    def test_speak_text_to_speech(self):
        """Test case for speak_text_to_speech

        Perform text-to-speech on a string  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()