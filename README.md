# Rasa Open Source

[![Join the chat on Rasa Community Forum](https://img.shields.io/badge/forum-join%20discussions-brightgreen.svg)](https://forum.rasa.com/?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![PyPI version](https://badge.fury.io/py/rasa.svg)](https://badge.fury.io/py/rasa)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rasa.svg)](https://pypi.python.org/pypi/rasa)
[![Build Status](https://github.com/RasaHQ/rasa/workflows/Continuous%20Integration/badge.svg)](https://github.com/RasaHQ/rasa/actions)
[![Coverage Status](https://coveralls.io/repos/github/RasaHQ/rasa/badge.svg?branch=master)](https://coveralls.io/github/RasaHQ/rasa?branch=master)
[![Documentation Status](https://img.shields.io/badge/docs-stable-brightgreen.svg)](https://rasa.com/docs)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git.svg?type=shield)](https://app.fossa.com/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git?ref=badge_shield)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/orgs/RasaHQ/projects/23)

<img align="right" height="244" src="https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png">

Rasa is an open source machine learning framework to automate text-and voice-based conversations. With Rasa, you can build contextual assistants on:
- Facebook Messenger
- Slack
- Google Hangouts
- Webex Teams
- Microsoft Bot Framework
- Rocket.Chat
- Mattermost
- Telegram
- Twilio
- Your own custom conversational channels

or voice assistants as:
- Alexa Skills
- Google Home Actions

Rasa helps you build contextual assistants capable of having layered conversations with 
lots of back-and-forth. In order for a human to have a meaningful exchange with a contextual 
assistant, the assistant needs to be able to use context to build on things that were previously 
discussed – Rasa enables you to build assistants that can do this in a scalable way.


above all, if you have any interest in rasa， you can search all message in their
official website. https://rasa.com/

## what i am done

### convert poetry to ordinary python project

rasa version == 2.0.0a1

because i did not use poetry before, best way to me is convert this
project to ordinary python project.


so in this project, i add requirement.txt file which you can find all
the python modules in rasa.

first build python virtual environment
```bash
python3 -m venv venv
```

and activate this project

```bash
source venv/bin/activate
```

and  install all project requirements

```bash
pip install requirement.txt
```

and download spacy data
```bash
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

and start this project

```bash
python start.py
```

all rase knowledge , you can find it in rasa official website.

i just show you how to custom this project, and do some interesting things.


problem resolved

```buildoutcfg
raceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\person\venv\lib\site-packages\tensorflow\__init__.py", line 41, in <module>
    from tensorflow.python.tools import module_util as _module_util
  File "C:\person\venv\lib\site-packages\tensorflow\python\__init__.py", line 50, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "C:\person\venv\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 69, in <module>
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "C:\person\venv\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "C:\person\venv\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "C:\person\venv\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: DLL load failed: 找不到指定的模块。


Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/errors

for some common reasons and solutions.  Include the entire stack trace
```

windows download this
https://github.com/AshleyFang/Others/blob/master/Tools%20%26%20Zips/VC_redist.x64.exe


now you can custom your own robot

```buildoutcfg
python start.py init
```

```buildoutcfg
http://localhost:5005/webhooks/rest/webhook

{
	"sender": "test", "message": "i am fine"
}

```

how2custom 
introduce rasa in chinese