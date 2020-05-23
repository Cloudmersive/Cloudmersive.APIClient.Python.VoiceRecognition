# coding: utf-8

"""
    speechapi

    Speech APIs enable you to recognize speech and convert it to text using advanced machine learning, and also to convert text to speech.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TextToSpeechRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'format': 'str',
        'text': 'str'
    }

    attribute_map = {
        'format': 'Format',
        'text': 'Text'
    }

    def __init__(self, format=None, text=None):  # noqa: E501
        """TextToSpeechRequest - a model defined in Swagger"""  # noqa: E501

        self._format = None
        self._text = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if text is not None:
            self.text = text

    @property
    def format(self):
        """Gets the format of this TextToSpeechRequest.  # noqa: E501

        File format for output audio file: wav or mp3, default is mp3  # noqa: E501

        :return: The format of this TextToSpeechRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this TextToSpeechRequest.

        File format for output audio file: wav or mp3, default is mp3  # noqa: E501

        :param format: The format of this TextToSpeechRequest.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def text(self):
        """Gets the text of this TextToSpeechRequest.  # noqa: E501

        Text to be converted to speech  # noqa: E501

        :return: The text of this TextToSpeechRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextToSpeechRequest.

        Text to be converted to speech  # noqa: E501

        :param text: The text of this TextToSpeechRequest.  # noqa: E501
        :type: str
        """

        self._text = text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TextToSpeechRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TextToSpeechRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
