# cloudmersive_voicerecognition_api_client.RecognizeApi

All URIs are relative to *https://testapi.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**speech_recognize_file_post**](RecognizeApi.md#speech_recognize_file_post) | **POST** /speech/recognize/file | Recognize audio input as text using Advanced AI


# **speech_recognize_file_post**
> SpeechRecognitionResult speech_recognize_file_post(language_code=language_code, recognition_mode=recognition_mode, speech_file=speech_file)

Recognize audio input as text using Advanced AI

Uses advanced AI to convert input audio to text. Supports WAV, MP3, M4A, FLAC, OGG, and WMA formats. Consumes 1 API call per second of audio in Fast mode, 5 API calls per second in Normal mode, and 10 API calls per second in Advanced mode.

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
language_code = '' # str | ISO 639-3 three-letter language code (e.g. eng, spa, fra). Empty for auto-detect. (optional) (default to )
recognition_mode = 'Normal' # str | Recognition mode: Fast, Normal (default), or Advanced. Advanced is only available on Private Cloud and Managed Instance deployments. (optional) (default to Normal)
speech_file = '/path/to/file.txt' # file |  (optional)

try:
    # Recognize audio input as text using Advanced AI
    api_response = api_instance.speech_recognize_file_post(language_code=language_code, recognition_mode=recognition_mode, speech_file=speech_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->speech_recognize_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| ISO 639-3 three-letter language code (e.g. eng, spa, fra). Empty for auto-detect. | [optional] [default to ]
 **recognition_mode** | **str**| Recognition mode: Fast, Normal (default), or Advanced. Advanced is only available on Private Cloud and Managed Instance deployments. | [optional] [default to Normal]
 **speech_file** | **file**|  | [optional] 

### Return type

[**SpeechRecognitionResult**](SpeechRecognitionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

