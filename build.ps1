﻿#Remove-Item –path ./ –recurse
& java -jar swagger-codegen-cli-2.4.5.jar generate -i https://api.cloudmersive.com/swagger/api/nlpv2 -l python -c packageconfig.json
#(Get-Content ./client/package.json).replace('v1', '1.0.1') | Set-Content ./client/package.json

$extrasetup = (Get-Content ./extrasetup.py) -join "`n"
Write-Host $extrasetup
(Get-Content ./setup.py).replace('# http://pypi.python.org/pypi/setuptools', $extrasetup) | Set-Content ./setup.py
(Get-Content ./setup.py).replace('"""\', "long_description,`n    long_description_content_type='text/markdown'") | Set-Content ./setup.py
(Get-Content ./setup.py).replace('The powerful Natural Language Processing APIs (v2) let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501', '') | Set-Content ./setup.py
(Get-Content ./setup.py).replace('    """', '') | Set-Content ./setup.py
(Get-Content ./README.md).replace('This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:', 'This Python package provides a native API client for [Cloudmersive NLP](https://www.cloudmersive.com/nlp-api)') | Set-Content ./README.md
Write-Host "Done."