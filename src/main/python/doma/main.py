"""doma

Usage:
  doma link <config>
"""

import os

from docopt import docopt
import yaml

LINK = 'link'
SUBCOMMANDS = [LINK]


class CMDLineExit(Exception):
    pass


class ConfigError(Exception):
    pass


def get_subcommand(arguments):
    for subcommand in SUBCOMMANDS:
        if arguments[subcommand]:
            return subcommand
    else:
        raise CMDLineExit


def main():
    arguments = docopt(__doc__)
    config_path = arguments['<config>']
    dir_name = os.path.dirname(arguments['<config>'])
    home_dir = os.environ['HOME']
    loaded_config = yaml.load(open(config_path).read())
    subcommand = get_subcommand(arguments)
    if subcommand == LINK:
        for program, program_config in loaded_config.items():
            for file_ in program_config['files']:
                try:
                    src = os.path.abspath(os.path.join(dir_name, file_['src']))
                except KeyError:
                    raise ConfigError("Missing 'src' entry")
                try:
                    dest = os.path.join(home_dir, file_['dest'])
                except KeyError:
                    dest = os.path.join(home_dir, file_['src'])
                os.symlink(src, dest)
