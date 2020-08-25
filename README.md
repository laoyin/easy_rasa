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

and start this project

```bash
python start.py
```

all rase knowledge , you can find it in rasa official website.

i just show you how to custom this project, and do some interesting things.
