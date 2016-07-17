"""yadoma

Usage:
  yadoma [options] link <config>

Options:
  -d --debug  Activate debug

"""

import os

from docopt import docopt
import yaml

LINK = 'link'
SUBCOMMANDS = [LINK]
DEBUG = False


class CMDLineExit(Exception):
    pass


class ConfigError(Exception):
    pass


def debug(message):
    if DEBUG:
        print(message)


def get_subcommand(arguments):
    for subcommand in SUBCOMMANDS:
        if arguments[subcommand]:
            return subcommand
    else:
        raise CMDLineExit


def main():
    arguments = docopt(__doc__)
    global DEBUG
    if arguments['--debug']:
        DEBUG = True
    config_path = arguments['<config>']
    dir_name = os.path.dirname(arguments['<config>'])
    home_dir = os.environ['HOME']
    loaded_config = yaml.load(open(config_path).read())
    debug(loaded_config)
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
                debug("Will try to symlink '{0}' to '{1}'...".format(src, dest))
                try:
                    os.symlink(src, dest)

                except OSError as ose:
                    if ose.errno == 17:
                        debug("symlink exists")
                    else:
                        raise
                else:
                    debug("successful")

