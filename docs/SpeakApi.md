# cloudmersive_voicerecognition_api_client.SpeakApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**speak_post**](SpeakApi.md#speak_post) | **POST** /speech/speak/text/basicVoice/{format} | Perform text-to-speech on a string
[**speak_text_to_speech**](SpeakApi.md#speak_text_to_speech) | **POST** /speech/speak/text/voice/basic/audio | Perform text-to-speech on a string


# **speak_post**
> object speak_post(format, text)

Perform text-to-speech on a string

Takes as input a string and a file format (mp3 or wav) and outputs a wave form in the appropriate format.

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
api_instance = cloudmersive_voicerecognition_api_client.SpeakApi(cloudmersive_voicerecognition_api_client.ApiClient(configuration))
format = 'format_example' # str | File format to generate response in; possible values are \"mp3\" or \"wav\"
text = 'text_example' # str | The text you would like to conver to speech.  Be sure to surround with quotes, e.g. \"The quick brown fox jumps over the lazy dog.\"

try:
    # Perform text-to-speech on a string
    api_response = api_instance.speak_post(format, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeakApi->speak_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format to generate response in; possible values are \&quot;mp3\&quot; or \&quot;wav\&quot; | 
 **text** | **str**| The text you would like to conver to speech.  Be sure to surround with quotes, e.g. \&quot;The quick brown fox jumps over the lazy dog.\&quot; | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speak_text_to_speech**
> object speak_text_to_speech(req_config)

Perform text-to-speech on a string

Takes as input a string and a file format (mp3 or wav) and outputs a wave form in the appropriate format.

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
api_instance = cloudmersive_voicerecognition_api_client.SpeakApi(cloudmersive_voicerecognition_api_client.ApiClient(configuration))
req_config = cloudmersive_voicerecognition_api_client.TextToSpeechRequest() # TextToSpeechRequest | String input request

try:
    # Perform text-to-speech on a string
    api_response = api_instance.speak_text_to_speech(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeakApi->speak_text_to_speech: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**TextToSpeechRequest**](TextToSpeechRequest.md)| String input request | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

