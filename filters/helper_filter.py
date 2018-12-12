from filters.base_filter import BaseFilter
from boilerplate_templates.helpers_templates import gitignore_template, \
    cfg_handler_template, arg_parse_template


# `gitignore` adds a .gitignore file for git based python repo
def add_gitignore(zip_file):
    zip_file.writestr('.gitignore', gitignore_template)


# `config_handler` adds a ready to use config handler package
def add_config_handler(zip_file):
    zip_file.writestr('config/__init__.py', '')
    zip_file.writestr('config/cfg.ini', '')
    zip_file.writestr('config/cfg_handler.py', cfg_handler_template)


# `arg_parse` adds argparser helper file to make command-line tool
def add_argparse(zip_file):
    zip_file.writestr('argparse_helper.py', arg_parse_template)


class HelperFilter(BaseFilter):

    def handle_request(self, zip_file, args):

        if 'gitignore' in args:
            add_gitignore(zip_file)

        if 'config_handler' in args:
            add_config_handler(zip_file)

        if 'argparse' in args:
            add_argparse(zip_file)

        # handle successor if provided
        if self._successor is not None:
            self._successor.handle_request(zip_file, args)
