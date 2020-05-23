# coding: utf-8

# flake8: noqa

"""
    speechapi

    Speech APIs enable you to recognize speech and convert it to text using advanced machine learning, and also to convert text to speech.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from cloudmersive_voicerecognition_api_client.api.recognize_api import RecognizeApi
from cloudmersive_voicerecognition_api_client.api.speak_api import SpeakApi

# import ApiClient
from cloudmersive_voicerecognition_api_client.api_client import ApiClient
from cloudmersive_voicerecognition_api_client.configuration import Configuration
# import models into sdk package
from cloudmersive_voicerecognition_api_client.models.speech_recognition_result import SpeechRecognitionResult
from cloudmersive_voicerecognition_api_client.models.text_to_speech_request import TextToSpeechRequest
