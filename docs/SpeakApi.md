# cloudmersive_voicerecognition_api_client.SpeakApi

All URIs are relative to *https://testapi.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**speech_speak_text_voice_basic_audio_post**](SpeakApi.md#speech_speak_text_voice_basic_audio_post) | **POST** /speech/speak/text/voice/basic/audio | Generate audio from text using Advanced AI


# **speech_speak_text_voice_basic_audio_post**
> str speech_speak_text_voice_basic_audio_post(body=body)

Generate audio from text using Advanced AI

Converts text to speech using advanced AI. Supports English, Spanish, French, Hindi, Italian, Japanese, Portuguese, and Chinese. Specify language with LanguageCode (ISO 639-3, default: eng) and gender with Gender (Male or Female, default: Female). Output format is controlled by the Format field (mp3 or wav, default: mp3). Consumes 1 API call per second of generated audio.

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
body = cloudmersive_voicerecognition_api_client.TextToSpeechRequest() # TextToSpeechRequest | String input request (optional)

try:
    # Generate audio from text using Advanced AI
    api_response = api_instance.speech_speak_text_voice_basic_audio_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeakApi->speech_speak_text_voice_basic_audio_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TextToSpeechRequest**](TextToSpeechRequest.md)| String input request | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

