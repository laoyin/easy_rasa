import re
regex = re.compile('\s+')


import_package_list = """absl-py                       0.9.0           Abseil Python Common Libraries, see https://github.com/abseil/abseil-py.
aiofiles                      0.5.0           File support for asyncio.
aiohttp                       3.6.2           Async http client/server framework (asyncio)
aioresponses                  0.6.4           Mock out requests made by ClientSession from aiohttp package
alabaster                     0.7.12          A configurable sidebar-enabled Sphinx theme
apipkg                        1.5             apipkg: namespace control and lazy-import mechanism
appdirs                       1.4.4           A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".
apscheduler                   3.6.3           In-process task scheduler with Cron-like capabilities
argh                          0.26.2          An unobtrusive argparse wrapper with natural syntax
astunparse                    1.6.3           An AST unparser for Python
async-generator               1.10            Async generators and context managers for Python 3.5+
async-timeout                 3.0.1           Timeout context manager for asyncio programs
attrs                         19.3.0          Classes Without Boilerplate
aws-sam-translator            1.25.0          AWS SAM Translator is a library that transform SAM templates into AWS CloudFormation templates
aws-xray-sdk                  2.6.0           The AWS X-Ray SDK for Python (the SDK) enables Python developers to record and emit information from within their applications to the AWS X-Ray ...
azure-core                    1.7.0           Microsoft Azure Core Library for Python
azure-storage-blob            12.3.2          Microsoft Azure Blob Storage Client Library for Python
babel                         2.8.0           Internationalization utilities
black                         19.10b0         The uncompromising code formatter.
bleach                        3.1.5           An easy safelist-based HTML-sanitizing tool.
blis                          0.4.1           The Blis BLAS-like linear algebra library, as a self-contained C-extension.
boto                          2.49.0          Amazon Web Services Library
boto3                         1.14.20         The AWS SDK for Python
botocore                      1.17.20         Low-level, data-driven core of boto 3.
cachetools                    4.1.1           Extensible memoizing collections and decorators
catalogue                     1.0.0           Super lightweight function registries for your library
certifi                       2020.6.20       Python package for providing Mozilla's CA Bundle.
cffi                          1.14.0          Foreign Function Interface for Python calling C code.
cfn-lint                      0.33.2          Checks CloudFormation templates for practices and behaviour that could potentially be improved
chardet                       3.0.4           Universal encoding detector for Python 2 and 3
click                         7.1.2           Composable command line interface toolkit
cloudpickle                   1.3.0           Extended pickling support for Python objects
colorclass                    2.2.0           Colorful worry-free console applications for Linux, Mac OS X, and Windows.
coloredlogs                   14.0            Colored terminal output for Python's logging module
colorhash                     1.0.2           Generate a color based on a value
coverage                      5.2             Code coverage measurement for Python
coveralls                     2.1.1           Show coverage stats online via coveralls.io
cryptography                  2.9.2           cryptography is a package which provides cryptographic recipes and primitives to Python developers.
cycler                        0.10.0          Composable style cycles
cymem                         2.0.3           Manage calls to calloc/free through Cython
decorator                     4.4.2           Decorators for Humans
defusedxml                    0.6.0           XML bomb protection for Python stdlib modules
dnspython                     1.16.0          DNS toolkit
docker                        4.2.2           A Python library for the Docker Engine API.
docopt                        0.6.2           Pythonic argument parser, that will make you smile
docutils                      0.15.2          Docutils -- Python Documentation Utilities
ecdsa                         0.15            ECDSA cryptographic signature library (pure python)
entrypoints                   0.3             Discover and load entry points from installed packages.
execnet                       1.7.1           execnet: rapid multi-Python deployment
fakeredis                     1.4.1           Fake implementation of redis API for testing purposes.
fbmessenger                   6.0.0           A python library to communicate with the Facebook Messenger API's
filelock                      3.0.12          A platform independent file lock.
flake8                        3.8.3           the modular source code checker: pep8 pyflakes and co
freezegun                     0.3.15          Let your Python tests travel through time
future                        0.18.2          Clean single-source support for Python 3 and 2
gast                          0.3.3           Python AST that abstracts the underlying Python version
github3.py                    1.3.0           Python wrapper for the GitHub API(http://developer.github.com/v3)
google-api-core               1.21.0          Google API client core library
google-auth                   1.18.0          Google Authentication Library
google-auth-oauthlib          0.4.1           Google Authentication Library
google-cloud-core             1.3.0           Google Cloud API client core library
google-cloud-storage          1.29.0          Google Cloud Storage API client library
google-pasta                  0.2.0           pasta is an AST-based Python refactoring library
google-resumable-media        0.5.1           Utilities for Google Media Downloads and Resumable Uploads
googleapis-common-protos      1.52.0          Common protobufs used in Google APIs
grpcio                        1.30.0          HTTP/2-based RPC framework
h11                           0.8.1           A pure-Python, bring-your-own-I/O implementation of HTTP/1.1
h2                            3.2.0           HTTP/2 State-Machine based protocol implementation
h5py                          2.10.0          Read and write HDF5 files from Python
hpack                         3.0.0           Pure-Python HPACK header compression
hstspreload                   2020.7.7        Chromium HSTS Preload list as a Python package and updated daily
httplib2                      0.18.1          A comprehensive HTTP client library.
httptools                     0.1.1           A collection of framework independent HTTP protocol utils.
httpx                         0.9.3           The next generation HTTP client.
humanfriendly                 8.2             Human friendly output for text interfaces using Python
hyperframe                    5.2.0           HTTP/2 framing layer for Python
idna                          2.8             Internationalized Domain Names in Applications (IDNA)
imagesize                     1.2.0           Getting image size from png/jpeg/jpeg2000/gif file
importlab                     0.5.1           A library to calculate python dependency graphs.
importlib-metadata            1.7.0           Read metadata from Python packages
incremental                   17.5.0
ipaddress                     1.0.23          IPv4/IPv6 manipulation library
ipython-genutils              0.2.0           Vestigial utilities from IPython
isodate                       0.6.0           An ISO 8601 date/time/duration parser and formatter
jieba                         0.42.1          Chinese Words Segmentation Utilities
jinja2                        2.11.2          A very fast and expressive template engine.
jmespath                      0.10.0          JSON Matching Expressions
joblib                        0.15.1          Lightweight pipelining: using Python functions as pipeline jobs.
jsondiff                      1.1.2           Diff JSON and JSON-like structures in Python
jsonpatch                     1.26            Apply JSON-Patches (RFC 6902)
jsonpickle                    1.4.1           Python library for serializing any arbitrary object graph into JSON
jsonpointer                   2.0             Identify specific nodes in a JSON document (RFC 6901)
jsonschema                    3.2.0           An implementation of JSON Schema validation for Python
junit-xml                     1.9             Creates JUnit XML test result documents that can be read by tools such as Jenkins
jupyter-core                  4.6.3           Jupyter core package. A base package on which Jupyter projects rely.
jwcrypto                      0.7             Implementation of JOSE Web standards
kafka-python                  2.0.1           Pure Python client for Apache Kafka
keras-preprocessing           1.1.2           Easy data preprocessing and data augmentation for deep learning models
kiwisolver                    1.2.0           A fast implementation of the Cassowary constraint solver
livereload                    2.6.2           Python LiveReload is an awesome tool for web developers
markdown                      3.2.2           Python implementation of Markdown.
markupsafe                    1.1.1           Safely add untrusted strings to HTML/XML markup.
matplotlib                    3.2.2           Python plotting package
mattermostwrapper             2.2             A mattermost api v4 wrapper to interact with api
mccabe                        0.6.1           McCabe checker, plugin for flake8
mistune                       0.8.4           The fastest markdown parser in pure Python
mock                          4.0.2           Rolling backport of unittest.mock for all Pythons
mongomock                     3.19.0          Fake pymongo stub for testing simple MongoDB-dependent code
more-itertools                8.4.0           More routines for operating on iterables, beyond itertools
moto                          1.3.14          A library that allows your python tests to easily mock out the boto library
msrest                        0.6.17          AutoRest swagger generator Python client runtime.
multidict                     4.7.6           multidict implementation
murmurhash                    1.0.2           Cython bindings for MurmurHash
nbconvert                     5.6.1           Converting Jupyter Notebooks
nbformat                      5.0.7           The Jupyter Notebook format
nbsphinx                      0.7.1           Jupyter Notebook Tools for Sphinx
networkx                      2.4             Python package for creating and manipulating graphs and networks
ninja                         1.10.0.post1    Ninja is a small build system with a focus on speed
numpy                         1.19.0          NumPy is the fundamental package for array computing with Python.
oauth2client                  4.1.3           OAuth 2.0 client library
oauthlib                      3.1.0           A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
opt-einsum                    3.2.1           Optimizing numpys einsum function
packaging                     20.4            Core utilities for Python packages
pandocfilters                 1.4.2           Utilities for writing pandoc filters in python
pathspec                      0.8.0           Utility library for gitignore style pattern matching of file paths.
pathtools                     0.1.2           File system general utilities
pep440-version-utils          0.3.0           Utilities to deal with pep440 versioning
pika                          1.1.0           Pika Python AMQP Client Library
plac                          1.1.3           The smartest command line arguments parser in the world
pluggy                        0.13.1          plugin and hook calling mechanisms for python
port-for                      0.3.1           Utility that helps with local TCP ports managment. It can find an unused TCP localhost port and remember the association.
preshed                       3.0.2           Cython hash table that trusts the keys are pre-hashed
prompt-toolkit                2.0.10          Library for building powerful interactive command lines in Python
protobuf                      3.12.2          Protocol Buffers
psycopg2-binary               2.8.5           psycopg2 - Python-PostgreSQL Database Adapter
py                            1.9.0           library with cross-python path, ini-parsing, io, code, log facilities
pyasn1                        0.4.8           ASN.1 types and codecs
pyasn1-modules                0.2.8           A collection of ASN.1-based protocols modules.
pycodestyle                   2.6.0           Python style guide checker
pycparser                     2.20            C parser in Python
pydot                         1.4.1           Python interface to Graphviz's Dot
pyflakes                      2.2.0           passive checker of Python programs
pygments                      2.6.1           Pygments is a syntax highlighting package written in Python.
pyjwt                         1.7.1           JSON Web Token implementation in Python
pykwalify                     1.7.0           Python lib/cli for JSON/YAML schema validation
pymongo                       3.10.1          Python driver for MongoDB <http://www.mongodb.org>
pypandoc                      1.5             Thin wrapper for pandoc.
pyparsing                     2.4.7           Python parsing module
pyrsistent                    0.16.0          Persistent/Functional/Immutable data structures
pytest                        5.4.3           pytest: simple powerful testing with Python
pytest-asyncio                0.10.0          Pytest support for asyncio.
pytest-cov                    2.10.0          Pytest plugin for measuring coverage.
pytest-forked                 1.2.0           run tests in isolated forked subprocesses
pytest-localserver            0.5.0           py.test plugin to test server connections locally.
pytest-sanic                  1.6.1           a pytest plugin for Sanic
pytest-xdist                  1.33.0          pytest xdist plugin for distributed testing and loop-on-failing modes
python-crfsuite               0.9.7           Python binding for CRFsuite
python-dateutil               2.8.1           Extensions to the standard Python datetime module
python-engineio               3.13.1          Engine.IO server
python-jose                   3.1.0           JOSE implementation in Python
python-socketio               4.6.0           Socket.IO server
python-telegram-bot           12.8            We have made you a wrapper you can't refuse
pytype                        2020.6.26       Python type inferencer
pytz                          2020.1          World timezone definitions, modern and historical
pyyaml                        5.3.1           YAML parser and emitter for Python
questionary                   1.5.2           Python library to build pretty command line user prompts ⭐️
rasa-sdk                      2.0.0a1         Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, an...
rasabaster                    0.7.26          A configurable sidebar-enabled Sphinx theme
redis                         3.5.3           Python client for Redis key-value store
regex                         2020.6.8        Alternative regular expression module, to replace re.
requests                      2.24.0          Python HTTP for Humans.
requests-oauthlib             1.3.0           OAuthlib authentication support for Requests.
requests-toolbelt             0.9.1           A utility belt for advanced users of python-requests
responses                     0.10.15         A utility library for mocking out the `requests` Python library.
rfc3986                       1.4.0           Validating URI References per RFC 3986
rocketchat-api                1.4             Python API wrapper for Rocket.Chat
rsa                           4.6             Pure-Python RSA implementation
ruamel.yaml                   0.16.10         ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order
ruamel.yaml.clib              0.2.0           C version of reader, parser and emitter for ruamel.yaml derived from libyaml
s3transfer                    0.3.3           An Amazon S3 Transfer Manager
sacremoses                    0.0.43          SacreMoses
sanic                         19.12.2         A web server and web framework that's written to go fast. Build fast. Run fast.
sanic-cors                    0.10.0.post3    A Sanic extension adding a decorator for CORS support. Based on flask-cors by Cory Dolphin.
sanic-jwt                     1.4.1           JWT oauth flow for Sanic
sanic-plugins-framework       0.9.3           Doing all of the boilerplate to create a Sanic Plugin, so you don't have to.
scikit-learn                  0.23.1          A set of python modules for machine learning and data mining
scipy                         1.4.1           SciPy: Scientific Library for Python
sentencepiece                 0.1.92          SentencePiece python wrapper
sentinels                     1.0.0           Various objects to denote special meanings in python
six                           1.15.0          Python 2 and 3 compatibility utilities
sklearn-crfsuite              0.3.6           CRFsuite (python-crfsuite) wrapper which provides interface simlar to scikit-learn
slackclient                   2.7.2           Slack API clients for Web API and RTM API
sniffio                       1.1.0           Sniff out which async library your code is running under
snowballstemmer               2.0.0           This package provides 26 stemmers for 25 languages generated from Snowball algorithms.
sortedcontainers              2.2.2           Sorted Containers -- Sorted List, Sorted Dict, Sorted Set
spacy                         2.2.4           Industrial-strength Natural Language Processing (NLP) in Python
sphinx                        3.1.2           Python documentation generator
sphinx-autobuild              0.7.1           Watch a Sphinx directory and rebuild the documentation when a change is detected. Also includes a livereload enabled web server.
sphinx-autodoc-typehints      1.10.3          Type hints (PEP 484) support for the Sphinx autodoc extension
sphinx-rtd-theme              0.2.5b1 6b89a7c Read the Docs theme for Sphinx
sphinx-tabs                   1.1.13          Tab views for Sphinx
sphinxcontrib-applehelp       1.0.2           sphinxcontrib-applehelp is a sphinx extension which outputs Apple help books
sphinxcontrib-devhelp         1.0.2           sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.
sphinxcontrib-htmlhelp        1.0.3           sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files
sphinxcontrib-httpdomain      1.7.0           Sphinx domain for documenting HTTP APIs
sphinxcontrib-jsmath          1.0.1           A sphinx extension which renders display math in HTML via JavaScript
sphinxcontrib-programoutput   0.16            Sphinx extension to include program output
sphinxcontrib-qthelp          1.0.3           sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.
sphinxcontrib-serializinghtml 1.1.4           sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized" HTML files (json and pickle).
sphinxcontrib-trio            1.1.2           Make Sphinx better at documenting Python functions and methods
sphinxcontrib-versioning      2.2.1 b335b37   Sphinx extension that allows building versioned docs for self-hosting.
sphinxcontrib-websupport      1.2.3           Sphinx API for Web Apps
sqlalchemy                    1.3.18          Database Abstraction Library
srsly                         1.0.2           Modern high-performance serialization utilities for Python
sshpubkeys                    3.1.0           SSH public key parser
tabulate                      0.8.7           Pretty-print tabular data
tensorboard                   2.2.2           TensorBoard lets you watch Tensors Flow
tensorboard-plugin-wit        1.7.0           What-If Tool TensorBoard plugin.
tensorflow                    2.2.0           TensorFlow is an open source machine learning framework for everyone.
tensorflow-addons             0.10.0          TensorFlow Addons.
tensorflow-estimator          2.2.0           TensorFlow Estimator.
tensorflow-hub                0.8.0           TensorFlow Hub is a library to foster the publication, discovery, and consumption of reusable parts of machine learning models.
tensorflow-probability        0.10.1          Probabilistic modeling and statistical inference in TensorFlow
tensorflow-text               2.2.1           TF.Text is a TensorFlow library of text related ops, modules, and subgraphs.
termcolor                     1.1.0           ANSII Color formatting for output in terminal.
terminaltables                3.1.0           Generate simple tables in terminals from a nested list of strings.
testpath                      0.4.4           Test utilities for code working with files and commands
thinc                         7.4.0           Practical Machine Learning for NLP
threadpoolctl                 2.1.0           threadpoolctl
tokenizers                    0.7.0           Fast and Customizable Tokenizers
toml                          0.10.1          Python Library for Tom's Obvious, Minimal Language
tornado                       6.0.4           Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
towncrier                     19.2.0          Building newsfiles for your project.
tqdm                          4.47.0          Fast, Extensible Progress Meter
traitlets                     4.3.3           Traitlets Python config system
transformers                  2.11.0          State-of-the-art Natural Language Processing for TensorFlow 2.0 and PyTorch
twilio                        6.42.0          Twilio API client and TwiML generator
typed-ast                     1.4.1           a fork of Python 2 and 3 ast modules with type comment support
typeguard                     2.9.1           Run-time type checker for Python
tzlocal                       2.1             tzinfo object for the local timezone
ujson                         3.0.0           Ultra fast JSON encoder and decoder for Python
uritemplate                   3.0.1           URI templates
urllib3                       1.25.9          HTTP library with thread-safe connection pooling, file post, and more.
uvloop                        0.14.0          Fast implementation of asyncio event loop on top of libuv
wasabi                        0.7.0           A lightweight console printing and formatting toolkit
watchdog                      0.10.3          Filesystem events monitoring
wcwidth                       0.2.5           Measures the displayed width of unicode strings in a terminal
webencodings                  0.5.1           Character encoding aliases for legacy web content
webexteamssdk                 1.3             Community-developed Python SDK for the Webex Teams APIs
websocket-client              0.57.0          WebSocket client for Python. hybi13 is supported.
websockets                    8.0.2           An implementation of the WebSocket Protocol (RFC 6455 & 7692)
werkzeug                      1.0.1           The comprehensive WSGI web application library.
wheel                         0.34.2          A built-package format for Python
wrapt                         1.12.1          Module for decorators, wrappers and monkey patching.
xmltodict                     0.12.0          Makes working with XML feel like you are working with JSON
yarl                          1.4.2           Yet another URL library
zipp                          3.1.0
"""

aa = import_package_list.split("\n")
for a in aa:
    if a:
        # require_package_list = a.split('\t')
        require_package_list = regex.split(a)
        # print(require_package_list)
        print("pip  install " + require_package_list[0]+"=="+require_package_list[1])


