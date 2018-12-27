
# Templates for Helper files

gitignore_template = '''
### Python ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# dotenv
.env

# virtualenv
.venv
venv/
ENV/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site
'''


cfg_handler_template = '''
""" cfg_handler.py: This module reads the configuration file and make the configuration params
                    for use for other modules """

import os
from configparser import ConfigParser


class CfgHandlerError(Exception):
    pass


class CfgHandler(ConfigParser, object):
    """
    CfgHandler handles all configuration related task; Reads
    the configuration file and make all configuration parameters
    available for use.
    """

    _defaultConfigFileName = "cfg.ini"
    _configFileInUse = None

    def __init__(self, cfg_file=None):
        """
        Constructor
        @param cfg_file: Configuration file path with name,
         if not provided then default is used: config/cfg.ini
        """
        super(CfgHandler, self).__init__()
        self.load_configuration(cfg_file)

    def load_configuration(self, cfg_file):
        """
        Load the configuration file in memory
        @raise CfgHandlerError: If configuration file cannot be loaded
        """
        self._configFileInUse = (os.path.abspath(os.path.dirname(__file__)) + os.sep +
                                 self._defaultConfigFileName) if cfg_file is None else cfg_file

        lst = self.read(self._configFileInUse)

        if len(lst) == 0:
            raise CfgHandlerError("Config file not found")

    def get_cfg_file_in_use(self):
        return self._configFileInUse
'''

arg_parse_template = '''
import argparse

def setup_parameters():
    """
    Set up the command line parameters
    """

    parser = argparse.ArgumentParser(description='Sample project')
    parser.add_argument('-l', '--loglevel', action='store', metavar='Log level',
                        dest='log_level', type=int,
                        help='Specify the log level')
    parser.add_argument('-v', '--version', action='store_true', dest='version',
                        help='Display version number')

    return parser.parse_args()

'''
