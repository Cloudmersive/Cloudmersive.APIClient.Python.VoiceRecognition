# cloudmersive_voicerecognition_api_client
Speech APIs enable you to recognize speech and convert it to text using advanced machine learning, and also to convert text to speech.

This Python package provides a native API client for [Cloudmersive Voice Recognition](https://cloudmersive.com/voice-recognition-and-speech-api)

- API version: v1
- Package version: 4.1.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_voicerecognition_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_voicerecognition_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://testapi.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RecognizeApi* | [**speech_recognize_file_post**](docs/RecognizeApi.md#speech_recognize_file_post) | **POST** /speech/recognize/file | Recognize audio input as text using Advanced AI
*SpeakApi* | [**speech_speak_text_voice_basic_audio_post**](docs/SpeakApi.md#speech_speak_text_voice_basic_audio_post) | **POST** /speech/speak/text/voice/basic/audio | Generate audio from text using Advanced AI


## Documentation For Models

 - [SpeechRecognitionResult](docs/SpeechRecognitionResult.md)
 - [TextToSpeechRequest](docs/TextToSpeechRequest.md)
 - [TokenTimestamp](docs/TokenTimestamp.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



