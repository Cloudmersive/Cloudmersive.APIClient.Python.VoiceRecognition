# cloudmersive_voicerecognition_api_client.RecognizeApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recognize_file**](RecognizeApi.md#recognize_file) | **POST** /speech/recognize/file | Recognize audio input as text using machine learning


# **recognize_file**
> SpeechRecognitionResult recognize_file(speech_file)

Recognize audio input as text using machine learning

Uses advanced machine learning to convert input audio, which can be mp3 or wav, into text.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_voicerecognition_api_client
from cloudmersive_voicerecognition_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_voicerecognition_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_voicerecognition_api_client.RecognizeApi(cloudmersive_voicerecognition_api_client.ApiClient(configuration))
speech_file = '/path/to/file.txt' # file | Speech file to perform the operation on.  Common file formats such as WAV, MP3 are supported.

try:
    # Recognize audio input as text using machine learning
    api_response = api_instance.recognize_file(speech_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **speech_file** | **file**| Speech file to perform the operation on.  Common file formats such as WAV, MP3 are supported. | 

### Return type

[**SpeechRecognitionResult**](SpeechRecognitionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

